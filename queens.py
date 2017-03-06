#! /usr/bin/env python
def queens(num=8,state=()):
    for pos in range(num):
#num参数是皇后的总数
        if not conflict(state,pos):
#state参数是存放前面皇后的位置信息的元组
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num,state + (pos,)):
                    yield (pos,) + result

#len(list(queens(8)))
