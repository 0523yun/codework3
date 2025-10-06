ID=str(eval(input("请输入身份证号：")))
year=ID[6:10]
month=ID[10:12]
day=ID[12:14]
print("您的出生日期是：{}年{}月{}日".format(year,month,day))