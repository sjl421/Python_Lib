#coding=utf-8

import glob

#得到当前目录下的所有python文件，返回一个列表
f = glob.glob(r'./*.py')
for i in f:
	print i

#得到父级目录下所有的文件，返回一个生成器，也能够用for循环遍历

t = glob.iglob(r'../*')

print t.next()

for j in t:
	print j
