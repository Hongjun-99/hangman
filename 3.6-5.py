'''
fruit=['Apple','Orange','Pear']
fruit.append('Banana')
fruit.append('Peach')
print(fruit)
'''
'''
random=list()
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)
'''
'''
colors=["blue","green","yellow"]

item=colors.pop()
print(item)
print(colors)
if "green" in colors:
    print(True)

if "black" not in colors:
    print(True)
print(len(colors))
'''
'''
colors=["purple","orange","green"]
guess = input("猜一个颜色：")
if guess in colors:
    print("回答正确！")
else:
    print("猜错了，请重试1")
'''
#元组
'''
dys=("1984","Brave New World","Fahrenheit 451")
dys[1]="Handmaid's Tale"
print(dys)
'''

#字典
'''
books={"A":"1","B":"2","C":"3"}
del books["A"]
print(books)

'''
my_dict={"1":"A",
         "2":"B",
         "3":"C",
         "4":"D"
         }
n=input("请输入一个数字：")
if n in my_dict:
    dict=my_dict[n]
    print(dict)
else:
    print("没有发现！")
