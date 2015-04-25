#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 xmonster.cn. All rights reserved.
#

from tornado import template

model_list = [
    {
        'field': 'f_id',
        'element': 'text',
        'placeholder': 'ID',
        'required': True,
    }, {
        'field': 'f_name',
        'element': 'text',
        'placeholder': u'商品名称',
        'required': True,
    }, {
        'field': 'f_is_show',
        'element': 'radio',
        'placeholder': u'类型',
        'type': 'int',
        'value_array': [1, 2, 3],
        'desc_array': [u'收费', u'免费', u'优惠活动'],
        'default': 2,
    }, {
        'field': 'f_supplier',
        'element': 'select',
        'placeholder': u'供应商',
        'type': 'str',
        'value_array': ['gewala', 'self', 'manlv'],
        'desc_array': [u'格瓦拉', u'自营', u'漫旅'],
        'default': 'self',
    }, {
        'field': 'f_week',
        'element': 'checkbox',
        'placeholder': u'星期',
        'value_array': [1, 2, 3, 4, 5, 6, 7],
        'desc_array': [u'一', u'二', u'三', u'四', u'五', u'六', u'日'],
        'default': [2, 4],
    }, {
        'field': 'f_tiny_type',
        'element': 'checkbox',
        'placeholder': u'小类型',
        'value_array': ['1', '2', '3', '4', '5', '6', '7'],
        'desc_array': [u'一', u'二', u'三', u'四', u'五', u'六', u'日'],
        'default': ['2', '4'],
    }
]


def generate_view(arg_model_list):
    loader = template.Loader("templates")
    view_template = loader.load("form_new.htm")
    print view_template.generate(
        model_list=arg_model_list,
        escape=None,
    )
    view_template = loader.load("form_edit.htm")
    print view_template.generate(
        model_list=arg_model_list,
        model_name='project',
        prev="{{",
        next="}}",
        escape=None,
    )


if __name__ == '__main__':
    generate_view(model_list)
