class Commands:
    header = '#!/usr/bin/env sh'
    search = 'WID=`xdotool search --name "^Diablo III$" | tail -1`'
    mousemove = 'xdotool mousemove %d %d; sleep .15'
    windowactivate = 'xdotool windowactivate --sync $WID'
    key = 'xdotool key %s'
    key_s = key % 's'
    click = 'xdotool click %d; sleep .15'
    click_1 = click % 1

class Pages:
    page_0, page_1, page_2, page_3, page_4,\
            page_5, page_6 = range(7)

class Skill:
    # Abilities
    left = (530, 224)
    # 3 skills
    ability_3_0 = (800, 224)
    ability_3_1 = (960, 224)
    ability_3_2 = (1120, 224)
    # 4 skills
    ability_4_0 = (720, 224)
    ability_4_1 = (880, 224)
    ability_4_2 = (1040, 224)
    ability_4_3 = (1200, 224)
    right = (1400, 224)
    # Runes
    rune_0 = (560, 480)
    rune_1 = (720, 480)
    rune_2 = (880, 480)
    rune_3 = (1040, 480)
    rune_4 = (1200, 480)
    rune_5 = (1360, 480)
    # Passives
    # Row 0
    passive_0_0 = (528, 466)
    passive_0_1 = (766, 466)
    passive_0_2 = (1008, 466)
    passive_0_3 = (1250, 466)
    # Row 1
    passive_1_0 = (528, 580)
    passive_1_1 = (766, 580)
    passive_1_2 = (1008, 580)
    passive_1_3 = (1250, 580)
    # Row 2
    passive_2_0 = (528, 700)
    passive_2_1 = (766, 700)
    passive_2_2 = (1008, 700)
    passive_2_3 = (1250, 700)
    # Row 3-3
    passive_3_3_0 = (645, 810)
    passive_3_3_1 = (890, 810)
    passive_3_3_2 = (1130, 810)
    # Row 3-4
    passive_3_4_0 = (528, 810)
    passive_3_4_1 = (766, 810)
    passive_3_4_2 = (1008, 810)
    passive_3_4_3 = (1250, 810)
    # Confirmation
    accept = (840, 910)
    cancel = (1080, 910)

class Skills:
    # Mouse
    mouse_0 = (765, 230)
    mouse_1 = (1180, 230)
    # Key
    key_0 = (765, 420)
    key_1 = (1180, 420)
    key_2 = (765, 580)
    key_3 = (1180, 580)
    # Passives
    passive_0 = (764, 764)
    passive_1 = (960, 764)
    passive_2 = (1154, 764)
    active = ( mouse_0, mouse_1, key_0, key_1, key_2, key_3 )
    passive = ( passive_0, passive_1, passive_2 )
    skills = active + passive

VALID_SLOTS = (
    'mouse_0', 'mouse_1',
    'key_0', 'key_1', 'key_2', 'key_3',
    'passive_0', 'passive_1', 'passive_2',
)
SLOT_ASSOC = dict(zip(VALID_SLOTS, Skills.skills))
SPARE_PASSIVES = ( Skill.passive_0_0, Skill.passive_0_1,
        Skill.passive_0_2, Skill.passive_0_3, Skill.passive_1_0,
        Skill.passive_1_1, Skill.passive_1_2, Skill.passive_1_3,
        Skill.passive_2_0, Skill.passive_2_1, Skill.passive_2_2,
        Skill.passive_2_3 )

