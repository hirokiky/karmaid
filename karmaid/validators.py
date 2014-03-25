def validate_resource(resource):
    if not isinstance(resource, str):
        return False
    return 1 <= len(resource) < 5000
