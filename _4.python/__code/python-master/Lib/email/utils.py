import os
import re
import time
import random
import socket
import datetime
import urllib.parse

from email._parseaddr import quote
from email._parseaddr import AddressList as _AddressList
from email._parseaddr import mktime_tz

from email._parseaddr import parsedate, parsedate_tz, _parsedate_tz

# Intrapackage imports
from email.charset import Charset

COMMASPACE = ', '
EMPTYSTRING = ''
UEMPTYSTRING = ''
CRLF = '\r\n'
TICK = "'"

specialsre = re.compile(r'[][\\()<>@,:;".]')
escapesre = re.compile(r'[\\"]')


ecre = re.compile(r'''
  =\?                   # literal =?
  (?P<charset>[^?]*?)   # non-greedy up to the next ? is the charset
  \?                    # literal ?
  (?P<encoding>[qb])    # either a "q" or a "b", case insensitive
  \?                    # literal ?
  (?P<atom>.*?)         # non-greedy up to the next ?= is the atom
  \?=                   # literal ?=
  ''', re.VERBOSE | re.IGNORECASE)


def _format_timetuple_and_zone(timetuple, zone):
    return '%s, %02d %s %04d %02d:%02d:%02d %s' % (
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][timetuple[6]],
        timetuple[2],
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][timetuple[1] - 1],
        timetuple[0], timetuple[3], timetuple[4], timetuple[5],
        zone)

