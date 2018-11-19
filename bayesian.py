import numpy as np
import matplotlib.pyplot as plt
import random as ra
import math

def fac(n):
    fac=1
    for i in range(1, n+1):
        fac*= i
    return fac

def combi(m, n):
    combi= fac(m)/ (fac(m-n)* fac(n))
    return combi

c10_2= combi(10,2)

head = 0.0
tail = 1.0
like = [0.0]*11
for i in range(11):
    like[i] = c10_2* head **2 * tail **8;
    head += 0.1
    tail -= 0.1

max_like= max(like)
for i in range(11):
    if like[i]== max_like:
        print "MLE=", i*0.1

ho = np.arange(0.0, 1.1, 0.1)
plt.bar(ho, like, width = 0.08)
plt.title('likelihood')
plt.show()

print "\n(1) assumption a:"
pr_a= [1.0/11.0]*11
pos_a=[0.0]*11
mar_a=0.0
for i in range(11):
    mar_a+= pr_a[i]*like[i]
for i in range(11):
    pos_a[i]= pr_a[i]*like[i]/mar_a
#print pos_a

max_a= max(pos_a)
for i in range(11):
    if pos_a[i]==max_a:
        print "MAP=", i*0.1

plt.bar(ho, pr_a, width = 0.08)
plt.title('prior of (a)')
plt.ylim(0, 0.2)
plt.show()

plt.bar(ho, pos_a, width = 0.08)
plt.title('posterior of (a)')
plt.show()


print "\nassumption b:"
pr_b= [0.01, 0.01, 0.05, 0.08, 0.15, 0.4, 0.15, 0.08, 0.05, 0.01, 0.01]
pos_b=[0.0]*11
mar_b=0.0
for i in range(11):
    mar_b+= pr_b[i]*like[i]
for i in range(11):
    pos_b[i]= pr_b[i]*like[i]/mar_b
#print pos_b

max_b= max(pos_b)
for i in range(11):
    if pos_b[i]==max_b:
        print "MAP=", i*0.1

plt.bar(ho, pr_b, width = 0.08)
plt.title('prior of (b)')
plt.show()

plt.bar(ho, pos_b, width = 0.08)
plt.title('posterior of (b)')
plt.show()



print "\n(2)"
entro = []
likee = np.ones(11)
pr    = np.ones(11) / 11
head  = np.arange(11) * 0.1
tail  = 1 - np.arange(11) * 0.1
for i in range(5):
    for k in range(10):
        he=0
        ta=0
        for j in range(10):
            if ra.randint(0, 1)==1:
                he+=1
            else:
                ta+=1
       # print ("head= {0}, tail= {1}".format(he, ta))
        likeeold = likee
        likee    = np.power(head, he) * np.power(tail, ta)
        # for h in range(11):
        #     likee[h]= head** he * tail**ta
        #     head+=0.1
        #     tail-=0.1
        likee *= likeeold
        # for n in range(11):
        #     likee[n]*= likeeold[n]
        

        pos  = likee * pr
        pos /= np.sum(pos)
        # pos= [0.0]*11
        # mar= 0.0
        # for o in range(11):
        #     mar+= pr[o]*likee[o]
        # for m in range(11):
        #     pos[m] = pr[m] * likee[m] / mar
        #     # no need for (try, except)
        #     if not pos[m]:
        #         pos[m]+=0.00000001
        #     summ = [0]*11
        #     summ[m] = -(pos[m]* math.log(pos[m], 2))
        # entro[i*10+k]= sum(summ)
        entro += [-(pos*np.log2(pos+0.00000001)).sum()]

    plt.bar(ho, pos, width = 0.08)
    plt.show()

#print(entro)
plt.plot(range(50), entro)
plt.show()
