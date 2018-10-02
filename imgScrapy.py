#test_爬取来自www.doutula.com的表情包
from urllib import request
from urllib import parse
import urllib
import re
import sys
import os
import time

page=1
x=0
totolnum=0
sys.stdin.encoding

def filename(keyword):
    path=os.path.abspath('.')
    newpath=path+'\\img\\'+keyword
    if(os.path.exists(newpath)==False):
        os.makedirs(path+'\\img\\'+keyword)
    return newpath

def link(keyword,pagenum):
    qkeyword=urllib.parse.quote(keyword)
    page="&page="+str(pagenum)
    search='search?type=photo&more=1&keyword='
    url="http://www.doutula.com/"
    link=url+search+qkeyword+page
    req=request.Request(link)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
    text=request.urlopen(req).read()
    text=text.decode('utf-8')
    return text

def content(keyword,pagenum):
    text=link(keyword,pagenum)
    pattern1='data-original="(http|https):(/|\w|\.)+(gif|jpg|png)"'
    match=re.finditer(pattern1,text)
    return match


keyword=input("请输入想要爬取的表情包的名字  ")
page=int(input("请输入爬取页数  "))
newpath=filename(keyword)
if os.path.exists('match.txt')==True:
    os.remove('match.txt')


for pagei in range(1,page+1):
    match=content(keyword,pagei)
    f=open('match.txt','a+')
    f.write('\n')
    for i in match:
        f.write(i.group())
        f.write('\n')
        totolnum+=1
    f.close()


f=open('match.txt','r+')
str=f.read()
pattern2='(http|https):(/|\w|\.)+(gif|jpg|png)'
src=re.finditer(pattern2,str)
for i in src:
    urllib.request.urlretrieve(i.group(),newpath+'\\'+'%s.jpg' %(x+1))
    x+=1
    print('正在爬取%d/%d' %(x,totolnum))
    time.sleep(0.8)
f.close()

if totolnum==0:
    print('对不起,找不到关于%s的表情包,请重新输入' %keyword)
else:
    print('爬取完成,爬取%d个文件\n保存在%s' %(totolnum,newpath))