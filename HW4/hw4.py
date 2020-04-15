#HW4
import math
print('It is a Europian put calculator.')
print('There is a stock which will pay two dividends,')
print('Assumption1: Current price of the stock is $75 and has a sigma of 0.35.')
print('Assumption2: The first dividends is $1 in 1 month, and the second one is $1 in 4 months.')
print('Assumption3: Interest rate= 6%. There is exercise with price $65 maturing in 6 months.')
dd=input('Are assumptions valid? If true, all of the settings are defaulted(y/n):') #如果是使用題目的預設數字就不用打字了
if dd=='n':
    print('Then please input the deatials of the stock and the call option.')
    #讀取輸入值，因為輸入值不一定是整數故使用float
    cp=float(input('請輸入 current price of the stock:'))
    s=float(input('請輸入 sigma:'))
    d1tinput=float(input('請輸入 time of paying of the first dividend(month):'))
    d1p=float(input('請輸入 paying of the first dividend:'))
    d2tinput=float(input('請輸入 time of paying of the second dividend(month):'))
    d2p=float(input('請輸入 paying of the second dividend:'))
    rinput=float(input('請輸入 r(%):'))
    x=float(input('請輸入 striking pirce:'))
    jinput=float(input('duration of maturing(month):'))
if dd=='y':
    cp=75
    s=0.35
    d1tinput=1
    d1p=1
    d2tinput=4
    d2p=1
    x=65
    jinput=6
    rinput=6
#整理輸入值成運算用的資訊
d1t=d1tinput/12
d2t=d2tinput/12
j=jinput/12
r=rinput/100
#運算
d=d1p*math.exp(-1*r*d1t)+d2p*math.exp(-1*r*d2t)
sh=cp-d
d1=(math.log(sh/x)+(r+0.5*s*s)*j)/s/(j**0.5)
d2=d1-s*(j**0.5)
n1=(1+math.erf(-1*d1/(2**0.5)))*.5
n2=(1+math.erf(-1*d2/(2**0.5)))*.5
p=x*math.exp(-1*r*j)*n2-sh*n1
c=cp-x-p
print('The value of the Europian put is $', round(p,2))
print('The value of the Europian call is $', round(c,2))
