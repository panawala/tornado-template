#!/usr/bin/python
# -*- coding: utf-8 -*-
#


from libs.query import Query


class {{model_name_upper}}Model(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "t_{{model_name}}"
        super({{model_name_upper}}Model, self).__init__()

    def search_{{model_name}}(self, search_str, num=20, current_page=0):
        where = "t_{{model_name}}.f_name LIKE '%%%s%%'" % (search_str)
        field = 't_{{model_name}}.*'
        order = 'f_create_time DESC'
        return self.where(where).order(order).field(field).pages(current_page=current_page, list_rows=num)

    def get_{{model_name}}(self, {{model_name}}_id):
        where = "f_id = %s" % {{model_name}}_id
        {{model_name}}s_rows = self.where(where).select()
        if not {{model_name}}s_rows:
            return False, 'no {{model_name}}s found'
        else:
            return True, {{model_name}}s_rows[0]

    def update_{{model_name}}(self, {{model_name}}, {{model_name}}_id):
        where = 'f_id = %s' % {{model_name}}_id
        return self.where(where).data({{model_name}}).save()

    def add_{{model_name}}(self, {{model_name}}):
        return self.data({{model_name}}).add()

    def upsert_{{model_name}}(self, {{model_name}}, {{model_name}}_id):
        where = "f_id = %s" % {{model_name}}_id
        {{model_name}}_rows = self.where(where).select()
        if not {{model_name}}_rows:
            self.add_{{model_name}}({{model_name}})
        else:
            self.update_{{model_name}}({{model_name}}, {{model_name}}_id)

    def remove_{{model_name}}(self, {{model_name}}_id):
        where = "f_id = %s" % {{model_name}}_id
        ret = self.where(where).delete()
        if ret:
            return False, 'remove {{model_name}} failed: %s ' % {{model_name}}_id
        return True, 'ok'