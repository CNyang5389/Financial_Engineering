#HW2
import math
import numpy as np
#讀取輸入值，因為輸入值不一定是整數故使用float
print('The non-dividend paying stock is selling for $160, u=1.5, d=0.5, r=18.232% per period')
print('Ａ Eupean call on this stock with X=150, n=3')
print('If the input is not same as the default, the result will be differnt c')
dd=input('run the default settings(y/n):')
#此程式可算三期的call price
#為了讓如果是使用這題目的預設數字就不用打字了
if dd=='n':
    print('Let the period of European call "n" always equals 3')
    price=float(input('請輸入 price of non-dividend paying stock:'))
    u=float(input('請輸入 u :'))
    d=float(input('請輸入 d :'))
    rr=float(input('請輸入 r(%):'))
    x=float(input('請輸入 X of European call:'))
if dd=='y':
    price=160
    u=1.5
    d=0.5
    rr=18.332
    x=150
#整理輸入值成運算用的資訊
n=3
r=round(math.exp(rr/100),1)
p=(r-d)/(u-d)
q=1-p
#以矩陣畫樹枝圖
#K1為第一個樹枝圖(Binomial process for the stock price)
print('-0 means empty')
k1 = np.zeros((7,4))
"{0}".format(k1)
m=range(7)
i=range(4)
for j in i:
    for h in m:
        k1[h][j]=round(0.3-1/3,1)#處理空白區=-0
    k1[3-j][j]=price*(u**j)
    if j >=1:
        k1[5-j][j]=price*d*(u**(j-1))
    if j >=2:
        k1[7-j][j]=price*d*d*(u**(j-2))
    if j >=3:
        k1[9-j][j]=price*d*d*d*(u**(j-3))
print('Binomial process for the stock price')
print(k1)
#K2為第一個樹枝圖的機率(probabilities in parentheses)
k2 = np.zeros((7,4))
"{0}".format(k2)
for j in i:
    for h in m:
        k2[h][j]=round(0.3-1/3,1)#處理空白區=-0
    k2[3-j][j]=(p**j)
    if j >=1:
        k2[5-j][j]=q*(p**(j-1))*j
    if j >=2:
        k2[7-j][j]=q*q*(p**(j-2))*j
    if j >=3:
        k2[9-j][j]=q*q*q*(p**(j-3))
print('probabilities in parentheses')
print(k2)
#K3為第二個樹枝圖 (Binomial process for the call price)
k3 = np.zeros((7,4))
"{0}".format(k3)
for j in i:
    for h in m:
        k3[h][j]=round(0.3-1/3,1)#處理空白區=-0
z=range(0,8,2)
for t in z:
    k3[t][3]=k1[t][3]-x
    if (k1[t][3]-x)<0:
        k3[t][3]=0
e=range(1,7,2)
for ee in e:
    k3[ee][2]=round((k3[ee-1][3]*p+k3[ee+1][3]*q)/r,3)
s=range(2,6,2)
for ss in s:
    k3[ss][1]=round((k3[ss-1][2]*p+k3[ss+1][2]*q)/r,3)
k3[3][0]=round((k3[2][1]*p+k3[4][1]*q)/r,3)
print('Binomial process for the call price')
print(k3)
#計算call price
cv=round((k3[0][3]*k2[0][3]+k3[2][3]*k2[2][3]+k3[4][3]*k2[4][3]+k3[6][3]*k2[6][3])/(r**3),3)
print('call price is',cv,',and is also found as the PV of the expectef payoff at expiration.')
