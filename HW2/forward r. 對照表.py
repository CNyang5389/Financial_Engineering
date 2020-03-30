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

