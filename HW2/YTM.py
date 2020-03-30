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
