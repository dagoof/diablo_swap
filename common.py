import functools, collections

def apply_f(applied_f):
    def decorator(f):
        @functools.wraps(f)
        def _wrapped(*args, **kwargs):
            return applied_f(f(*args, **kwargs))
        return _wrapped
    return decorator

def compose(*fs):
    def _inner(*args, **kwargs):
        current = fs[-1](*args, **kwargs)
        rest = reversed(fs[:-1])
        for more in rest:
            current = more(current)
        return current
    if fs:
        return _inner
    raise ValueError('No functions provided')

class attrdict(dict):
    def __getattr__(self, key): return self.get(key)
    def __setattr__(self, key, value): self[key] = value

def Rattrdict(_dict):
    def _convert(element):
        if isinstance(element, collections.Mapping):
            if element:
                keys, values = zip(*element.items())
                return attrdict(zip(keys, map(_convert, values)))
            return attrdict()
        elif isinstance(element, collections.Sequence) and not\
                isinstance(element, basestring):
            return map(_convert, element)
        return element
    return _convert(_dict)
