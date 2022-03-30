
import csv


header=["class","name","sex","height","year"]
rows=[{"class":"1","name":"xiao|ming","sex":"male","height":"168","year":"23"},
      {"class":"1","name":"xiao|hong","sex":"female","height":"162","year":"22"},
      {"class":"2","name":"xiao|zhang","sex":"female","height":"163","year":"21"},
      {"class":"2","name":"xiao|li","sex":"male","height":"158","year":"21"}]

with open("C:/Users/29507/OneDrive/桌面/测试.csv","w",encoding="utf-8",newline="")as m:
    my_m=csv.DictWriter(m ,header )
    my_m.writeheader()
    my_m.writerows(rows)



csv.register_dialect('mydialect',delimiter='|',quoting=csv.QUOTE_ALL)#用来定义dialect
with open("C:/Users/29507/OneDrive/桌面/测试.csv","r") as  f:
    
    r=csv.reader(f,"mydialect")
    for row in r:
        print(",".join(row))
csv.unregister_dialect('mydialect')#用来注销自定义的dialect

with open("C:/Users/29507/OneDrive/桌面/测试.csv","r") as  f:
    
    r=csv.reader(f)
    for row in r:
        print(row)
