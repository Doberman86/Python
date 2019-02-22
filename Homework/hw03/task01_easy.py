def my_round(number, ndigits):
    int_ndigits = int(ndigits)
    degree = pow(10,int(ndigits))
    mul =  number*degree
    res = int(mul)
    ost = mul-res
    # print(number,mul,res,ost)
    if not (abs(ost) < 0.5):
        if res>0: res+=1
        else: res-=1
    return res/degree



my_round(2.1234567, 5)