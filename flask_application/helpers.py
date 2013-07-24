import datetime
import math
from flask import abort 
from functools import wraps


# Caching
def cached(app, timeout=5 * 60, key='view/%s'):
    '''http://flask.pocoo.org/docs/patterns/viewdecorators/#caching-decorator'''
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key % request.path
            rv = app.cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            app.cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator


# Custom Template Filters
def datetimeformat(value):
    delta = datetime.datetime.now() - value
    if delta.days == 0:
        formatting = 'today'
    elif delta.days < 10:
        formatting = '{0} days ago'.format(delta.days)
    elif delta.days < 28:
        formatting = '{0} weeks ago'.format(int(math.ceil(delta.days/7.0)))
    elif value.year == datetime.datetime.now().year:
        formatting = 'on %d %b'
    else:
        formatting = 'on %d %b %Y'
    return value.strftime(formatting)

keyspace = "wf59eorpma2vnxb07kiqt83_u6lgzs41-ycdjh"

def int_str(val):
    """ Turn a positive integer into a string. """
    assert val >= 0
    out = ""
    while val > 0:
        val, digit = divmod(val, len(keyspace))
        out += keyspace[digit]
    return out[::-1]

def str_int(val):
    """ Turn a string into a positive integer. """
    out = 0
    for c in val:
        out = out * len(keyspace) + keyspace.index(c)
    return out

def chaffify(val, chaff_val = 25978):
    """ Add chaff to the given positive integer. """
    return val * chaff_val

def dechaffify(chaffy_val, chaff_val = 25978):
    """ Dechaffs the given chaffed value. If the value does not seem to be correctly chaffed, raises a ValueError. """
    val, chaff = divmod(chaffy_val, chaff_val)
    if chaff != 0:
        raise ValueError("Invalid chaff in value")
    return val

def get_or_abort(model, object_id, code=404):
        """
        get an object with his given id or an abort error (404 is the default)
        """
        result = model.query.get(object_id)
        return result or abort(code)

def encode_id(val):
    """
     Encodes ID into semi random set of strings
    """
    return int_str(chaffify(val))

def decode_id(val):
    return dechaffify(str_int(val))


