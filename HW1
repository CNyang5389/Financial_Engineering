#讀取輸入值，因為輸入值不一定是整數故使用float
x=float(input('請輸入 本金(萬元):'))
t=float(input('請輸入 期數(年):'))
r=float(input('請輸入 年利率(%):'))
#整理輸入值成運算用的資訊，其中期數必須為整數，故取整數
xx=x*10000
rr=r/1200
tt=int(12*t)
#小數點到第三位
m=round(xx/tt,3)
#在這便分列期數，使用range列出1到tt期
ind=range(1,tt+1)
s=0
print('每月攤還本金(元)',m,'共',tt,'期')
print('期數',' 本金(元)','利息(元)','本金利息累計(元)')
#用for迴圈進行運算，算完第一期後用餘額繼續算第二期，直至末期
for i in ind:
    xxremain=xx-m*(i-1)
    rrr=round(xxremain*rr,3)
    s=s+m+rrr
    print(i,m,"%.3f"%rrr,"%.3f"%round(s,3))
 
