import json

from rest_framework.renderers import JSONRenderer


class ConduitJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(ConduitJSONRenderer, self).render(data)

        return json.dumps({
            self.object_label: data
        })
