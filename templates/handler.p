{% autoescape None %}
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 xmonster.cn. All rights reserved.
#

import logging
import time

import tornado.web
import tornado.auth
from tornado import escape
from handlers.base.admin_handler import ViewHandler, InnerAPIHandler

from libs.exceptions import APIError
from libs.uploader import upload
from libs.validator import validate
from libs.util import json_dumps


class {{model_name_upper}}ViewHandler(ViewHandler):
    def get_{{model_name}}_from_arguments(self):
        fields = [
        {% for model in model_list %}    {
                'name': '{{model['field'][2:]}}',
                'type': '{{model['type']}}',
                'required': {{True if model['required'] else False}},
                {% if not model['required'] %}'default': {{"'" + str(model['default']) + "'" if model['type'] == 'str' and model['element'] != 'checkbox' else model['default']}},{% end %}
            },{% end %}
        ]


        ret, params = validate(self.request.arguments, fields)
        logging.info(ret)
        logging.info(params)
        if not ret:
            raise APIError(400, params)

        return ret, params, {
        {% for model in model_list %}
            "{{model['field']}}": params['{{model['field'][2:]}}'],
        {% end %}
        }


class {{model_name_upper}}NewHandler({{model_name_upper}}ViewHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('{{model_name}}_new.html', menu='{{model_name}}s')

    @tornado.web.authenticated
    def post(self):
        ret, {{model_name}} = self.get_{{model_name}}_from_arguments()
        {{model_name}}["f_create_time"] = time.strftime('%Y-%m-%d %X', time.localtime())
        self.{{model_name}}_model.upsert_{{model_name}}({{model_name}}, {{model_name}}['id'])
        self.redirect("/{{model_name}}s")
        return


class {{model_name_upper}}EditHandler({{model_name_upper}}ViewHandler):
    @tornado.web.authenticated
    def get(self, {{model_name}}_id):
        ret, {{model_name}} = self.{{model_name}}_model.get_{{model_name}}({{model_name}}_id)
        if not ret:
            raise APIError(404, {{model_name}})
        self.render('{{model_name}}_edit.html', {{model_name}}={{model_name}}, menu='{{model_name}}s')

    @tornado.web.authenticated
    def post(self):
        ret, {{model_name}} = self.get_{{model_name}}_from_arguments()
        self.{{model_name}}_model.upsert_{{model_name}}({{model_name}}, {{model_name}}['id'])
        self.redirect("/{{model_name}}s")
        return


class {{model_name_upper}}sHandler(ViewHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("{{model_name}}_entries.html", menu='{{model_name}}s')


class Inner{{model_name_upper}}sHandler(InnerAPIHandler):
    @tornado.web.authenticated
    def get(self):
        page = int(self.get_argument('page', '1'))
        num = int(self.get_argument('pagesize', '20'))
        search_str = self.get_argument('search_str', '')
        {{model_name}}s = self.{{model_name}}_model.search_{{model_name}}(search_str, num=num, current_page=page)
        self.finish({{model_name}}s)

    @tornado.web.authenticated
    def delete(self):
        {{model_name}}_id = self.get_argument("id")
        {{model_name}}_id = self.{{model_name}}_model.remove_{{model_name}}({{model_name}}_id)
        result = {'ret': '0', 'msg': '', 'data': {'result': {{model_name}}_id}}
        self.finish(result)

