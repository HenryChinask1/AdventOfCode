class Solution:
    def clearStars(self, s: str) -> str:
        cnt = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            #print(cnt)
            if c != '*':
                cnt[ord(c) - ord('a')].append(i)
            else:
                #print(arr)
                for j in range(26):
                    #print(arr,'\n',cnt)
                    if cnt[j]:
                        print(cnt[j])
                        arr[cnt[j].pop()] = '*'
                        break
        return ''.join(c for c in arr if c != '*')

s = Solution()
s.clearStars('aa*ba*')