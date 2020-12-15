#! python2
from jsonschema import validate

true = True 
false = False 

#1
instance_json = {"data":{"definition":{"processform":{"cc":{"node":"4","selecter":{"id":"CC","name":"\u6284\u9001","range_remote":{"type":"UserRangeRemote"},"type":"MulSelectUser4CC","value_type":"int"},"type":"UserTaskCC"},"elements":[{"check":{"required":true},"id":"contract","name":"\u603b\u627f\u5305\u5355\u4f4d","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"PartnerRangeRemote"},"type":"SelectPartner","value_type":"int"},{"check":{"required":true},"id":"manage","name":"\u76d1\u7406\u5355\u4f4d","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"PartnerRangeRemote"},"type":"SelectPartner","value_type":"int"},{"check":{"required":true},"id":"receive","name":"\u63a5\u6536\u5355\u4f4d","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"PartnerRangeRemote"},"type":"SelectPartner","value_type":"int"},{"check":{"format":"YYYY-MM-DD","required":true},"id":"deliver","name":"\u5b9e\u7269\u4ea4\u63a5\u65e5\u671f","perm":{"editable":true,"visible":true,"writable":true},"type":"Date","value_type":"text","view":{"format":"YYYY-MM-DD"}},{"check":{"max_length":2000,"min_length":0,"required":false},"id":"contant","name":"\u79fb\u4ea4\u5185\u5bb9","perm":{"editable":true,"visible":true,"writable":true},"type":"TextArea","value_type":"text"},{"check":{"max_count":100,"min_count":0,"required":false},"id":"user_file","name":"\u9644\u4ef6","perm":{"editable":true,"visible":true,"writable":true},"type":"MulFile","upload_url":"/platform/v1/papi/app_file/upload/","value_type":"struct"},{"check":{"required":true,"unique":true},"filters":{"role":false,"unit":false},"id":"sender","name":"\u79fb\u4ea4\u5355\u4f4d\u4eba\u5458","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"UserRangeRemote"},"type":"SelectUser","value_type":"int"},{"check":{"required":true,"unique":true},"filters":{"role":false,"unit":false},"id":"receiver","name":"\u63a5\u6536\u5355\u4f4d\u4eba\u5458","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"UserRangeRemote"},"type":"SelectUser","value_type":"int"},{"check":{"required":true,"unique":true},"filters":{"role":false,"unit":false},"id":"manager","name":"\u76d1\u7406\u603b\u76d1\u5ba1\u6838","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"UserRangeRemote"},"type":"SelectUser","value_type":"int"},{"check":{"required":true,"unique":true},"filters":{"role":false,"unit":false},"id":"first_party","name":"\u7532\u65b9\u9879\u76ee\u7ecf\u7406\u5ba1\u6838","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"UserRangeRemote"},"type":"SelectUser","value_type":"int"}],"enable_cc":true,"id":"worktransfer_yc","level":"project","name":"\u5de5\u4f5c\u9762\u79fb\u4ea4","process":"worktransfer_yc","type":"ProcessForm"}},"schema":{"properties":{"contant":{"maxLength":2000,"minLength":0,"type":"string"},"contract":{"type":"integer"},"deliver":{"minLength":1,"type":"string"},"first_party":{"type":"integer"},"manage":{"type":"integer"},"manager":{"type":"integer"},"receive":{"type":"integer"},"receiver":{"type":"integer"},"sender":{"type":"integer"},"user_file":{"items":{"properties":{"filename":{"type":"string"},"md5":{"type":"string"}},"required":["md5"],"type":"object"},"maxItems":100,"minItems":0,"type":"array"}},"required":["contract","manage","receive","deliver","sender","receiver","manager","first_party"],"type":"object"}},"result":0}

responsedata_copy = '{"data":{"definition":{"processform":{"cc":{"node":"4","selecter":{"id":"CC","name":"\u6284\u9001","range_remote":{"type":"UserRangeRemote"},"type":"MulSelectUser4CC","value_type":"int"},"type":"UserTaskCC"},"elements":[{"check":{"required":true},"id":"contract","name":"\u603b\u627f\u5305\u5355\u4f4d","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"PartnerRangeRemote"},"type":"SelectPartner","value_type":"int"},{"check":{"required":true},"id":"manage","name":"\u76d1\u7406\u5355\u4f4d","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"PartnerRangeRemote"},"type":"SelectPartner","value_type":"int"},{"check":{"required":true},"id":"receive","name":"\u63a5\u6536\u5355\u4f4d","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"PartnerRangeRemote"},"type":"SelectPartner","value_type":"int"},{"check":{"format":"YYYY-MM-DD","required":true},"id":"deliver","name":"\u5b9e\u7269\u4ea4\u63a5\u65e5\u671f","perm":{"editable":true,"visible":true,"writable":true},"type":"Date","value_type":"text","view":{"format":"YYYY-MM-DD"}},{"check":{"max_length":2000,"min_length":0,"required":false},"id":"contant","name":"\u79fb\u4ea4\u5185\u5bb9","perm":{"editable":true,"visible":true,"writable":true},"type":"TextArea","value_type":"text"},{"check":{"max_count":100,"min_count":0,"required":false},"id":"user_file","name":"\u9644\u4ef6","perm":{"editable":true,"visible":true,"writable":true},"type":"MulFile","upload_url":"/platform/v1/papi/app_file/upload/","value_type":"struct"},{"check":{"required":true,"unique":true},"filters":{"role":false,"unit":false},"id":"sender","name":"\u79fb\u4ea4\u5355\u4f4d\u4eba\u5458","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"UserRangeRemote"},"type":"SelectUser","value_type":"int"},{"check":{"required":true,"unique":true},"filters":{"role":false,"unit":false},"id":"receiver","name":"\u63a5\u6536\u5355\u4f4d\u4eba\u5458","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"UserRangeRemote"},"type":"SelectUser","value_type":"int"},{"check":{"required":true,"unique":true},"filters":{"role":false,"unit":false},"id":"manager","name":"\u76d1\u7406\u603b\u76d1\u5ba1\u6838","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"UserRangeRemote"},"type":"SelectUser","value_type":"int"},{"check":{"required":true,"unique":true},"filters":{"role":false,"unit":false},"id":"first_party","name":"\u7532\u65b9\u9879\u76ee\u7ecf\u7406\u5ba1\u6838","perm":{"editable":true,"visible":true,"writable":true},"range_remote":{"type":"UserRangeRemote"},"type":"SelectUser","value_type":"int"}],"enable_cc":true,"id":"worktransfer_yc","level":"project","name":"\u5de5\u4f5c\u9762\u79fb\u4ea4","process":"worktransfer_yc","type":"ProcessForm"}},"schema":{"properties":{"contant":{"maxLength":2000,"minLength":0,"type":"string"},"contract":{"type":"integer"},"deliver":{"minLength":1,"type":"string"},"first_party":{"type":"integer"},"manage":{"type":"integer"},"manager":{"type":"integer"},"receive":{"type":"integer"},"receiver":{"type":"integer"},"sender":{"type":"integer"},"user_file":{"items":{"properties":{"filename":{"type":"string"},"md5":{"type":"string"}},"required":["md5"],"type":"object"},"maxItems":100,"minItems":0,"type":"array"}},"required":["contract","manage","receive","deliver","sender","receiver","manager","first_party"],"type":"object"}},"result":0}'


#anyof
schema_instance_anyof = {
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
                                                "properties": {
                                                    "check": {
                                                        "type": "object",
                                                        "required": [
                                                            "required"
                                                        ],
                                                        "properties": {
                                                            "required": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
                                                    },
                                                    "id": {
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
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
                                                "properties": {
                                                    "check": {
                                                        "type": "object",
                                                        "required": [
                                                            "format",
                                                            "required"
                                                        ],
                                                        "properties": {
                                                            "format": {
                                                                "type": "string"
                                                            },
                                                            "required": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
                                                    },
                                                    "id": {
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
                                                    },
                                                    "type": {
                                                        "type": "string"
                                                    },
                                                    "value_type": {
                                                        "type": "string"
                                                    },
                                                    "view": {
                                                        "type": "object",
                                                        "required": [
                                                            "format"
                                                        ],
                                                        "properties": {
                                                            "format": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "additionalProperties": true
                                                    }
                                                },
                                                "additionalProperties": true
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
                                                "properties": {
                                                    "check": {
                                                        "type": "object",
                                                        "required": [
                                                            "max_length",
                                                            "min_length",
                                                            "required"
                                                        ],
                                                        "properties": {
                                                            "max_length": {
                                                                "type": "integer"
                                                            },
                                                            "min_length": {
                                                                "type": "integer"
                                                            },
                                                            "required": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
                                                    },
                                                    "id": {
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "type": "boolean"
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
                                                "properties": {
                                                    "check": {
                                                        "type": "object",
                                                        "required": [
                                                            "max_count",
                                                            "min_count",
                                                            "required"
                                                        ],
                                                        "properties": {
                                                            "max_count": {
                                                                "type": "integer"
                                                            },
                                                            "min_count": {
                                                                "type": "integer"
                                                            },
                                                            "required": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
                                                    },
                                                    "id": {
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
                                                    },
                                                    "type": {
                                                        "type": "string"
                                                    },
                                                    "upload_url": {
                                                        "type": "string"
                                                    },
                                                    "value_type": {
                                                        "type": "string"
                                                    }
                                                },
                                                "additionalProperties": true
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
                                                "properties": {
                                                    "check": {
                                                        "type": "object",
                                                        "required": [
                                                            "required",
                                                            "unique"
                                                        ],
                                                        "properties": {
                                                            "required": {
                                                                "type": "boolean"
                                                            },
                                                            "unique": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
                                                    },
                                                    "filters": {
                                                        "type": "object",
                                                        "required": [
                                                            "role",
                                                            "unit"
                                                        ],
                                                        "properties": {
                                                            "role": {
                                                                "type": "boolean"
                                                            },
                                                            "unit": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
                                                    },
                                                    "id": {
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": true
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

schema_instance = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "required": [
        "data",
        "result"
    ],
    "properties": {
        "data": {
            "$id": "#/properties/data",
            "type": "object",
            "required": [
                "definition",
                "schema"
            ],
            "properties": {
                "definition": {
                    "$id": "#/properties/data/properties/definition",
                    "type": "object",
                    "required": [
                        "processform"
                    ],
                    "properties": {
                        "processform": {
                            "$id": "#/properties/data/properties/definition/properties/processform",
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
                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/cc",
                                    "type": "object",
                                    "required": [
                                        "node",
                                        "selecter",
                                        "type"
                                    ],
                                    "properties": {
                                        "node": {
                                            "$id": "#/properties/data/properties/definition/properties/processform/properties/cc/properties/node",
                                            "type": "string"
                                        },
                                        "selecter": {
                                            "$id": "#/properties/data/properties/definition/properties/processform/properties/cc/properties/selecter",
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
                                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/cc/properties/selecter/properties/id",
                                                    "type": "string"
                                                },
                                                "name": {
                                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/cc/properties/selecter/properties/name",
                                                    "type": "string"
                                                },
                                                "range_remote": {
                                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/cc/properties/selecter/properties/range_remote",
                                                    "type": "object",
                                                    "required": [
                                                        "type"
                                                    ],
                                                    "properties": {
                                                        "type": {
                                                            "$id": "#/properties/data/properties/definition/properties/processform/properties/cc/properties/selecter/properties/range_remote/properties/type",
                                                            "type": "string"
                                                        }
                                                    },
                                                    "additionalProperties": false
                                                },
                                                "type": {
                                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/cc/properties/selecter/properties/type",
                                                    "type": "string"
                                                },
                                                "value_type": {
                                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/cc/properties/selecter/properties/value_type",
                                                    "type": "string"
                                                }
                                            },
                                            "additionalProperties": false
                                        },
                                        "type": {
                                            "$id": "#/properties/data/properties/definition/properties/processform/properties/cc/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "elements": {
                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/elements",
                                    "type": "array",
                                    "additionalItems": false,
                                    "items": {
                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items",
                                        "anyOf": [
                                            {
                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0",
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
                                                "properties": {
                                                    "check": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/check",
                                                        "type": "object",
                                                        "required": [
                                                            "required"
                                                        ],
                                                        "properties": {
                                                            "required": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/check/properties/required",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "id": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/id",
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/name",
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/perm",
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/perm/properties/editable",
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/perm/properties/visible",
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/perm/properties/writable",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "range_remote": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/range_remote",
                                                        "type": "object",
                                                        "required": [
                                                            "type"
                                                        ],
                                                        "properties": {
                                                            "type": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/range_remote/properties/type",
                                                                "type": "string"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/type",
                                                        "type": "string"
                                                    },
                                                    "value_type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/0/properties/value_type",
                                                        "type": "string"
                                                    }
                                                },
                                                "additionalProperties": false
                                            },
                                            {
                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1",
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
                                                "properties": {
                                                    "check": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/check",
                                                        "type": "object",
                                                        "required": [
                                                            "format",
                                                            "required"
                                                        ],
                                                        "properties": {
                                                            "format": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/check/properties/format",
                                                                "type": "string"
                                                            },
                                                            "required": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/check/properties/required",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "id": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/id",
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/name",
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/perm",
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/perm/properties/editable",
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/perm/properties/visible",
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/perm/properties/writable",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/type",
                                                        "type": "string"
                                                    },
                                                    "value_type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/value_type",
                                                        "type": "string"
                                                    },
                                                    "view": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/view",
                                                        "type": "object",
                                                        "required": [
                                                            "format"
                                                        ],
                                                        "properties": {
                                                            "format": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/1/properties/view/properties/format",
                                                                "type": "string"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    }
                                                },
                                                "additionalProperties": false
                                            },
                                            {
                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2",
                                                "type": "object",
                                                "required": [
                                                    "check",
                                                    "id",
                                                    "name",
                                                    "perm",
                                                    "type",
                                                    "value_type"
                                                ],
                                                "properties": {
                                                    "check": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/check",
                                                        "type": "object",
                                                        "required": [
                                                            "max_length",
                                                            "min_length",
                                                            "required"
                                                        ],
                                                        "properties": {
                                                            "max_length": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/check/properties/max_length",
                                                                "type": "integer"
                                                            },
                                                            "min_length": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/check/properties/min_length",
                                                                "type": "integer"
                                                            },
                                                            "required": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/check/properties/required",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "id": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/id",
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/name",
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/perm",
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/perm/properties/editable",
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/perm/properties/visible",
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/perm/properties/writable",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/type",
                                                        "type": "string"
                                                    },
                                                    "value_type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/2/properties/value_type",
                                                        "type": "string"
                                                    }
                                                },
                                                "additionalProperties": false
                                            },
                                            {
                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3",
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
                                                "properties": {
                                                    "check": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/check",
                                                        "type": "object",
                                                        "required": [
                                                            "max_count",
                                                            "min_count",
                                                            "required"
                                                        ],
                                                        "properties": {
                                                            "max_count": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/check/properties/max_count",
                                                                "type": "integer"
                                                            },
                                                            "min_count": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/check/properties/min_count",
                                                                "type": "integer"
                                                            },
                                                            "required": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/check/properties/required",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "id": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/id",
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/name",
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/perm",
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/perm/properties/editable",
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/perm/properties/visible",
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/perm/properties/writable",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/type",
                                                        "type": "string"
                                                    },
                                                    "upload_url": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/upload_url",
                                                        "type": "string"
                                                    },
                                                    "value_type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/3/properties/value_type",
                                                        "type": "string"
                                                    }
                                                },
                                                "additionalProperties": false
                                            },
                                            {
                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4",
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
                                                "properties": {
                                                    "check": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/check",
                                                        "type": "object",
                                                        "required": [
                                                            "required",
                                                            "unique"
                                                        ],
                                                        "properties": {
                                                            "required": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/check/properties/required",
                                                                "type": "boolean"
                                                            },
                                                            "unique": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/check/properties/unique",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "filters": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/filters",
                                                        "type": "object",
                                                        "required": [
                                                            "role",
                                                            "unit"
                                                        ],
                                                        "properties": {
                                                            "role": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/filters/properties/role",
                                                                "type": "boolean"
                                                            },
                                                            "unit": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/filters/properties/unit",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "id": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/id",
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/name",
                                                        "type": "string"
                                                    },
                                                    "perm": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/perm",
                                                        "type": "object",
                                                        "required": [
                                                            "editable",
                                                            "visible",
                                                            "writable"
                                                        ],
                                                        "properties": {
                                                            "editable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/perm/properties/editable",
                                                                "type": "boolean"
                                                            },
                                                            "visible": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/perm/properties/visible",
                                                                "type": "boolean"
                                                            },
                                                            "writable": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/perm/properties/writable",
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "range_remote": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/range_remote",
                                                        "type": "object",
                                                        "required": [
                                                            "type"
                                                        ],
                                                        "properties": {
                                                            "type": {
                                                                "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/range_remote/properties/type",
                                                                "type": "string"
                                                            }
                                                        },
                                                        "additionalProperties": false
                                                    },
                                                    "type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/type",
                                                        "type": "string"
                                                    },
                                                    "value_type": {
                                                        "$id": "#/properties/data/properties/definition/properties/processform/properties/elements/items/anyOf/4/properties/value_type",
                                                        "type": "string"
                                                    }
                                                },
                                                "additionalProperties": false
                                            }
                                        ]
                                    }
                                },
                                "enable_cc": {
                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/enable_cc",
                                    "type": "boolean"
                                },
                                "id": {
                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/id",
                                    "type": "string"
                                },
                                "level": {
                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/level",
                                    "type": "string"
                                },
                                "name": {
                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/name",
                                    "type": "string"
                                },
                                "process": {
                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/process",
                                    "type": "string"
                                },
                                "type": {
                                    "$id": "#/properties/data/properties/definition/properties/processform/properties/type",
                                    "type": "string"
                                }
                            },
                            "additionalProperties": false
                        }
                    },
                    "additionalProperties": false
                },
                "schema": {
                    "$id": "#/properties/data/properties/schema",
                    "type": "object",
                    "required": [
                        "properties",
                        "required",
                        "type"
                    ],
                    "properties": {
                        "properties": {
                            "$id": "#/properties/data/properties/schema/properties/properties",
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
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/contant",
                                    "type": "object",
                                    "required": [
                                        "maxLength",
                                        "minLength",
                                        "type"
                                    ],
                                    "properties": {
                                        "maxLength": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/contant/properties/maxLength",
                                            "type": "integer"
                                        },
                                        "minLength": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/contant/properties/minLength",
                                            "type": "integer"
                                        },
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/contant/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "contract": {
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/contract",
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/contract/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "deliver": {
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/deliver",
                                    "type": "object",
                                    "required": [
                                        "minLength",
                                        "type"
                                    ],
                                    "properties": {
                                        "minLength": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/deliver/properties/minLength",
                                            "type": "integer"
                                        },
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/deliver/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "first_party": {
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/first_party",
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/first_party/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "manage": {
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/manage",
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/manage/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "manager": {
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/manager",
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/manager/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "receive": {
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/receive",
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/receive/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "receiver": {
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/receiver",
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/receiver/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "sender": {
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/sender",
                                    "type": "object",
                                    "required": [
                                        "type"
                                    ],
                                    "properties": {
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/sender/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "user_file": {
                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file",
                                    "type": "object",
                                    "required": [
                                        "items",
                                        "maxItems",
                                        "minItems",
                                        "type"
                                    ],
                                    "properties": {
                                        "items": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items",
                                            "type": "object",
                                            "required": [
                                                "properties",
                                                "required",
                                                "type"
                                            ],
                                            "properties": {
                                                "properties": {
                                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items/properties/properties",
                                                    "type": "object",
                                                    "required": [
                                                        "filename",
                                                        "md5"
                                                    ],
                                                    "properties": {
                                                        "filename": {
                                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items/properties/properties/properties/filename",
                                                            "type": "object",
                                                            "required": [
                                                                "type"
                                                            ],
                                                            "properties": {
                                                                "type": {
                                                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items/properties/properties/properties/filename/properties/type",
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "additionalProperties": false
                                                        },
                                                        "md5": {
                                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items/properties/properties/properties/md5",
                                                            "type": "object",
                                                            "required": [
                                                                "type"
                                                            ],
                                                            "properties": {
                                                                "type": {
                                                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items/properties/properties/properties/md5/properties/type",
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "additionalProperties": false
                                                        }
                                                    },
                                                    "additionalProperties": false
                                                },
                                                "required": {
                                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items/properties/required",
                                                    "type": "array",
                                                    "additionalItems": false,
                                                    "items": {
                                                        "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items/properties/required/items",
                                                        "anyOf": [
                                                            {
                                                                "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items/properties/required/items/anyOf/0",
                                                                "type": "string"
                                                            }
                                                        ]
                                                    }
                                                },
                                                "type": {
                                                    "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/items/properties/type",
                                                    "type": "string"
                                                }
                                            },
                                            "additionalProperties": false
                                        },
                                        "maxItems": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/maxItems",
                                            "type": "integer"
                                        },
                                        "minItems": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/minItems",
                                            "type": "integer"
                                        },
                                        "type": {
                                            "$id": "#/properties/data/properties/schema/properties/properties/properties/user_file/properties/type",
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                }
                            },
                            "additionalProperties": false
                        },
                        "required": {
                            "$id": "#/properties/data/properties/schema/properties/required",
                            "type": "array",
                            "additionalItems": false,
                            "items": {
                                "$id": "#/properties/data/properties/schema/properties/required/items",
                                "anyOf": [
                                    {
                                        "$id": "#/properties/data/properties/schema/properties/required/items/anyOf/0",
                                        "type": "string"
                                    }
                                ]
                            }
                        },
                        "type": {
                            "$id": "#/properties/data/properties/schema/properties/type",
                            "type": "string"
                        }
                    },
                    "additionalProperties": false
                }
            },
            "additionalProperties": false
        },
        "result": {
            "$id": "#/properties/result",
            "type": "integer"
        }
    },
    "additionalProperties": false
}

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
print(validate(instance=instance_json, schema=schema_array_noprop))

print(type(instance_json))
print(type(responsedata_copy))

#print(instance_json)