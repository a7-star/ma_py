import pandas as pd

#====读取数据====
r_csv = pd.read_csv('/storage/emulated/0/Download/e_commerce.csv')
print("数据读取成功！")
#增加读取列数
pd.set_option('display.max_columns', 500)
print('打印csv前五行：')
print(r_csv.head())

#====评估数据====
print('\n评估数据整齐度：')
print(r_csv.sample(10))
print('\n评估数据干净不度：')
print(r_csv.info())
#观察值得到结果Description,CustomerID变量存在缺失值，且InvoiceDate的数据类型应为日期，CustomerID的数据类型应该为字符串
print('\n评估缺失数据：')
print(r_csv[r_csv['Description'].isnull()])
#根据结果来看Description缺失数据，UnitPrice目测值为零
print(r_csv[(r_csv['Description'].isnull()) & (r_csv['UnitPrice']!=0)])
#缺失产品名的数据，它的产品单价也是零，说明这些行是无效数据需要删除
print('\n缺失ID观察值：')
print(r_csv[r_csv['CustomerID'].isnull()])
#客户ID缺失的数据，其他并没有缺失，并不影响数据判断
print('\n评估重复数据：')
print(r_csv.duplicated().sum())
print('\n评估不一致数据：')
print((r_csv['Country'].value_counts()))
#从国家变量值来看，“USA”、“United States”均表示美国，三个UK表示英国，需要对值进行统一
print('\n评估无效或错误数据：')
print(r_csv.describe())
#用户ID数据要改成字符串，Quantity、UnitPrice存在负数
print('\n先筛选Quantity为负数的观察值，进一步评估：')
print(r_csv[r_csv['Quantity']<=0])
#Quantity为负数的观察值，InvoiceNo似乎均以c开头，表示退单
print('\n验证上一猜想：')
print(r_csv[(r_csv['Quantity']<=0) & (r_csv['InvoiceNo'].str[0]!='C')])
#猜想错误，且观测到UnitPrice为0
print('\n增加条件验证：')
print(r_csv[(r_csv['Quantity']<=0) & (r_csv['InvoiceNo'].str[0]!='C') & (r_csv['UnitPrice']!=0)])
#Quantity为负数的观察值都要删除
print('\n继续验证猜想：')
print(r_csv[(r_csv['UnitPrice']<=0)])
#UnitPrice<=0数据为坏账调整也需要删除

#====清理数据====
#为了区分原始数据和清理数据，新建变量w_csv
w_csv = r_csv.copy()
print('\n打印前几行：')
print(w_csv.head())
#改InvoiceDate数据类型为日期
w_csv['InvoiceDate'] = pd.to_datetime(w_csv['InvoiceDate'])
print('\n查看修改InvoiceDate数据类型为日期的结果：')
print(w_csv['InvoiceDate'])
#改CustomerID数据类型为字符串
w_csv['CustomerID'] = w_csv['CustomerID'].astype(str)
print('\n查看修改CustomerID数据类型为字符串的结果：')
print(w_csv['CustomerID'])
#结尾出现了.0
#删除“.0”
w_csv['CustomerID'] = w_csv['CustomerID'].str.slice(0, -2)
print('\n查看修改删除“.0”结果：')
print(w_csv['CustomerID'])
#把Description存在无意义的缺失值删了
w_csv = w_csv.dropna(subset=['Description'])
print('\n查看修改无意义的缺失值的删除：')
print(w_csv.isnull().sum())
#把Co#untry变量值“USA”等全替换为“United States”
w_csv['Country'] = w_csv['Country'].replace({'USA': 'United States',
	'UK': 'United States',
	'U.K.': 'United States',
})
print("\n验证USA/UK/U.K.是否被全部替换：")
print("USA剩余数量：", len(w_csv[w_csv['Country'] == 'USA']))
print("UK剩余数量：", len(w_csv[w_csv['Country'] == 'UK']))
print("U.K.剩余数量：", len(w_csv[w_csv['Country'] == 'U.K.']))
print("替换后United States总数：", len(w_csv[w_csv['Country'] == 'United States']))
#把Quantity变量值为负数的观察值删除，并检查
w_csv = w_csv[w_csv['Quantity'] >= 0]
print('\n验证Quantity观察值小于0的个数是不是为0了：')
print(len(w_csv[w_csv['Quantity'] < 0]))
#把UnitPrice变量值为负数的观察值删除，并检查
w_csv = w_csv[w_csv['UnitPrice'] >= 0]
print('\n验证UnitPrice观察值小于0的个数是不是为0了：')
print(len(w_csv[w_csv['UnitPrice'] < 0]))

#====保存清理后的数据====
w_csv.to_csv('e_commerce_cleaned.csv', index=False)
print('\n读取保存清理后的数据：')
print(pd.read_csv('e_commerce_cleaned.csv').head)
