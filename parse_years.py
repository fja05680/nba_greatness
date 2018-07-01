# -*- encoding: utf-8 -*-

import re

def force_to_unicode(text):
    "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding"
    return text if isinstance(text, unicode) else text.decode('utf8')

#1956–1969
#1984–1993, 1995–1998, 2001–2003
#1979–1991, 1996
#1995–present

str = '1984–1993, 1995–1998, 2001–2003'
print(str[:4], str[-4:])
