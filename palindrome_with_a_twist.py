"""
You are given a string S, you are allowed to swap atmost one character in the string between any two characters in the string.

Determine whether it is possible to transform the string to palindrome using recursion

"""

def checkSwappedPalindrome(left,right,s,index_mismatch):
    #print(index_mismatch)
    #Eprint(f"left: {left} and right: {right}")
    if left >= right:
        if len(index_mismatch) == 0:
            return True
        elif len(index_mismatch) == 1:
            first = index_mismatch[0]
            if s[first[0]] == s[len(s)//2] or s[first[1]] == s[len(s)//2]:
                return True
            return False
        elif len(index_mismatch) == 2:
            first = index_mismatch[0]
            second = index_mismatch[1]
            if s[first[0]] == s[second[1]] and s[first[1]] == s[second[0]] or \
            s[first[0]] == s[second[0]] and s[first[1]] == s[second[1]]:
                return True
            return False
    
    if s[left] != s[right]:
        #print("inside the left != right")
        index_mismatch.append((left,right))
        if len(index_mismatch) > 2:
            return False
    #print(index_mismatch)
    return checkSwappedPalindrome(left+1,right-1,s,index_mismatch)
    
def canBecomePalindrome(s):
    index_mismatch = []
    return checkSwappedPalindrome(0,len(s)-1,s,index_mismatch)
            
if __name__ == "__main__":
    s = input()
    print("true" if canBecomePalindrome(s) else "false")