def formatdate(timeval=None, localtime=False, usegmt=False):
    # Note: we cannot use strftime() because that honors the locale and RFC
    # 2822 requires that day and month names be the English abbreviations.
    if timeval is None:
        timeval = time.time()
    if localtime:
        now = time.localtime(timeval)
        # Calculate timezone offset, based on whether the local zone has
        # daylight savings time, and whether DST is in effect.
        if time.daylight and now[-1]:
            offset = time.altzone
        else:
            offset = time.timezone
        hours, minutes = divmod(abs(offset), 3600)
        # Remember offset is in seconds west of UTC, but the timezone is in
        # minutes east of UTC, so the signs differ.
        if offset > 0:
            sign = '-'
        else:
            sign = '+'
        zone = '%s%02d%02d' % (sign, hours, minutes // 60)
    else:
        now = time.gmtime(timeval)
        # Timezone offset is always -0000
        if usegmt:
            zone = 'GMT'
        else:
            zone = '-0000'
    return _format_timetuple_and_zone(now, zone)

def format_datetime(dt, usegmt=False):
    """Turn a datetime into a date string as specified in RFC 2822.

    If usegmt is True, dt must be an aware datetime with an offset of zero.  In
    this case 'GMT' will be rendered instead of the normal +0000 required by
    RFC2822.  This is to support HTTP headers involving date stamps.
    """
    now = dt.timetuple()
    if usegmt:
        if dt.tzinfo is None or dt.tzinfo != datetime.timezone.utc:
            raise ValueError("usegmt option requires a UTC datetime")
        zone = 'GMT'
    elif dt.tzinfo is None:
        zone = '-0000'
    else:
        zone = dt.strftime("%z")
    return _format_timetuple_and_zone(now, zone)


def make_msgid(idstring=None, domain=None):
    """Returns a string suitable for RFC 2822 compliant Message-ID, e.g:

    <20020201195627.33539.96671@nightshade.la.mastaler.com>

    Optional idstring if given is a string used to strengthen the
    uniqueness of the message id.  Optional domain if given provides the
    portion of the message id after the '@'.  It defaults to the locally
    defined hostname.
    """
    timeval = time.time()
    utcdate = time.strftime('%Y%m%d%H%M%S', time.gmtime(timeval))
    pid = os.getpid()
    randint = random.randrange(100000)
    if idstring is None:
        idstring = ''
    else:
        idstring = '.' + idstring
    if domain is None:
        domain = socket.getfqdn()
    msgid = '<%s.%s.%s%s@%s>' % (utcdate, pid, randint, idstring, domain)
    return msgid


def parsedate_to_datetime(data):
    *dtuple, tz = _parsedate_tz(data)
    if tz is None:
        return datetime.datetime(*dtuple[:6])
    return datetime.datetime(*dtuple[:6],
            tzinfo=datetime.timezone(datetime.timedelta(seconds=tz)))


def parseaddr(addr):
    addrs = _AddressList(addr).addresslist
    if not addrs:
        return '', ''
    return addrs[0]


# rfc822.unquote() doesn't properly de-backslash-ify in Python pre-2.3.
def unquote(str):
    """Remove quotes from a string."""
    if len(str) > 1:
        if str.startswith('"') and str.endswith('"'):
            return str[1:-1].replace('\\\\', '\\').replace('\\"', '"')
        if str.startswith('<') and str.endswith('>'):
            return str[1:-1]
    return str



# RFC2231-related functions - parameter encoding and decoding
def decode_rfc2231(s):
    """Decode string according to RFC 2231"""
    parts = s.split(TICK, 2)
    if len(parts) <= 2:
        return None, None, s
    return parts


def encode_rfc2231(s, charset=None, language=None):
    """Encode string according to RFC 2231.

    If neither charset nor language is given, then s is returned as-is.  If
    charset is given but not language, the string is encoded using the empty
    string for language.
    """
    s = urllib.parse.quote(s, safe='', encoding=charset or 'ascii')
    if charset is None and language is None:
        return s
    if language is None:
        language = ''
    return "%s'%s'%s" % (charset, language, s)


rfc2231_continuation = re.compile(r'^(?P<name>\w+)\*((?P<num>[0-9]+)\*?)?$',
    re.ASCII)

def decode_params(params):
    """Decode parameters list according to RFC 2231.

    params is a sequence of 2-tuples containing (param name, string value).
    """
    # Copy params so we don't mess with the original
    params = params[:]
    new_params = []
    # Map parameter's name to a list of continuations.  The values are a
    # 3-tuple of the continuation number, the string value, and a flag
    # specifying whether a particular segment is %-encoded.
    rfc2231_params = {}
    name, value = params.pop(0)
    new_params.append((name, value))
    while params:
        name, value = params.pop(0)
        if name.endswith('*'):
            encoded = True
        else:
            encoded = False
        value = unquote(value)
        mo = rfc2231_continuation.match(name)
        if mo:
            name, num = mo.group('name', 'num')
            if num is not None:
                num = int(num)
            rfc2231_params.setdefault(name, []).append((num, value, encoded))
        else:
            new_params.append((name, '"%s"' % quote(value)))
    if rfc2231_params:
        for name, continuations in rfc2231_params.items():
            value = []
            extended = False
            # Sort by number
            continuations.sort()
            # And now append all values in numerical order, converting
            # %-encodings for the encoded segments.  If any of the
            # continuation names ends in a *, then the entire string, after
            # decoding segments and concatenating, must have the charset and
            # language specifiers at the beginning of the string.
            for num, s, encoded in continuations:
                if encoded:
                    # Decode as "latin-1", so the characters in s directly
                    # represent the percent-encoded octet values.
                    # collapse_rfc2231_value treats this as an octet sequence.
                    s = urllib.parse.unquote(s, encoding="latin-1")
                    extended = True
                value.append(s)
            value = quote(EMPTYSTRING.join(value))
            if extended:
                charset, language, value = decode_rfc2231(value)
                new_params.append((name, (charset, language, '"%s"' % value)))
            else:
                new_params.append((name, '"%s"' % value))
    return new_params

def collapse_rfc2231_value(value, errors='replace',
                           fallback_charset='us-ascii'):
    if not isinstance(value, tuple) or len(value) != 3:
        return unquote(value)
    # While value comes to us as a unicode string, we need it to be a bytes
    # object.  We do not want bytes() normal utf-8 decoder, we want a straight
    # interpretation of the string as character bytes.
    charset, language, text = value
    if charset is None:
        # Issue 17369: if charset/lang is None, decode_rfc2231 couldn't parse
        # the value, so use the fallback_charset.
        charset = fallback_charset
    rawbytes = bytes(text, 'raw-unicode-escape')
    try:
        return str(rawbytes, charset, errors)
    except LookupError:
        # charset is not a known codec.
        return unquote(text)


#
# datetime doesn't provide a localtime function yet, so provide one.  Code
# adapted from the patch in issue 9527.  This may not be perfect, but it is
# better than not having it.
#

def localtime(dt=None, isdst=-1):
    if dt is None:
        return datetime.datetime.now(datetime.timezone.utc).astimezone()
    if dt.tzinfo is not None:
        return dt.astimezone()
    # We have a naive datetime.  Convert to a (localtime) timetuple and pass to
    # system mktime together with the isdst hint.  System mktime will return
    # seconds since epoch.
    tm = dt.timetuple()[:-1] + (isdst,)
    seconds = time.mktime(tm)
    localtm = time.localtime(seconds)
    try:
        delta = datetime.timedelta(seconds=localtm.tm_gmtoff)
        tz = datetime.timezone(delta, localtm.tm_zone)
    except AttributeError:
        # Compute UTC offset and compare with the value implied by tm_isdst.
        # If the values match, use the zone name implied by tm_isdst.
        delta = dt - datetime.datetime(*time.gmtime(seconds)[:6])
        dst = time.daylight and localtm.tm_isdst > 0
        gmtoff = -(time.altzone if dst else time.timezone)
        if delta == datetime.timedelta(seconds=gmtoff):
            tz = datetime.timezone(delta, time.tzname[dst])
        else:
            tz = datetime.timezone(delta)
    return dt.replace(tzinfo=tz)


ccc = formatdate(timeval=None, localtime=False, usegmt=False)
print(ccc)

timeval = time.time()
print(timeval)
now = time.localtime(timeval)
print(type(now))
print(now)

ccc = datetime.datetime.now(datetime.timezone.utc).astimezone()
print(ccc)

    



'''
dt = datet
def format_datetime(dt, usegmt=False):
'''



    

