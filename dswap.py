#!/usr/bin/env python

import operator, functools, subprocess, sys, json, os
import classes
from common import apply_f, compose, attrdict, Rattrdict
from coordinates import Commands, Skill, Skills, VALID_SLOTS,\
    SLOT_ASSOC, SPARE_PASSIVES

p = functools.partial
op = operator
jp = p(json.dumps, indent = 2)

(
    ADD, SWITCH, USE, REMOVE, ASSIGN, LIST,
    SHOW, STORE, REVERT, CHARACTER, BUILD
) = (
    'add', 'switch', 'use', 'remove', 'assign', 'list',
    'show', 'store', 'revert', 'character', 'build'
)

@apply_f('\n'.join)
def skill_movement(old_ability, new_ability):
    (o_page, o_ability), o_rune = old_ability
    (n_page, n_ability), n_rune = new_ability
    page_turns = n_page - o_page
    direction = Skill.right
    if n_page < o_page:
        direction = Skill.left 
    yield Commands.mousemove % direction
    for n in range(abs(n_page - o_page)):
        yield Commands.click_1
    yield Commands.mousemove % n_ability
    yield Commands.click_1
    yield Commands.mousemove % n_rune
    yield Commands.click_1
    yield Commands.mousemove % Skill.accept
    yield Commands.click_1

@apply_f('\n'.join)
def passive_movement(skill, passive):
    yield Commands.mousemove % skill
    yield Commands.click_1
    yield Commands.mousemove % passive
    yield Commands.click_1
    yield Commands.mousemove % Skill.accept
    yield Commands.click_1

@apply_f('\n'.join)
def generate_script(current, proposed):
    def indexer(n):
        def _indexer(indexable):
            return indexable[n]
        return _indexer
    car = indexer(0)
    cadr = indexer(1)

    def internal_build(build):
        actives = ( )
        passives = ( )
        for slot, ability in build.items():
            internal_slot = SLOT_ASSOC.get(slot)
            internal_ability = classes.ABILITY_ASSOC.get(ability)
            if internal_slot in Skills.active:
                actives += ((internal_slot, internal_ability),)
            if internal_slot in Skills.passive:
                passives += ((internal_slot, internal_ability),)
        return actives, passives

    def make_movements(current, proposed):
        movements = ( )
        proposed_map = dict(proposed)
        for slot, ability in current:
            if slot not in proposed_map:
                raise Exception('Script failed, slot mismatch')
            movements += ((slot, ability, proposed_map[slot]),)
        return movements

    def clear_passives(current, proposed):
        cslots, cabils = zip(*current)
        pslots, pabils = zip(*proposed)
        used = set(cabils + pabils)
        return zip(cslots, set(SPARE_PASSIVES) - used)

    current_actives, current_passives = internal_build(current)
    proposed_actives, proposed_passives = internal_build(proposed)

    if not set(map(compose(car, cadr), current_actives)) ^\
            set(map(compose(car, cadr), proposed_actives)):
        raise Exception('Script failed, deadlock')
    movements = make_movements(current_actives, proposed_actives)

    yield Commands.search
    yield Commands.windowactivate
    yield Commands.key_s
    while movements:
        movement, movements = movements[-1], movements[:-1]
        skill, current, proposed = movement
        if car(proposed) not in map(compose(car, cadr), movements):
            yield Commands.mousemove % skill
            yield Commands.click_1
            yield skill_movement(current, proposed)
        else:
            movements = (movement,) + movements

    for skill, passive in clear_passives(current_passives, proposed_passives):
        yield passive_movement(skill, passive)
    for skill, passive in proposed_passives:
        yield passive_movement(skill, passive)


Error = Exception('Invalid input')
def Errorf(*args):
    raise Error

def handle_input(config, arguments):
    # Character handlers
    def character_add(name):
        print config.characters
        config.characters[name] = attrdict(
            name = name,
            builds = { },
            last_build = None,
            build = None,
        )
        return 'Character %s added' % name

    def character_use(name):
        if name in config.characters:
            config.current_character = name
            return 'Using character %s' % name
        return 'Unable to find character %s' % name

    def character_remove(name):
        if name == config.current_character:
            return 'Cannot remove current character'
        if name in config.characters:
            del config.characters[name]
            return 'Removed character %s' % name
        return 'Cannot remove character %s, not found' % name

    def character_list():
        return jp(config.characters.keys())

    def character_show(name = None):
        if name and name in config.characters:
            return jp(config.characters[name])
        return jp(config.characters[config.current_character])

    # Build handlers
    def build_add(name):
        character = config.characters[config.current_character]
        character.builds[name] = attrdict(
            name = name,
        )
        return 'Added build %s' % name

    def build_switch(name):
        character = config.characters[config.current_character]
        if name in character.builds:
            character.last_build = character.build
            character.build = character.builds[name]
            return 'Switching to build %s' % name
        return 'Could not find build %s' % name

    def build_use(name):
        character = config.characters[config.current_character]
        if name in character.builds:
            character.last_build = character.build
            character.build = character.builds[name]
            script = generate_script(character.last_build, character.build)
            subprocess.call(script, shell = True)
            return 'Using build %s' % name
        return 'Could not find build %s' % name

    def build_remove(name):
        character = config.characters[config.current_character]
        if name == character.build.name:
            return 'Cannot remove current build'
        if name in character.builds:
            del character.builds[name]
            return 'Removed build %s' % name
        return 'Cannot remove build %s, not found' % name
        raise Error

    def build_list():
        character = config.characters[config.current_character]
        return jp(character.builds.keys())

    def build_show(name = None):
        character = config.characters[config.current_character]
        if name and name in character.builds:
            return jp(character.builds[name])
        return jp(character.build)

    def build_assign(slot, ability):
        character = config.characters[config.current_character]
        if slot in VALID_SLOTS and ability in classes.KNOWN_ABILITIES:
            character.build[slot] = ability
            return 'Assigning %s to %s in build %s' %\
                    (slot, ability, character.build.name)
        return slot in VALID_SLOTS and 'Invalid ability' or 'Invalid slot'

    def build_store(name = None):
        character = config.characters[config.current_character]
        name = name or character.build.name
        character.builds[name] = character.build
        character.builds[name].name = name
        return 'Storing current build as %s' % name

    def build_revert(name = None):
        character = config.characters[config.current_character]
        character.build, character.last_build =\
                character.last_build, character.build
        return 'Reverting to build %s' % character.build.name

    if len(arguments) < 2:
        return 'Invalid argument count'
    arguments = map(op.methodcaller('lower'), arguments)
    section, command = arguments[:2]
    arguments = arguments[2:]
    handlers = {
        CHARACTER: {
            ADD: character_add,
            USE: character_use,
            REMOVE: character_remove,
            LIST: character_list,
            SHOW: character_show,
        },
        BUILD: {
            ADD: build_add,
            USE: build_use,
            SWITCH: build_switch,
            REMOVE: build_remove,
            LIST: build_list,
            SHOW: build_show,
            ASSIGN: build_assign,
            STORE: build_store,
            REVERT: build_revert,
        }
    }
    if section in handlers:
        return handlers[section].get(command, Errorf)(*arguments)

if __name__ == '__main__':
    fpath = 'mybuilds'
    config = attrdict(
        characters = { },
        current_character = None
    )
    if os.path.exists(fpath):
        with open(fpath) as fin:
            try:
                config = Rattrdict(json.load(fin)) or config
            except Exception, e:
                print e
    print handle_input(config, sys.argv[1:])
    with open('mybuilds', 'w') as fout:
        json.dump(config, fout, indent = 2)
