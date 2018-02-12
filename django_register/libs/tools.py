# -*- coding: utf-8 -*-
import libs.exceptions
from functools import wraps


# 参数验证
def args_required(method, *required):

    def wrapper(func):

        @wraps(func)
        def handler(request, *args, **kwargs):

            req = getattr(request, method)
            for key in required:
                if key not in req:
                    raise libs.exceptions.LackPropertiesException(u'缺少必需参数 %s' % key)

            return func(request, *args, **kwargs)
        return handler
    return wrapper
