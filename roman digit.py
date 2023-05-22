class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        total = my_dict[s[0]]
        for i in range(1, len(s)):
            if my_dict[s[i]] >= my_dict[s[i - 1]]:
                total += my_dict[s[i]]
            else:
                total -= my_dict[s[i]]
        return total


print(Solution.romanToInt(self="MCMXCIV", s="MCMXCIV"))
#1994