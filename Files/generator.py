import time
myFile = open('1.txt', 'w')
#for cnt in range(10000):
#    myFile.write(str(cnt))
#    time.sleep(0.1)
#    myFile.seek(0)
#myFile.close()

def formula(t):
    return((-50) * (t**2) + (250 * t) + (-200))
#while(True):
    #for cnt in range(100):
    #    myFile.write(str(cnt))
    #    time.sleep(0.03)
    #    myFile.seek(0)
for cnt in range(0, 101, 3):
    myFile.write(str(formula(float(cnt)/10)))
    time.sleep(0.3)
    myFile.seek(0)

myFile.close()
print("Finish")