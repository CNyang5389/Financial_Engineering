#HW2
#-------------
#YTM
#當期數比較多時會跑比較久
#輸入需要用到的函數與套件
import math
from sympy import symbols,solve
#讀取輸入值
bp=float(input('請輸入 Current Bond Price:'))
pv=float(input('請輸入 Bond Par Value:'))
cc=float(input('請輸入 Bond Coupon Rate(% p.a.)'))
y=float(input('請輸入 Year to maturity'))
m=float(input('請輸入 每年支付次數(即annually=1,semi-annually=2,quarterly=4'))
#整理輸入值成運算用的資訊
c=cc/100*pv/m
n=m*y
#方程式計算
x=symbols('x',real=True,positive=True)#設定條件避免出現0或虛數根
k=(solve(bp*((x+1)**(n+1))-(bp+c)*((x+1)**n)-pv*(x+1)+c+pv,x))
[kk]=k#浮點化
ytm="%.4f"%round(100*kk,4)
print('Yield to Maturity(YTM)=',ytm,'%')
#-------------
#Spot Rate
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
#-------------
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
#-------------
#Forward Rate對照表
import math
import numpy as np
#讀取輸入值，因為輸入值不一定是整數故使用float
y=float(input('請輸入 年限(years):'))
x=float(input('請輸入 期長(一年=1,半年=0.5,每季=0.25)'))
ibp=input('請輸入各期Bond price，以,隔開:').split(',')
ipv=input('請輸入各期par value，以,隔開:').split(',')
#整理輸入值成運算用的資訊
bp=['100']+ibp
pv=['100']+ipv
n=int(y/x)
nr=range(1,n+2)
#以矩陣列成表格形式
k = np.zeros( (n+2, n+2) )
"{0}".format(k)
#分兩層回圈計算
for i in nr:
    ii=i-1
    k1=float(bp[ii])
    k2=float(pv[ii])
    for m in nr:
        mm=m-1
        b1=float(bp[mm])
        b2=float(pv[mm])
        k[0][m]=mm#處理座標
        k[i][0]=ii#處理座標
        if m<i:
            k[i][m]=round(0.3-1/3,1)#處理空白區=-0
        if m>i:
            crp=float(bp[mm])/float(pv[mm])
            #forward rate計算，丟入矩陣
            k[i][m]=round(100/x*(((k1/k2)/crp)**(1/(m-i))-1),4)         
print(k)
print('-0 means empty')
