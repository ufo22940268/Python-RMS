# -*- coding: utf-8 -*-

import os
from rms import deploy
import copy

# Running on local machine. Let's just use the local mongod instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'rms'

DEBUG = True

AUTH_FIELD = "user_id"
DATE_FORMAT = "%Y-%m-%d %H:%M"

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

operator = {
        'schema': {
            #工号
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

            #联系人
            'contact': {
                'type': 'string',
                },

            #电话
            'tel': {
                'type': 'string',
                },

            #部门
            'department': {
                'type': 'string',
                },

            #职位
            'job': {
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

            'enabled': {
                    'type': 'string',
                    'default': '1',
                    },
            # 0     0      0     0
        #view add delete check
        #
        #For example:
        #  0100 only has add permission
        
        #入库
        'import_permission': {
                'type': 'string',
                'default': '1111',
                },

        #出库
        'export_permission': {
                'type': 'string',
                'default': '1111',
                },
        
        #库存结存
        'query_permission': {
                'type': 'string',
                'default': '1',
                },
        

        #产品信息管理
        'product_permission': {
                'type': 'string',
                'default': '1111',
                },

        #供应商信息管理
        'provider_permission': {
                'type': 'string',
                'default': '1111',
                },

        #操作员信息管理
        'operator_permission': {
                'type': 'string',
                'default': '1111',
                },

        #客户管理
        'customer_permission': {
                'type': 'string',
                'default': '1111',
                },

        #销售订单
        'order_permission': {
                'type': 'string',
                'default': '1111',
                },

        #销售开单
        'open_order_permission': {
                'type': 'string',
                'default': '1111',
                },

        #录音
        'recorder_permission': {
                'type': 'string',
                'default': '11',
                },

        #ip电话
        'ip_tel_permission': {
                'type': 'string',
                'default': '11',
                },

        #ip电话联系人管理
        'contact_permission': {
                'type': 'string',
                'default': '1111',
                },

        #视频监控
        'video_permission': {
                'type': 'string',
                'default': '1',
                },

        #视频监控
        'verify_permission': {
                'type': 'string',
                'default': '111',
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

contact_schema = {
        #编码
        'snum': {
            'type': 'string',
            'unique': True,
            },

        #联系人
        'name': {
            'type': 'string',
            },

        #公司名称
        'company': {
            'type': 'string',
            'required': 'true',
            },

        #联系电话
        'tel': {
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

        'contact_type': {
            'type': 'string',
            },

        #邮编
        'postcode': {
            'type': 'string',
            },

        'email': {
            'type': 'string',
            },

        'qq': {
            'type': 'string',
            },

        'kaihuhang_name': {
            'type': 'string',
            },

        'kaihuhang_account': {
            'type': 'string',
            },

        'category': {
                'type': 'string',
                },

        #备注
    'comment': {
            'type': 'string',
            },

    #0 for provider, 1 for customer, 2 for person
    'type': {
            'type': 'integer',
            'allowed': [1, 2, 3],
            }
}

contact = {'schema': contact_schema}

customer = {
        'datasource': {
                'source': 'contact',
                'filter': {'type': 1}
                }
        }
customer['schema'] = copy.deepcopy(contact_schema)
customer['schema']['type']['default'] = 1

person = {
        'datasource': {
                'source': 'contact',
                'filter': {'type': 2}
                }
        }
person['schema'] = copy.deepcopy(contact_schema)
person['schema']['type']['default'] = 2

provider = {
        'datasource': {
                'source': 'contact',
                'filter': {'type': 3}
                }
        }

provider['schema'] = copy.deepcopy(contact_schema)
provider['schema']['type']['default'] = 3

product = {
        'schema': {

            #产品编码
            'snum': {
                'type': 'string',
                'required': 'true',
                'unique': 'true',
                },

            #产品名称
            'name': {
                'type': 'string',
                },

            #产品规格
            'specification': {
                'type': 'string',
                },

            #插入时间
            'time':{
                'type': 'datetime',
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

record = {
        'schema': {

            'ID': {
                'type': 'string',
                },

            'CompID': {
                'type': 'string',
                },

            'RecDate': {
                'type': 'string',
                },

            'RecTime': {
                'type': 'string',
                },

            'RecLen': {
                'type': 'string',
                },

            'DialNum': {
                'type': 'string',
                },

            'CallerId': {
                'type': 'string',
                },

            'RingNum': {
                'type': 'string',
                },

            'RecTxt': {
                'type': 'string',
                },

            'NameNo': {
                'type': 'string',
                },

            'ENDID': {
                'type': 'string',
                },

            'RecFileName': {
                'type': 'string',
                },

            'QuestionID': {
                'type': 'string',
                },

            'BakFlag': {
                'type': 'string',
                },

            'YSFlag': {
                'type': 'string',
                },

            'UserBuf': {
                'type': 'string',
                },

            'UserFlag': {
                'type': 'string',
                },
        }
}

order_schema = {
        #订单号
        'snum': {
            'type': 'string',
            'required': 'true',
            'unique': 'true',
            },

        #客户名称
        'customer_name': {
            'type': 'string',
            },

        #联系人
        'contact': {
            'type': 'string',
            },

        #产品名称
        'product_name': {
            'type': 'string',
            },


        #快递公司
        'deliver': {
            'type': 'string',
            },

        #发货时间
        'deliver_time': {
            'type': 'string',
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

        #单位
        'unit_price': {
            'type': 'string',
            },

        #数量
        'quantity': {
            'type': 'string',
            },

        #总价
        'total_price': {
            'type': 'string',
            },

        #订单状态
            #"wait_for_buyer" 等待买家付款
            #"buyer_paid" 买家已付款
            #"seller_delivered" 卖家已发货
            #"repo_delivered" 仓库已发货
            #"refund" 已退款
            #"buyer_returned" 卖家已退货

        'status': {
                'type': 'string',
                'default': 'default',
                'allowed': ['default', "wait_for_buyer", "buyer_paid", "seller_delivered", "refund", "buyer_returned", "repo_delivered"],
                },

        #送货地址
        'address': {
                'type': 'string',
                },

        #备注u
        'comment': {
                'type': 'string',
                },

        'type': {
                'type': 'integer',
                'allowed': [1, 2],
                },
        #审核
        'validated': {
                'type': 'string',
                'default': '0',
                'allowed': ['0', '1'],
                }
        }

order = {
        'datasource': {
                'source': 'order',
                }
        }

order['schema'] = copy.deepcopy(order_schema)

open_order = {
        'datasource': {
                'source': 'open_order',
                }
        }

open_order['schema'] = copy.deepcopy(order_schema)


imports = {
        'id_field': 'snum',
        'schema': {


            ##入库单号
            'snum':{
                'type': 'string',
                },

            #入库时间
            'time':{
                'type': 'datetime',
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
                },

        #审核
        'validated': {
                'type': 'string',
                'default': '0',
                'allowed': ['0', '1'],
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
                'type': 'datetime',
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
                },

        #审核
        'validated': {
                'type': 'string',
                'default': '0',
                'allowed': ['0', '1'],
                }
        },
}

test = {
        'schema': {
            #时间
            'date': {
                'type': 'datetime',
                },

            'num': {
                'type': 'integer',
                },

            'k': {
                'type': 'string',
                }
            }
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
        # 操作员
        'operator': operator,

        # 出货记录
        'export': export,

        # 入货记录
        'import': imports,

        'product': product,

        #联系人
        'contact': contact,

        #供应商
        'provider': provider,

        #客户
        'customer': customer,

        #普通联系人
        'person': person,

        #订单
        'order': order,

        #开单
        'open_order': open_order,

        #录音
        'record': record,

        #'account': account,
        'test': test
        }
