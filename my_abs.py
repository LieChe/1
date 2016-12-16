# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('非整型或浮点型数据!')
    if x > 0:
        return x
    else:
        return -x