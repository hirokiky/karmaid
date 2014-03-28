from karmaid.stuffs import STUFF_REGEXP


def validate_stuff(stuff):
    try:
        return bool(STUFF_REGEXP.match(stuff))
    except TypeError:
        return False
