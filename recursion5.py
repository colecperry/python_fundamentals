lis = [1,2,3,4]
def reverse(lis):
    if len(lis) == 1:
        return lis
    else:
        smaller = reverse(lis[1:])
        smaller.append(lis[0])
        return smaller

print(reverse([1,2,3]))

# How to code works:
# reverse([1,2,3]) is called, length is not 1 so enter else block, and reverse([2,3]) is called but smaller does not store anything since it has not returned anything yet
# reverse([2,3]) is called, length is not 1 so enter else block, and reverse ([3]) is called and we hit our base case (len(list) == 1 ) and we return lis which is [3]
# reverse([2,3]) is waiting for the smaller variable to return from reverse([3]), which returns [3]. We then append lis[0] to smaller and return smaller which is [3,2]
# reverse([1,2,3]) is waiting for the smaller variable to return from reverse([2,3]), which returns ([3,2]). We then append lis[0] to smaller and return smaller which is [3,2,1]