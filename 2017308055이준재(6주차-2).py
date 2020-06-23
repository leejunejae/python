import threading

class sum :
    sumName=''
    def __init__(self,name) :
        self.sumName=name

    def numsum(self,first,last) :
        result=0
        for i in range(first,last+1) :
            result+=i
        print("1+2+3.....+ ",last," = ", result)

sum1=sum('1000까지합')
sum2=sum('100000까지합')
sum3=sum('10000000까지합')

th1=threading.Thread(target=sum1.numsum(1,1000))
th2=threading.Thread(target=sum2.numsum(1,100000))
th3=threading.Thread(target=sum3.numsum(1,10000000))

th1.start()
th2.start()
th3.start()