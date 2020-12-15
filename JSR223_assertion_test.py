#!python2
import sys
import os
import json


sys.path.append(r'C:\Users\hallo\AppData\Local\Programs\Python\Python27\Lib')
sys.path.append(r'C:\Users\hallo\AppData\Local\Programs\Python\Python27\Lib\site-packages')

from jsonschema import validate

true = True 
false = False 


responsedata = prev.getResponseDataAsString() #响应数据含有中文，python2返回的是<type 'unicode'>

josn_str = json.dumps(responsedata)  #json在调用dumps时会将中文转化为Unicode编码      <type 'unicode'> 

ojt = json.loads(josn_str).encode('utf-8') #  <type 'unicode'>


ojt = json.loads(ojt)  # <type 'dict'>



#发起表单定义接口响应，检测必须字段完整性、类型、object属性，内层elements数组只检测字段完整性，不校验数组嵌套的object属性
schema_array_noprop = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "object",
    "required": [
        "data",
        "result"
    ],
    "properties": {
        "data": {
            "type": "object",
            "required": [
                "definition",
                "schema"
            ],
            "properties": {
                "definition": {
                    "type": "object",
                    "required": [
                        "processform"
                    ],
                    "properties": {
                        "processform": {
                            "type": "object",
                            "required": [
                                "cc",
                                "elements",
                                "enable_cc",
                                "id",
                                "level",
                                "name",
                                "process",
                                "type"
                            ],
                            "properties": {
                                "cc": {
                                    "type": "object",
                                    "required": [
                                        "node",
                                        "selecter",
                                        "type"
                                    ],
                                    "properties": {
                                        "node": {
                                            "type": "string"
                                        },
                                        "selecter": {
                                            "type": "object",
                                            "required": [
                                                "id",
                                                "name",
                                                "range_remote",
                                                "type",
                                                "value_type"
                                            ],
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "range_remote": {
                                                    "type": "object",
                                                    "required": [
                                                        "type"
                                                    ],
                                                    "properties": {
                                                        "type": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "additionalProperties": true
                                                },
                                                "type": {
                                                    "type": "string"
                                                },
                                                "value_type": {
                                                    "type": "string"
                                                }
                                            },
                                            "additionalProperties": true
                                        },
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "elements": {
                                    "type": "array",
                                    "items": {
                                        "anyOf": [
                                            {
                                                "type": "object",
                                                "required": [
                                                    "check",
                                                    "id",
                                                    "name",
                                                    "perm",
                                                    "range_remote",
                                                    "type",
                                                    "value_type"
                                                ],
                                            },
                                            {
                                                "type": "object",
                                                "required": [
                                                    "check",
                                                    "id",
                                                    "name",
                                                    "perm",
                                                    "type",
                                                    "value_type",
                                                    "view"
                                                ],
                                            },
                                            {
                                                "type": "object",
                                                "required": [
                                                    "check",
                                                    "id",
                                                    "name",
                                                    "perm",
                                                    "type",
                                                    "value_type"
                                                ],
                                            },
                                            {
                                                "type": "object",
                                                "required": [
                                                    "check",
                                                    "id",
                                                    "name",
                                                    "perm",
                                                    "type",
                                                    "upload_url",
                                                    "value_type"
                                                ],
                                            },
                                            {
                                                "type": "object",
                                                "required": [
                                                    "check",
                                                    "filters",
                                                    "id",
                                                    "name",
                                                    "perm",
                                                    "range_remote",
                                                    "type",
                                                    "value_type"
                                                ],
                                            }
                                        ]
                                    }
                                },
                                "enable_cc": {
                                    "type": "boolean"
                                },
                                "id": {
                                    "type": "string"
                                },
                                "level": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "process": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                }
                            },
                            "additionalProperties": true
                        }
                    },
                    "additionalProperties": true
                },
                "schema": {
                    "type": "object",
                    "required": [
                        "properties",
                        "required",
                        "type"
                    ],
                    "properties": {
                        "properties": {
                            "type": "object",
                            "required": [
                                "contant",
                                "contract",
                                "deliver",
                                "first_party",
                                "manage",
                                "manager",
                                "receive",
                                "receiver",
                                "sender",
                                "user_file"
                            ],
                            "properties": {
                                "contant": {
                                    "type": "object",
                                    "required": [
                                        "maxLength",
                                        "minLength",
                                        "type"
                                    ],
                                    "properties": {
                                        "maxLength": {
                                            "type": "integer"
                                        },
                                        "minLength": {
                                            "type": "integer"
                                        },
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "contract": {
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "deliver": {
                                    "type": "object",
                                    "required": [
                                        "minLength",
                                        "type"
                                    ],
                                    "properties": {
                                        "minLength": {
                                            "type": "integer"
                                        },
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "first_party": {
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "manage": {
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "manager": {
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "receive": {
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "receiver": {
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "sender": {
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                },
                                "user_file": {
                                    "type": "object",
                                    "required": [
                                        "items",
                                        "maxItems",
                                        "minItems",
                                        "type"
                                    ],
                                    "properties": {
                                        "items": {
                                            "type": "object",
                                            "required": [
                                                "properties",
                                                "required",
                                                "type"
                                            ],
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "required": [
                                                        "filename",
                                                        "md5"
                                                    ],
                                                    "properties": {
                                                        "filename": {
                                                            "type": "object",
                                                            "required": [
                                                                "type"
                                                            ],
                                                            "properties": {
                                                                "type": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "additionalProperties": true
                                                        },
                                                        "md5": {
                                                            "type": "object",
                                                            "required": [
                                                                "type"
                                                            ],
                                                            "properties": {
                                                                "type": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "additionalProperties": true
                                                        }
                                                    },
                                                    "additionalProperties": true
                                                },
                                                "required": {
                                                    "type": "array",
                                                    "items": {
                                                        "anyOf": [
                                                            {
                                                                "type": "string"
                                                            }
                                                        ]
                                                    }
                                                },
                                                "type": {
                                                    "type": "string"
                                                }
                                            },
                                            "additionalProperties": true
                                        },
                                        "maxItems": {
                                            "type": "integer"
                                        },
                                        "minItems": {
                                            "type": "integer"
                                        },
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": true
                                }
                            },
                            "additionalProperties": true
                        },
                        "required": {
                            "type": "array",
                            "items": {
                                "anyOf": [
                                    {
                                        "type": "string"
                                    }
                                ]
                            }
                        },
                        "type": {
                            "type": "string"
                        }
                    },
                    "additionalProperties": true
                }
            },
            "additionalProperties": true
        },
        "result": {
            "type": "integer"
        }
    },
    "additionalProperties": true
}

log.error(validate(instance=ojt, schema=schema_array_noprop))





'''
responsedata = prev.getResponseDataAsString()

log.error(responsedata)


log.error(SampleResult.getResponseDataAsString())



if 'UserRangeRemote' in responsedata:
	prev.setSuccessful(True)

headers = prev.getRequestHeaders()
log.error(headers)

code = prev.getResponseCode()
log.error(code)

responsesheader= prev.getResponseHeaders()
log.error(responsesheader)


url1 = prev.getUrlAsString()
log.error(url1)

prev.setResponseMessage("这是响应信息")
prev.setResponseCode("404")

log.error(vars.get("group_id"))

vars.put("group_id","jack")

log.error(vars.get("group_id"))

'''



'''
prev.getResponseDataAsString()与prev.getResponseData()都是获取Response Body的内容，只是返回的数据类型不同，
prev.getResponseDataAsString()返回String字符串，prev.getResponseData()返回byte[]字节数组，使用时可根据实际需要对返回数据进行处理。

获取请求头信息
String headers = prev.getRequestHeaders() ;

获取请求返回的code
String code = prev.getResponseCode() ;
获取响应信息
String responsesmessage = prev.getResponseMessage() ;

获取响应头信息
String responsesheader= prev.getResponseHeaders() ;

//获取请求URL
URL url = prev.getURL() ;
String url1 = prev.getUrlAsString();

设置响应信息Response message
prev.setResponseMessage("这是响应信息");
设置响应代码Response code
prev.setResponseCode("404");


打印日志 ，日志会保存在bin目录下的jmeter.log文件中
默认支持级别为info及以上，debug级别日志由于太多，默认不支持
log.error("This is error message");


设置属性与调用属性
${__setProperty(test1,property1,)};
props.put("test2","property2");
String test1 =props.get("test1");
String test2 = props.get("test2");

属性是所有线程公有的，需要注意的是，在JSR223或BeanShell中使用props.put（”name”，”value”）创建的属性，
不能直接在当前JSR223或BeanShell中使用${__P(name,)}或${__property(name,,)}进行调用，
如果需要在当前JSR223或BeanShell中调用，需要使用props.get("name")方法。此处的name是属性名称，而不是随机的字符串。

定义变量与调用变量
此处的name是在用户定义的变量中定义的变量，已赋值为lucy
String test5 = vars.get("name");
//定义变量值，并获取
vars.put("name2","jack");
String test6 = vars.get("name2");

通过vars.put(“name”,”value”)方式定义的变量作用域限制为当前线程组，如果要跨线程调用，请使用属性定义，与props.put（”name”，”value”）
同样的，vars.put(“name”,”value”)创建的变量，也不能直接在当前JSR223或BeanShell中使用${name}进行调用，而是使用vars.get("name")方法。
'''