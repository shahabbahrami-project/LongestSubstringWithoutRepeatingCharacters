#Longest Substring Without Repeating Character PRoblem
#By Shahab Bahrami
#March 2022

def LongestSubstring(s):
    if len(s)==0:
        return 0
    longest = 0
    left = 0
    right = 0
    for left in range(len(s)):
        temp = 0
        seen = {}
        for right in range(left,len(s)):
            if (s[right] in seen.keys()) or right==len(s)-1:
                longest = max(temp,longest)
                # print(longest)
                break
            else:
                seen[s[right]]=1
                temp+=1
        # print(seen)

    return longest


s='abcdefgabcbddbacdef'
result=LongestSubstring(s)
print(result)
