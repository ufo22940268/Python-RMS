# -*- coding: utf-8 -*-

import os
from rms import deploy

# Running on local machine. Let's just use the local mongod instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'rms'

DEBUG = True

AUTH_FIELD = "user_id"

#if deploy.is_local():
    ## let's not forget the API entry point
    #SERVER_NAME = "127.0.0.1:5000"
#else:
    #SERVER_NAME = "192.241.196.189:5000"
SERVER_NAME = deploy.get_host() + ":5000"

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

provider = {
    'schema': {
        'name': {
            'type': 'string',
            'unique': True,
        },
        'postcode': {
            'type': 'string',
        },
        'tel': {
            'type': 'string',
        },
        'contact': {
            'type': 'string',
        },
        'mobile': {
            'type': 'string',
        },
        'fax': {
            'type': 'string',
        },
        'address': {
            'type': 'string',
        },
        'email': {
            'type': 'string',
        },
        'qq': {
            'type': 'string',
        },
        'py_kaihuhang': {
            'type': 'string',
        },
        'account': {
            'type': 'string',
        },
        'category': {
            'type': 'string',
        },
        'category': {
            'type': 'string',
        },
        'remark': {
            'type': 'string',
        },
    }
}

operator = {
    'schema': {
        'snum': {
            'type': 'string',
            'unique': True,
        },
        'name': {
            'type': 'string',
        },
        'password': {
            'type': 'string',
        },
        'contact': {
            'type': 'string',
        },
        'mobile': {
            'type': 'string',
        },
        'fax': {
            'type': 'string',
        },
        'address': {
            'type': 'string',
        },
        'email': {
            'type': 'string',
        },
        'qq': {
            'type': 'string',
        },
        'py_kaihuhang': {
            'type': 'string',
        },
        'account': {
            'type': 'string',
        },
        'category': {
            'type': 'string',
        },
        'category': {
            'type': 'string',
        },
        'remark': {
            'type': 'string',
        },

        'permission': {
            'type': 'list',
            'allowed': ['read', 'add', 'delete', 'validate']
        },

        # Foreign key to super user.
        'super_user_id': {
            'type': 'objectid',
            'data_relation': {
                'collection': 'super_user',
                'field': '_id',
                'embeddable': True
            },
        },
    }
}

product = {
    'schema': {

        #产品编码
        'snum': {
            'type': 'string',
            'required': 'true'
        },

        #产品名称
        'name': {
            'type': 'string',
        },

        #产品规格
        'specification': {
            'type': 'string',
        },

        #单位
        'provider': {
            'type': 'string',
        },

        #颜色
        'color': {
            'type': 'string',
        },

        #属性
        'property': {
            'type': 'string',
        },

        #备注
        'comment': {
            'type': 'string',
        },

        #库存下线
        'min': {
            'type': 'string',
        },

        #库存上限
        'max': {
            'type': 'string',
            'default': '0',
        },

        #库存数量
        'num': {
            'type': 'string',
            'default': '0',
        },
    }
}

account = {
    'schema': {
        'username':{
            'type': 'string',
            'required': True,
            #'unique': True,
        },
        'password':{
            'type': 'string',
            'required': True,
        },
    },
}

imports = {
    'id_field': 'snum',
    'schema': {


        ##入库单号
        'snum':{
            'type': 'string',
        },

        #入库时间
        'time':{
            'type': 'string',
        },

        #入库类型
        'type': {
            'type': 'string',
        },

        #供应单位
        'provider':{
            'type': 'string',
        },

        #采购人员
        'buyer':{
            'type': 'string',
        },

        #操作人员
        'operator':{
            'type': 'string',
        },

        #产品名称
        'product_name': {
            'type': 'string',
        },

        #产品编码
        'product_snum': {
            'type': 'string',
            'required': True,
            #'data_relation' : {
                #'collection' : 'product',
                #'field': 'snum',
            #}
        },

        #颜色
        'color': {
            'type': 'string',
        },

        #属性
        'property': {
            'type': 'string',
        },

        #备注
        'comment': {
            'type': 'string',
            'default': 'asdfa',
        },

        #数量
        'quantity': {
            'type': 'string',
            'default': '1',
        },

        #单位
        'unit': {
            'type': 'string',
        }
    }
}

export = {
    'schema': {

        #出库单号
        'snum':{
            'type': 'string',
            'required': True,
            'unique': True,
        },

        #备注
        'comment': {
            'type': 'string',
        },

        #产品名称
        'product_name': {
            'type': 'string',
        },

        #单位
        'unit': {
            'type': 'string',
        },

        #出库时间
        'time':{
            'type': 'string',
        },

        #出库类型
        'type': {
            'type': 'string',
        },
        
        #采购人员
        'buyer': {
            'type': 'string'
        },

        #采购单位
        'buy_company': {
            'type': 'string'
        },

        #操作人员
        'operator': {
            'type': 'string'
        },

        #产品编码
        'product_snum': {
            'type': 'string',
            'required': True,
            'data_relation' : {
                'collection' : 'product',
                'field': 'snum',
            }
        },

        #供应单位
        'provider':{
            'type': 'string',
        },

        #颜色
        #采用整数来进行表示
        'color': {
            'type': 'string'
        },

        #属性
        'property': {
            'type': 'string'
        },

        #备注
        'remark': {
            'type': 'string'
        },

        #数量
        'quantity': {
            'type': 'string',
            'default': '1',
        }
    },
}

# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.
people = {
    # 'title' tag used in item links.
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.
    'additional_lookup': {
        'url': '[\w]+',
        'field': 'lastname'
    },

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'lastname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
            # talk about hard constraints! For the purpose of the demo
            # 'lastname' is an API entry-point, so we need it to be unique.
            'unique': True,
        },
        # 'role' is a list, and can only contain values from 'allowed'.
        'role': {
            'type': 'list',
            'allowed': ["author", "contributor", "copy"],
        },
        # An embedded 'strongly-typed' dictionary.
        'location': {
            'type': 'dict',
            'schema': {
                'address': {'type': 'string'},
                'city': {'type': 'string'}
            },
        },
    }
}

works = {
    # if 'item_title' is not provided Eve will just strip the final
    # 's' from resource name, and use it as the item_title.
    #'item_title': 'work',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': {
        'title': {
            'type': 'string',
            'required': True,
        },
        'description': {
            'type': 'string',
        },
        'owner': {
            'type': 'objectid',
            'required': True,
            # referential integrity constraint: value must exist in the
            # 'people' collection. Since we aren't declaring a 'field' key,
            # will default to `people._id` (or, more precisely, to whatever
            # ID_FIELD value is).
            'data_relation': {
                'collection': 'people'
            }
        },
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    # 供应商
    'provider': provider,

    # 操作员
    'operator': operator,

    # 出货记录
    'export': export,

    # 入货记录
    'import': imports,

    'product': product,
    'account': account,
}

