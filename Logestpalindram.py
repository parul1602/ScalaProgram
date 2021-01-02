str ="babad"
def longest_palindrome(s):
    def helper(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
             l -= 1  # decrement the left
             r += 1  # increment the right
        return s[l + 1:r]
    longest = " "
    for i in range(len(s)):
        tmp = helper(s, i, i)
        if len(tmp) > len(longest):
            longest = tmp
        tmp = helper(s, i, i+1)
        if len(tmp) > len(longest):
              longest = tmp
    return longest
print(longest_palindrome(str))