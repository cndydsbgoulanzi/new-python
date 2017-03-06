#! /usr/bin/env python
def flatten(nested):
    try:
        #不要迭代类似字符串的对象
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield elemnt
    except TypeError:
        yield nested

#测试
#list(flatten(['foo',['bar',['baz']]]) 
