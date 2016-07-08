#coding:utf8

import re
import string

'''
ord()  chr()可以返回字符的ASCII码
'''
def  originChar():
	originList=[]
	first='a'
	firstAscii=ord(first)
	for i in range(26):
		order=firstAscii+i
		string=chr(order)
		originList.append(string)
	return originList

'''
extend 是原地操作，是改变了第一个列表
'''
def  mappingList(originList):
	firstHalf=originList[2:]
	end=originList[:2]
	firstHalf.extend(end)
	return firstHalf

#判断是不是特殊字符　使用了正则表达式
def   judge(char):
	pattern=re.compile(r'[a-z]')
	if pattern.match(char) is not None:
		return True
	else:
		return False


def  parse(string,originList,mapList):
	stringList=string.split(' ')
	sentence=[]
	for item in stringList:
		word=''
		for element in item:
			if judge(element):
				number=originList.index(element)
				rightchar=mapList[number]
				word=word+rightchar
			else:
				word=word+element
		sentence.append(word)
	return sentence


def newmethod(string_origin):
	table = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
	return string_origin.translate(table)





#string='a'
#s=string.decode('ascii')
def main():
	originList=originChar()
	mapList=mappingList(originList)
	string_origin='g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '
	url="map"
	sentence=parse(string_origin, originList, mapList)
	url_parse=parse(url,originList,mapList)
	print url_parse,sentence
	result=newmethod(string_origin)
	print result

main()