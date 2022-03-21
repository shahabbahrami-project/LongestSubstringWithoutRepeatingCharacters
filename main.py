#Longest Substring Without Repeating Character PRoblem
#By Shahab Bahrami
#March 2022

def LongestSubstring(s):
    if len(s)==0:
        return 0
    longest = 0
    left = 0
    seen = {}
    for right in range(len(s)):
        if (s[right] in seen.keys()):
            left = max(left,seen[s[right]] + 1)
            seen[s[right]] = right
        else:
            seen[s[right]] = right
            longest = max(longest, right-left+1)
    return longest
