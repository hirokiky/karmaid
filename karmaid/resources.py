from pyramid.httpexceptions import HTTPBadRequest

from karmaid.validators import validate_stuff


class StuffResource(object):
    def __init__(self, request):
        self.request = request

    @property
    def stuff(self):
        stuff = self.request.params.get('stuff')
        if not validate_stuff(stuff):
            raise HTTPBadRequest
        return stuff
