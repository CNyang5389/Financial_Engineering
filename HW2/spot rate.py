import math
#讀取輸入值
print('Enter the following details,while price must between 0-1')
d=float(input('duration of spot rate(years):'))
print('Price of',d,'year unit zero-coupon bond')
p=float(input(':'))

if p>=1 or p<=0:
    print('Price must between 0-1') 
    exit()
sr=(p**(-1/d)-1)
sfr=math.log(1+sr)
print(d,'year spot rate of interest:'"%.2f"%round(sr*100,2),'%')
print(d,'year spot force of interest:'"%.2f"%round(sfr*100,2),'%')
