class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def countAtMost(k):
            vowels = set('aeiou')
            ans = 0
            left = 0
            count = {}
            
            for right, char in enumerate(word):
                if char not in vowels:
                    count = {}
                    left = right + 1
                    continue
                
                count[char] = count.get(char, 0) + 1
                
                while len(count) > k:
                    count[word[left]] -= 1
                    if count[word[left]] == 0:
                        del count[word[left]]
                    left += 1
                
                ans += (right - left + 1)
            return ans

        return countAtMost(5) - countAtMost(4)