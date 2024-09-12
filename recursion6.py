def isPalindrome(s):
    ''' Returns True if the input string "s" is a palindrome'''
    if len(s) <= 1:
        return True
    else:
        smaller = isPalindrome(s[1:len(s)-1])
        return s[0] == s[len(s)-1] and smaller

print(isPalindrome('abba'))

# isPalindrome('abba') is called. Since length is not equal to 1, enter else block. Call isPalindrome('bb') but smaller does not store any value yet.
# isPalindrome('bb') is called. Since length is not equal to 1, enter else block. Call isPalindrome('b') and smaller returns True for isPalindrome('bb') call block. 
# Back up the stack: isPalindrome('bb') call block stores true for smaller and True and True which equals True for it's return statement
# isPalindrome('abba') is waiting for smaller to return from isPalindrome('bb'), which returned True. isPalindrome('abba') returns True and True which equals true 