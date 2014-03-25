from pyramid.httpexceptions import HTTPBadRequest

from karmaid.validators import validate_resource


class KarmaResource(object):
    def __init__(self, request):
        self.request = request

    @property
    def resource(self):
        resource = self.request.params.get('resource')
        if not validate_resource(resource):
            raise HTTPBadRequest
        return resource
