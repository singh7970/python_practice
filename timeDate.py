# "from datetime import datetime
# print(datetime.now())
# print(dir(datetime))"


import time
start=time.time()
for i in range(1,1000):
    print(i)
print((time.time()-start), "time")  