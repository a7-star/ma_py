import requests
import re
import os
#爬取豆瓣的所有图片
if __name__=='__main__':
	
	headers = {
	'User-Agent':'Mozilla/5.0 (Linux; Android 16; 2407FRK8EC Build/BP2A.250605.031.A3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.7151.115 Mobile Safari/537.36',
	'Referer': 'https://movie.douban.com/top250'
	}
	
	#创建一个文件夹，保存所有图片
	if not os.path.exists('./豆瓣'):
		os.mkdir('./豆瓣')
	#设置一个通用的url模板
	url='https://movie.douban.com/top250?start=%d&filter='
	#循环页码
	for pageNum in range(0,51,25):
		#对应页码的url
		new_url = url % pageNum
		
		#使用通用爬虫对url对应的一整张页面进行爬取
		page_text = requests.get(url=new_url,headers=headers).text
		
		#验证反爬
		#print(page_text[:500])

		ex = r'<img width="100" alt=.*? src="(.*?)">'
		img_src_list = re.findall(ex,page_text,re.S) #re.S单行匹配
		print(img_src_list)
		for i in img_src_list:
			
			#请求到了图片的二进制数据
			img_data = requests.get(url=i,headers=headers).content
			#生成图片名称
			img_name = i.split('/')[-1]
			imgPath = './豆瓣/'+img_name
			#图片存储的路径
			with open(imgPath,'wb')as f:
				f.write(img_data)
				print(img_name,'下载成功！')