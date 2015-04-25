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
        'placeholder': 'ID',
        'required': True,
        'type': 'int'
    }, {
        'field': 'f_name',
        'element': 'text',
        'placeholder': u'商品名称',
        'required': True,
        'type': 'str'
    }, {
        'field': 'f_is_show',
        'element': 'radio',
        'placeholder': u'类型',
        'type': 'int',
        'value_array': [1, 2, 3],
        'desc_array': [u'收费', u'免费', u'优惠活动'],
        'required': False,
        'default': 2,
    }, {
        'field': 'f_supplier',
        'element': 'select',
        'placeholder': u'供应商',
        'type': 'str',
        'value_array': ['gewala', 'self', 'manlv'],
        'desc_array': [u'格瓦拉', u'自营', u'漫旅'],
        'required': False,
        'default': 'self',
    }, {
        'field': 'f_week',
        'element': 'checkbox',
        'placeholder': u'星期',
        'value_array': [1, 2, 3, 4, 5, 6, 7],
        'desc_array': [u'一', u'二', u'三', u'四', u'五', u'六', u'日'],
        'default': [2, 4],
        'required': False,
        'type': 'int'
    }, {
        'field': 'f_tiny_type',
        'element': 'checkbox',
        'placeholder': u'小类型',
        'value_array': ['1', '2', '3', '4', '5', '6', '7'],
        'desc_array': [u'一', u'二', u'三', u'四', u'五', u'六', u'日'],
        'default': ['2', '4'],
        'required': False,
        'type': 'str'
    }
]


def generate_view(arg_model_list):
    loader = template.Loader("templates")

    build_path = "build"
    build_path_exists = os.path.exists(build_path)
    print(build_path_exists)
    if not build_path_exists:
        os.mkdir(build_path)

    input_file_name = "form_new.htm"
    view_template = loader.load(input_file_name)
    template_result = view_template.generate(
        model_list=arg_model_list,
        model_name='project',
        escape=None,
    )
    output_file = open('/'.join([build_path, input_file_name + 'l']), 'w+')
    output_file.write(template_result)
    output_file.close()

    input_file_name = "form_edit.htm"
    view_template = loader.load(input_file_name)
    template_result = view_template.generate(
        model_list=arg_model_list,
        model_name='project',
        prev="{{",
        next="}}",
        escape=None,
    )

    output_file = open('/'.join([build_path, input_file_name + 'l']), 'w+')
    output_file.write(template_result)
    output_file.close()


    input_file_name = "handler.p"
    view_template = loader.load(input_file_name)
    template_result = view_template.generate(
        model_list=arg_model_list,
        model_name='project',
        model_name_upper='Project',
        prev="{{",
        next="}}",
        escape=None,
    )

    output_file = open('/'.join([build_path, input_file_name + 'y']), 'w+')
    output_file.write(template_result)
    output_file.close()

    input_file_name = "model.p"
    view_template = loader.load(input_file_name)
    template_result = view_template.generate(
        model_list=arg_model_list,
        model_name='project',
        model_name_upper='Project',
        prev="{{",
        next="}}",
        escape=None,
    )

    output_file = open('/'.join([build_path, input_file_name + 'y']), 'w+')
    output_file.write(template_result)
    output_file.close()

    input_file_name = "entries.htm"
    view_template = loader.load(input_file_name)
    template_result = view_template.generate(
        model_list=arg_model_list,
        model_name='project',
        model_name_upper='Project',
        prev="{{",
        next="}}",
        prev_per="{%",
        next_per="%}",
        escape=None,
    )

    output_file = open('/'.join([build_path, input_file_name + 'l']), 'w+')
    output_file.write(template_result)
    output_file.close()

if __name__ == '__main__':
    generate_view(model_list)
