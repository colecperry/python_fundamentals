def SumDigits(n):
    '''Get the sum of digits for a non-negative integer n.
    Ex: 345 -> 12'''
    if n == 0:
        return 0
    else:
        smaller = SumDigits(int(n/10))
        return n%10 + smaller
    
print(SumDigits(345))

# SumDigits(345) is called. Since n does not equal 0, enter else block. SumDigits(int(345/10)) or SumDigits(34) is called and smaller does not store anything yet.
# SumDigits(34) is called and since n does not equal 0, enter else block. SumDigits(int(34/10)) or SumDigits(3) is called and smaller does not store anything yet.
# SumDigits(3) is called and since n does not equal 0, enter the else block. SumDigits(int(3/10)) or SumDigits(0) is called and we hit the base case and return 0 to SumDigits(3)
# SumDigits(3) stores 0 for smaller and returns 3%10 + 0 = 3 to SumDigits(34)
# SumDigits(34) stores 3 for smaller and returns 34%10 + 3 = 7 to SumDigits(345)
# SumDigits(345) stores 7 for smaller and returns 345%10 + 7 = 12 