def countVowels(s):
    if s == '':
        return 0
    else:
        smaller = countVowels(s[1:])
        print(smaller)
        if s[0] in "AEIOU":
            return smaller + 1
        else:
            return smaller

print(countVowels("ABC"))

# How the code works:

# countVowels('ABC') is called. Since s is not an empty string, proceed to the else block. Call the function countVowels('BC') is called, but the smaller variable does not store anything yet
# countVowels('BC') is called. Since s is not an empty string, proceed to the else block. Call the function countVowels('C') is called, but the smaller variable does not store anything yet
# countVowels('C') is called. Since s is not an empty string, proceed to the else block. Call the function countVowels('') is called.
# countVowels('') returns 0, and the base case is hit
# countVowels('C') is waiting for the variable smaller to store the return for countVowels('') which is 0. Now the code checks if s[0] ('C') is in 'AEIOU', which is false. countVowels('C') returns smaller (0)
# countVowels('BC') is waiting for the variable smaller to store the return for countVowels('C') which returned 0. Now the code checks if s[0] ('B') is in 'AEIOU', which is false. countVowels('BC') returns smaller (0)
# countVowels('ABC') is waiting for the variable smaller to store the return for countVowels('BC') which returned 0. Now the code checks if s[0] ('A') is in 'AEIOU', which is true. countVowels('ABC') returns 1 + smaller = 1

