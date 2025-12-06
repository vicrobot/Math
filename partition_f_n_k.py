
def f(n,k):
    if (n == 0) or (n==1):
        return 1
    a=n//k
    b=n%k
    if n<k:
        return p(n)

    
    res=p(b)

    for j in range(a):
        for i in range(1,k):
            n_temp = n-(j*k)-i
            k_temp = i
            if n_temp < k_temp:
                res += p(n_temp)
            else:
                res += f(n_temp,k_temp)
    return res


def p(n):
    res=1
    for i in range(1,n):
        temp = f(n-i,i)
        print(temp)
        res+= temp
    return res

print(p(8))

