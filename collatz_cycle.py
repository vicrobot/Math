def collatz(num):
    d_x = {'n':0,'ts':[]}
    if(num%2==0):
        num1 = num
        k = 0
        while(num1%2==0):
            k+=1
            num1 = num1/2
        d_x['ts'].append(k)
        num = num1
    n = 0
    num1 = num
    while num1 !=1:
        t = 0
        num2 = 3*num1+1
        while (num2%2==0):
            t+=1
            num2 = num2/2
        d_x['ts'].append(t)
        num1 = num2
        n += 1
    d_x['n'] += n
    return d_x

dict_nums = {}
init, end = 2, 50
for i in range(init, end):
    dict_nums[i] = collatz(i)

#from itertools import combinations_with_replacement as cwr
from math import floor

def plus1(l1,u):
    if l1[-1] + 1 > u:
        l1[-1] = 1
        return plus1(l1[:-1],u) + [1]
    else:
        l1[-1] += 1
        return l1

def cyclic_contra(n):
    u_bound = 1 + floor(0.5849625 * (n+1))  
    #print('u_bound', u_bound)
    ti_list = [1]*n
    while True:
        denom = 2**(sum(ti_list)) - 3**n
        #print(ti_list)
        if denom <= 0:
            if ti_list == len(ti_list)*[u_bound]:
                #print('broke here 1_',ti_list,u_bound)
                break
            #print('denom is -ve')
            try: ti_list = plus1(ti_list, u_bound)
            except:
                print('broke here 1_')
                break
        else:
            num = 0
            for i in range(0,n):
                num += 3**(i) * 2**sum(ti_list[:n-1-i])
            #print('num',num,'denom',denom)
            a = num/denom
            if a == 1:
                print('found_default')
                print(a, num, denom, ti_list, n, u_bound)
                pass
            elif a < 1:
                #print(ti_list,'smaller')
                try:
                    ti_list = plus1(ti_list[:-1]+[u_bound], u_bound)
                    continue
                except:
                    #print('broke here 1_')
                    break
            if a//1 == a and a!= 1:
                print("FOUND IT")
                print(a, num, denom, ti_list, n)
            else:
                #print('ti_list_after', ti_list)
                if ti_list == len(ti_list)*[u_bound]:
                    #print('broke here 2_')
                    break
                #print('ti_list_before', ti_list)
                try: ti_list = plus1(ti_list, u_bound)
                except: 
                    #print('broke here 2_')
                    break

for i in range(10,15):
    print(i)
    cyclic_contra(i)





"""
def cyclic_contra(n):
    u_bound = 1 + floor(0.5849625 * (n+1))  
    #print('u_bound', u_bound)
    ti_list = [1]*n
    while sum(ti_list[:n]) < n*u_bound:
        denom = 2**(sum(ti_list[:n])) - 3**n
        if denom <= 0:
            if counter >= u_bound:
                ti_list = plus1(ti_list,u_bound)
                counter = 1
            else:
                ti_list[-1] += 1
                counter += 1
            continue
        print(ti_list,u_bound)
        num = 0
        for i in range(0,n):
            num += 3**(i) * 2**sum(ti_list[:n-1-i])
        a = num/denom
        if a == 1: continue
        if a//1 == a:
            print("FOUND IT")
            print(a, num, denom, ti_list, n)
        if counter > u_bound:
            ti_list = plus1(ti_list,u_bound)
            counter = 1
        else:
            ti_list[-1] += 1
            counter += 1
"""            































































