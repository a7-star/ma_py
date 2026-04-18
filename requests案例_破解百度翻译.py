import requests
import json

if __name__=='__main__':
	#指定url
	post_url='https://fanyi.baidu.com/sug'
	#UA伪装
	headers={'user-agent':'Mozilla/5.0 (Linux; Android 16; 2407FRK8EC Build/BP2A.250605.031.A3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.7151.115 Mobile Safari/537.36'}
	#post请求参数处理（同get请求一致）
	word=input ('请输入要翻译的词：')
	data={
		'kw':word
	}
	#请求发送		
	response=requests.post(url=post_url,data=data,headers=headers)
	#获取响应数据
	dic_obj=response.json()
	
	#持久化存储
	fp=open (word+'.json','w',encoding='utf-8')
	json.dump(dic_obj,fp,ensure_ascii=False)
	fp.close()
	print ('打印成功！')
	with open (word+'.json','r',encoding='utf-8')as f:
		读取=f.read()
		print(读取)