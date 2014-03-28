import re

STUFF_REGEXP = re.compile('^[!-~]{1,5000}$', re.IGNORECASE)


def validate_stuff(stuff):
    try:
        return bool(STUFF_REGEXP.match(stuff))
    except TypeError:
        return False
