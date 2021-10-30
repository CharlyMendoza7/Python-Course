hrs = input("enter hours: ")
rate = input("enter rate: ")
fhrs = float(hrs)
frate = float(rate)

def xyz(pay,rate):
    mult = pay*rate
    ot = (pay-40.0)*(rate*0.5)
    s = mult+ot
    return s

if fhrs>40 :
    z = xyz(fhrs,frate)
else:
    z = fhrs*frate
print("Pay: ",z)
