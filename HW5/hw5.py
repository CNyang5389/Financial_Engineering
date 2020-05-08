import QuantLib as ql
import numpy as np
import matplotlib.pyplot as plt
import math
print("This is a European option calculator. Num. of simulation paths= 500.")
S0=float(input("Please enter the current stock price:"))
strikep=float(input("Please enter the strike price:"))
irfree=float(input("Please enter the risk-free interest rate (%):"))
iforward_rate=float(input("Please enter the forward rate(%):"))
length=float(input("Please enter the duration of the option (year):"))
a=float(input("Please enter the speed for interest rate to return to mean (a of HW model):"))
sigma=float(input("Please enter the volatitlity of interest (sigma of HW model):"))
#整理數據並設定必要數值
forward_rate=iforward_rate/100
rfree=irfree/100
timestep = 360
tt=int(timestep*length)
day_count = ql.Thirty360()
todays_date = ql.Date(12, 5, 2020)
num_paths = 500
vol=0.01
dt=0.01
#套用並微調pdf補充之HW model
ql.Settings.instance().evaluationDate = todays_date
sc = ql.FlatForward(todays_date, ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
sch = ql.YieldTermStructureHandle(sc)
p = ql.HullWhiteProcess(sch, a, sigma)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(tt, ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(p, length, tt, rng, False)
def generate_paths(num_paths, tt):
    arr = np.zeros((num_paths, tt+1))
    for i in range(num_paths):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr
time, paths = generate_paths(num_paths, tt)
#套用蒙地卡羅
st = np.zeros((num_paths,tt+1))
st[:,0] = np.log(S0)
for n in range(tt):
    rr=np.random.standard_normal(num_paths)
    st[:,n+1] = st[:,n] + (paths[:,n+1]-0.5*vol**2)*dt+vol*(dt**0.5)*rr
st_final = np.exp(st[:, -1])
#計算call price &put price
icp = np.zeros(num_paths)
for n in range(num_paths):
    if st_final[n]>=strikep:
        icp[n]=st_final[n]-strikep
mcp=np.sum(icp)/num_paths
cp=mcp*np.exp(-rfree*length)
print("call price=",round(cp,3))
ipp = np.zeros(num_paths)
for n in range(num_paths):
    if st_final[n]<=strikep:
        ipp[n]=strikep-st_final[n]
mpp=np.sum(ipp)/num_paths
pp=mpp*np.exp(-rfree*length)
print("put price=",round(pp,3))
#畫圖
for i in range(num_paths):
    plt.title("Short rate trace")
    plt.plot(time, paths[i, :], lw=1, alpha=1)
plt.show()
for i in range(num_paths):
    plt.title("price trace")
    plt.plot(time, st[i, :], lw=1, alpha=1)
plt.show()


