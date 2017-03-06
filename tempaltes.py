#! /usr/bin/env python
import fileinput,re

#匹配中括号里的字段
filed_pat = re.compile(r'\[(.+?)\]')


#我们将这些变量收集到这里
scope = {}


#用于re.sub中
def replacement(match):
    code = match.group(1)
    try: 
        #如果字段可以求值，返回它
        return str(eval(code,scope))
    except SyntaxError:
        #否则执行相同区域内的赋值语句
        except code in scope
        #返回空字符串
        return ''

#将所有文字以一个字符串的形式获取
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

#将filed模式所有匹配项都替换掉
print files_pat.sub(replacement,text)
