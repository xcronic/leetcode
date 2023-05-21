import os
import console_color as console_color

class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
           return ""
        result = s[0]
        i=0
        while i < len(s):
            tail_len = len(s) - i
            if len(result) >= tail_len:
               return result
            j=i+1
            while j <= i + tail_len/2:
                if s[j] == s[j-1]:
                    candidate = get_candidate(s, j-1, j, i)
                    if len(candidate) > len(result):
                       result = candidate
                if j+1 < len(s) and s[j+1] == s[j-1]:   
                    candidate = get_candidate(s, j-1, j+1, i)
                    if len(candidate) > len(result):
                        result = candidate
                j=j+1
            i=i+1
        return result
                   
                
           
def get_candidate(s, i, j, hard_left):
    palyndrome = ""
    left = i
    right = j
    while left>=hard_left and right<len(s):
        if s[left] == s[right]:
            palyndrome = s[left:right+1]
            left = left - 1
            right = right + 1
        else:
            break
    return palyndrome


def main():
    os.system('clear')
    solution = Solution()
    
    test_cases = [
        ("saddas","saddas"),
        ("sadadaf","adada"),
        ("sadadas","sadadas"),
        ("saddaf","adda"),
        ("", ""),
        ("d", "d"),
        ("abals","aba"),
        ("ladfd","dfd"),
        ("ladfdl","dfd"),
        ("asfrg", "a"),
        ("aaaaaaabcaaaa", "aaaaaaa"),
        ("aaaaaaaabcaaaa", "aaaaaaaa"),
        ("bobbobcv", "bobbob"),
        ("asdfgg", "gg")
    ]
    
    for test_case in test_cases:
        result = solution.longestPalindrome(test_case[0])
        color = console_color.ConsoleColor.RED
        if test_case[1] == result:
            color = console_color.ConsoleColor.GREEN
        console_color.print_colored(f"\"{test_case[0]}\" => \"{result}\", expected result is \"{test_case[1]}\"", color)
            

if __name__ == "__main__":
    main()
