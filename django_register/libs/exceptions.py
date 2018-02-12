# -*- coding: utf-8 -*-


# 缺少属性异常
class LackPropertiesException(Exception):
    pass


# 非法属性异常
class InvalidPropertiesException(Exception):
    pass


# 属性值为空异常
class PropertiesEmptyException(Exception):
    pass
