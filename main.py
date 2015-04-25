#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 xmonster.cn. All rights reserved.
#
import os

from tornado import template

model_list = [
    {
        'field': 'f_id',
        'element': 'id',
        'label': 'ID',
        'required': True,
        'type': 'int'
    }, {
        'field': 'f_address',
        'element': 'text',
        'label': u'地址',
        'required': True,
        'type': 'str'
    }, {
        'field': 'f_name',
        'element': 'text',
        'label': u'商品名称',
        'required': True,
        'type': 'str'
    }, {
        'field': 'f_is_show',
        'element': 'radio',
        'label': u'类型',
        'type': 'int',
        'option_array': [
            {'val': 1, 'desc': u'收费'},
            {'val': 2, 'desc': u'免费'},
            {'val': 3, 'desc': u'优惠活动'},
        ],
        'required': False,
        'default': 2,
    }, {
        'field': 'f_is_show1',
        'element': 'radio',
        'label': u'类型1',
        'type': 'str',
        'option_array': [
            {'val': '1', 'desc': u'收费1'},
            {'val': '2', 'desc': u'免费1'},
            {'val': '3', 'desc': u'优惠活动1'},
        ],
        'required': False,
        'default': '2',
    }, {
        'field': 'f_supplier',
        'element': 'select',
        'label': u'供应商',
        'type': 'str',
        'option_array': [
            {'val': 'gewala', 'desc': u'格瓦拉'},
            {'val': 'self', 'desc': u'自营'},
            {'val': 'manlv', 'desc': u'漫旅'},
        ],
        'required': False,
        'default': 'self',
    },{
        'field': 'f_supplier1',
        'element': 'select',
        'label': u'供应商1',
        'type': 'int',
        'option_array': [
            {'val': 1, 'desc': u'格瓦拉1'},
            {'val': 2, 'desc': u'自营1'},
            {'val': 3, 'desc': u'漫旅1'},
        ],
        'required': False,
        'default': 3,
    }, {
        'field': 'f_week',
        'element': 'checkbox',
        'label': u'星期',
        'type': 'int',
        'option_array': [
            {'val': 1, 'desc': u'一'},
            {'val': 2, 'desc': u'二'},
            {'val': 3, 'desc': u'三'},
            {'val': 4, 'desc': u'四'},
            {'val': 5, 'desc': u'五'},
            {'val': 6, 'desc': u'六'},
            {'val': 7, 'desc': u'日'},
        ],
        'default': [2, 4],
        'required': False,
    },
]


tpl_suffixes = {
    'html': ['.htm', 'l'],
    'handler': ['.p', 'y'],
    'model': ['.p', 'y'],
}


def __generate_template(tpl_file, arg_model_list, tpl_type="html"):
    loader = template.Loader("templates")
    build_path = "build"
    build_path_exists = os.path.exists(build_path)
    print(build_path_exists)
    if not build_path_exists:
        os.mkdir(build_path)

    input_tpl_file = tpl_file + tpl_suffixes[tpl_type][0]
    view_template = loader.load(input_tpl_file)
    template_result = view_template.generate(
        model_list=arg_model_list,
        model_name='topic',
        model_name_upper='Topic',
        prev="{{",
        next="}}",
        prev_per="{%",
        next_per="%}",
        escape=None,
    )

    output_file = open('/'.join([build_path, input_tpl_file + tpl_suffixes[tpl_type][1]]), 'w+')
    output_file.write(template_result)
    output_file.close()


def generate_view(arg_model_list):
    __generate_template('entries', arg_model_list, tpl_type='html')
    __generate_template('form_edit', arg_model_list, tpl_type='html')
    __generate_template('form_new', arg_model_list, tpl_type='html')
    __generate_template('handler', arg_model_list, tpl_type='handler')
    __generate_template('model', arg_model_list, tpl_type='model')

if __name__ == '__main__':
    generate_view(model_list)
