class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return s
        
        res, n = "", len(s)
        '''
        neat trick: swapcase converts all lowercase letters to uppercase letters
        and vice versa
        ref: https://www.w3schools.com/python/ref_string_swapcase.asp
        credit for this trick: ye15
        (https://leetcode.com/problems/longest-nice-substring/solutions/1074546/python3-brute-force-divide-and-conquer/)
        Note: I have solved most of the questions that i can confortably solve (~80 questions from the progress sheet). 
        For these ones, I ended up getting stuck so i get hints by looking at some of the solutions
        before i can solve them. 

        '''
        for i in range(n):
            for j in range(i):
                sub_str = s[j:i+1]
                if set(sub_str) == set(sub_str.swapcase()):
                    res = max(res, sub_str, key=len)
        return res