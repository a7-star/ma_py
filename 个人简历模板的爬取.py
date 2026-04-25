import requests
from lxml import etree
import os

if not os.path.exists('/storage/emulated/0/Download/简历模板'):
	os.mkdir('/storage/emulated/0/Download/简历模板')

if __name__=='__main__':
	url='https://sc.chinaz.com/jianli/zhengtao_%d.html'
	head={'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'}
	
	for urls in range(1,4):
		if urls==1:
			#首页页码url
			new_url='https://sc.chinaz.com/jianli/zhengtao.html'
		else:
			#对应页码url
			new_url=url % urls
		#发起请求
		response=requests.get(url=new_url,headers=head)
		page_text=response.text
		#print(response.text)
	
		#实例化etree对象
		tree=etree.HTML(page_text)
		a_href=tree.xpath('//div[@id="container"]/div/a/@href')
		#print(a_href)
	
		n=0
		for i in a_href:
			try:
				response_i=requests.get(url=i,headers=head)
				response_i.encoding='utf-8'
				i_text=response_i.text
				tree_i=etree.HTML(i_text)
				i_url=tree_i.xpath('//div[@id="down"]/div[2]/ul/li/a/@href')[0]
				#print(i_url)
				file_resp=requests.get(i_url,headers=head)
				data_i=file_resp.content
				
				#文件名
				name_url=tree_i.xpath('//div/h1/text()')[0]
				i_name=name_url+'.rar'			
				with open('/storage/emulated/0/Download/简历模板/'+i_name,'wb')as f:
					f.write(data_i)
					print(name_url,'下载成功！')
				n+=1
			except Exception as e:
				continue