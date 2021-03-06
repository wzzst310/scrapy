# coding:utf-8

import json
from _11_parse_url import parse_url, headers
from pprint import pprint

url = "https://m.douban.com/rexxar/api/v2/gallery/subject_feed?start=0&count=4&subject_id=27083561&ck=null"
add_headers = {
    "Accept": "*/*",
    "Origin": "https://movie.douban.com",
    "Referer": "https://movie.douban.com/subject/27083561/?from=showing"
}
headers.update(add_headers)
data_dict = {"start": "0", "count": "4", "subject_id": "27083561", "ck": "null"}
html_str = parse_url(url, method="POST", data=data_dict)
print(html_str)
# json.loads 把json字符串转化为python类型
# ret1 = eval(html_str)
ret1 = json.loads(html_str)
# pprint(ret1)
# print(type(ret1))
# json.dumps能够把python类型转化为json字符串
with open("douban.json", "w", encoding="utf-8") as f:
    # indent = 4 缩进4格 一个tab
    f.write(json.dumps(ret1, ensure_ascii=False, indent=4))
    # f.write(str(ret1))

with open("douban.json", "r", encoding="utf-8") as f:
    ret2 = f.read()
    ret3 = json.loads(ret2)
    print(ret3)
    print(type(ret3))

# 具有read()或者write()方法的对象就是类文件对象通常叫做fp
# 使用json.load提取类文件对象中的数据
with open("douban.json", "r", encoding="utf-8") as f:
    ret4 = json.load(f)
    print('ret4 %s' % ret4)
    print('ret4 type %s' % type(ret4))

with open("douban_dump.json", "w", encoding="utf-8") as f:
    json.dump(ret4, f, ensure_ascii=False, indent=4)
