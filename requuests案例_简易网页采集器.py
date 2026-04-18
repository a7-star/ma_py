import requests

#UA伪装：User-Agent
headers={'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'} 

if __name__=='__main__':
	url='https://wap.sogou.com/web/searchList.jsp'
	#处理url携带的参数：封装到字典中
	kw=input('输入：')
	params={
		'keyword':kw
	}
	#对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
	response=requests.get(url,params=params,headers=headers)
	
	page_text=response.text
	#文件命名
	fileName=kw+'.html'
	with open (fileName,'w',encoding='utf-8') as f:
		f.write(page_text)
	print(fileName,'打印成功！')