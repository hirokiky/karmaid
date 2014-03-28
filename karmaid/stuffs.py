import re

STUFF_REGEXP = re.compile('^[!-~]{1,5000}$', re.IGNORECASE)


class InvalidStuff(Exception):
    pass
