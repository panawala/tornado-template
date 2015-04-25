#!/usr/bin/python
# -*- coding: utf-8 -*-
#
from tpl_engine import generate_model_view_handler

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
        'field': 'f_fee_type',
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
        'field': 'f_fee_type1',
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
    }, {
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


if __name__ == '__main__':
    generate_model_view_handler('topic', model_list, output_dir='build')
