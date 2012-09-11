import requests, json, collections, sys, operator

class adict(dict):
    def __getattr__(self, key):
        def _convert(element):
            if isinstance(element, collections.Mapping):
                return adict(element)
            elif isinstance(element, collections.Sequence) and not\
                    isinstance(element, basestring):
                return map(_convert, element)
            return element
        return _convert(self.get(key))
    def __setattr__(self, key, value): self[key] = value

def fix_slug(slug):
    return slug.replace('-', '_')

def fix_name(name):
    return '_'.join(name.lower().split())

def skills(source):
    slugs = map(operator.attrgetter('slug'), source.skills)
    slugs = map(fix_slug, slugs)
    categories = map(operator.attrgetter('categorySlug'), source.skills)
    categories = map(fix_slug, categories)
    return zip(slugs, categories)

def runes(source):
    return map(fix_name, map(operator.attrgetter('name'), source.runes))

classes = ('barbarian', 'witch-doctor', 'monk', 'demon-hunter', 'wizard')

if __name__ == '__main__':
    for c in sys.argv[1:] or classes:
        class_request = requests.get(
            'http://us.battle.net/d3/en/data/calculator/%s' % c)
        class_content = adict(json.loads(class_request.content))
        class_get = lambda label: map(operator.attrgetter(label),
            class_content.skills)
        class_abilities = [ ]

        for skill, pair in enumerate(skills(class_content)):
            slug, category = pair
            class_abilities.append(dict(
                skill = slug,
                category = category,
                runes = runes(class_content.skills[skill])))

        for skill in sorted(class_abilities, key = lambda x: x['category']):
            print '    # %s' % skill['skill']
            print '    \'%s\': (Barbarian._%s, Skill.rune_%s),' %\
                    (skill['skill'], skill['skill'], 0)
            for i, rune in enumerate(skill['runes']):
                print '    \'%s\': (Barbarian._%s, Skill.rune_%s),' %\
                        (rune, skill['skill'], i)
            print ''

