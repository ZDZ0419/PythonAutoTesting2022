'''
json：是一个固定格式的字符串
'''
import json
# json格式-->python格式
jsondata='{"name":"张三","age":18}'  #--json格式
pythondata=json.loads(jsondata)   #json.loads()  json格式转换为python
print(type(pythondata),pythondata)
print(type(jsondata),jsondata)
# python格式 --> json格式
pyhtondata1={"name":"张三","age":18}  # --python格式
jsondata1=json.dumps(pyhtondata1,ensure_ascii=False)#ensure_ascii=False:禁用ascii转码
print(type(jsondata1),jsondata1)
print(type(pyhtondata1),pyhtondata1)
