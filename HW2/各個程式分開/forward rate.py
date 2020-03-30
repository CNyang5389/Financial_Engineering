#Forward Rate
#讀取輸入值
import math
print('Enter the following details,while price must between 0-1')
t=float(input('Time due for the beginning of forward rate(years):'))
d=float(input('Duration of forward rate(years):'))
print('Price of',d,'year unit zero-coupon bond')
p=float(input(':'))
print('Price of',t+d,'year unit zero-coupon bond')
pt=float(input(':'))
#資料整理，排除無法計算的情況。若發生此情形，會出現警示並跳出程式
if p>=1 or pt>=1 or p<=0 or pt<=0:
    print('Price must between 0-1') 
    exit()
if pt > p:
    print('Price of bond in field 4 must less than which in field 3.')
    exit()
#計算與整理
f=(p/pt)**(1/d)-1
frate=f*100
fforce=100*math.log(f+1)
print(d,'year forward rate of interest:'"%.2f"%round(frate,2),'%')
print(d,'year forward force of interest:'"%.2f"%round(fforce,2),'%')
