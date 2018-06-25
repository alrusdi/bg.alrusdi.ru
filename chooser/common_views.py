# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.views import View


class JsonView(View):
    encoder_class = None

    def get_context_data(self, **kwargs):
        return kwargs

    def get(self, request, **kwargs):
        if self.encoder_class:
            data = json.dumps(self.get_context_data() or {}, cls=self.encoder_class)
        else:
            data = json.dumps(self.get_context_data() or {})
        resp = HttpResponse(data, content_type='application/json')
        resp['Expires'] = 'Mon, 1 Jan 2000 01:00:00 GMT'
        resp['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
        resp['Pragma'] = 'no-cache'
        return resp

    def post(self, request, **kwargs):
        self.json_post = {}
        try:
            self.json_post = json.loads(self.request.body.decode('utf-8'))
        except:
            pass
        return self.get(request, **kwargs)
