import re

RESOURCE_REGEXP = re.compile('^[!-~]{1,5000}$', re.IGNORECASE)


def validate_resource(resource):
    try:
        return bool(RESOURCE_REGEXP.match(resource))
    except TypeError:
        return False
