
import re

def regex_strip(text, chars=None):
    if chars is None:
        return re.sub(r'^\s+|\s+$', '', text)
    else:
        return re.sub(
            r'^[' + re.escape(chars) + r']+|[' + re.escape(chars) + r']+$',
            '',
            text
        )


print(regex_strip("   Hello World   "))
print(regex_strip("xxxHello Worldxxx", "x"))


