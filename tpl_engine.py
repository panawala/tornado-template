#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import os

from tornado import template

_tpl_conf = {
    'new': ['.htm', 'l'],
    'edit': ['.htm', 'l'],
    'entries': ['.htm', 'l'],
    'view_handler': ['.p', 'y'],
    'model': ['.p', 'y'],
}


def __generate_template(model_name, arg_model_list, tpl_type, templates_dir="templates", output_dir="build"):
    loader = template.Loader(templates_dir)
    output_path_exists = os.path.exists(output_dir)
    print(output_path_exists)
    if not output_path_exists:
        os.mkdir(output_dir)

    input_tpl_file = tpl_type + _tpl_conf[tpl_type][0]
    view_template = loader.load(input_tpl_file)
    template_result = view_template.generate(
        model_list=arg_model_list,
        model_name=model_name,
        model_name_upper=model_name.capitalize(),
        prev="{{",
        next="}}",
        prev_per="{%",
        next_per="%}",
        escape=None,
    )

    output_file = open('/'.join([output_dir, model_name + '_' + input_tpl_file + _tpl_conf[tpl_type][1]]), 'w+')
    output_file.write(template_result)
    output_file.close()


def generate_model_view_handler(model_name, arg_model_list, templates_dir="templates", output_dir="build"):
    __generate_template(model_name, arg_model_list, tpl_type='entries', templates_dir=templates_dir, output_dir=output_dir)
    __generate_template(model_name, arg_model_list, tpl_type='edit', templates_dir=templates_dir, output_dir=output_dir)
    __generate_template(model_name, arg_model_list, tpl_type='new', templates_dir=templates_dir, output_dir=output_dir)
    __generate_template(model_name, arg_model_list, tpl_type='view_handler', templates_dir=templates_dir, output_dir=output_dir)
    __generate_template(model_name, arg_model_list, tpl_type='model', templates_dir=templates_dir, output_dir=output_dir)
