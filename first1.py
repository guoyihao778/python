# def calculate_BMI(weight,height):
#     BMI=weight/height**2
#     if BMI<+18.5:
#         category="偏瘦"
#     elif BMI<=25:
#         category="正常"
#     elif BMI<=30:
#         category="偏胖"
#     else:
#         category="肥胖"
#     print(f"您的BMI分类为:{category}")
#     return BMI
# result=calculate_BMI(60,1.76)
# print(result)

# class CuteCat:
#     def __init__(self,name,age,genfer,color):
#         self.name=name
#         self.age=age
#         self.gender=genfer
#         self.color=color
# cat1=CuteCat("xinxin",3,"male","blue")
# print(cat1.name)
# print(cat1.age)
# print(cat1.gender)
# print(cat1.color)

# =================================================对象及其类型=================================================
# print("100 is",type(100))#整型int
# print("3.14 is",type(3.14))#浮点型float
# print("5+2j is",type(5+2j))#复数型complex
# print("True and False are",type(False))#布尔型bool
# print("\'I love Python.\' is",type('I love Python.'))#字符串str
# print("[1,2,3]",type([1,2,3]))#列表list[]
# print("(1,2,3)",type((1,2,3)))#元组tuple()
# print("{1,2,3}",type({1,2,3}))#可变集合set
# print("frozenset({1,2,3}) is",type(frozenset({1,2,3})))#不可变集合frozenset
# print("{'name':'Tom','age':18}",type({'name':'Tom','age':18}))#字典dict{}

# =================================================变量与赋值=================================================
#1
# name="XiaoMing"
# age=18
# height=175
# print("姓名",name)##!!!! ','表示print分别把两边内容表示，会自动转换为str;而‘+’的两边必须为同一类型
# print("年龄",age)
# print("身高",height)
# 2
# value=60
# print("第1次赋值",value)
# value=80
# print("第2次赋值",value)
# value=90
# print("第3次赋值",value)
# 3
# x=13.1
# y=0.2
# sum=x+y
# sub=x-y
# mul=x*y
# div=x/y
# print("x+y=",sum)
# print("x-y=",sub)
# print("x*y=",mul)
# print("x/y=",div)
# 4
# a,b,c,d=1,2,3,4
# a+=1
# b-=3
# c*=4
# d/=5
# print(a,b,c,d)
# 5
# a,b,c,d,e,f=111,32,45,325,66,21
# print(a,b,c,d,e,f)
# name,age,height,dict="xiaoming",18,175,{"1":"a","2":"b","3":"c","4":"d","5":"e"}
# print(name,age,height,dict)
# x=y=z=11#不能写成x,y,z=11,只有一个数字11，不能拆成三份
# print(x,y,z)
# 6
# x,y=9999,1111
# print("交换前",x,y)
# x,y=y,x
# print("交换后",x,y)
# 7
# PI=3.1415926
# r=3
# area=PI*r**2
# print("圆的半径为",r)
# print("圆的面积为",area)
# 8
# # 获取用户输入并赋值给变量
# user_name = input("请输入你的名字：")
# user_age = int(input("请输入你的年龄："))  # 转成整数
# user_gender=input("请输入你的性别：")
# print("你好，", user_name)
# print("明年你就", user_age + 1, "岁啦")
# print("你是个"+user_gender+"孩儿")
# =================================================运算符和表达式=================================================
