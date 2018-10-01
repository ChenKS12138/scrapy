#test_爬取来自www.doutula.com的表情包
from urllib import request
from urllib import parse
import urllib
import re
import sys
sys.stdin.encoding
keyword=input("请输入想要爬取的表情包的名字\n(文件将会被保存在D:\\test)")
keyword=urllib.parse.quote(keyword)
page="&page=2"
search='search?type=photo&more=1&keyword='
url="http://www.doutula.com/"
link=url+search+keyword
req=request.Request(link)
req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
text=request.urlopen(req).read()
text=text.decode('utf-8')
pattern1='data-original="(http|https):(/|\w|\.)+(gif|jpg|png)"'
match=re.finditer(pattern1,text)
f=open('match.txt','w+')
f.write('\n')
totolnum=0
for i in match:
    f.write(i.group())
    f.write('\n')
    totolnum+=1
f.close()
f=open('match.txt','r+')
str=f.read()
pattern2='(http|https):(/|\w|\.)+(gif|jpg|png)'
src=re.finditer(pattern2,str)
x=0
for i in src:
    urllib.request.urlretrieve(i.group(),'D:\\test\\%s.jpg' %x)
    x+=1
    print('正在爬取%d/%d' %(x,totolnum))
f.close()
print('爬取完成,爬取%d个文件,保存在D:\\test' %totolnum)