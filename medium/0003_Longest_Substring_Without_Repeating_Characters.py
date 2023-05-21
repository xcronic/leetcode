import os
import console_color as console_color

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        
        string_start = 0
        result = 0
        map_char_to_index = {}
        for (index, char) in enumerate(s):
            if char in map_char_to_index:
                if map_char_to_index[char] >= string_start:
                    string_start = map_char_to_index[char] + 1
            result = max(result, index - string_start + 1)
            map_char_to_index[char] = index
        return result



def main():
    os.system('clear')
    solution = Solution()
    
    test_cases = [
        ("abobbobcv", 4),
        ("tmmzuxt", 5),
        ("aaaaaaaabcaaaa", 3),
        ("sadaghjkl",7),
        ("asdfgh",6),
        ("saddghjkl",6),
        ("sadaghjkl",7),
        ("saddas",3),
        ("sadadaf",3),
        ("", 0),
        ("d", 1),
        ("aa",1),
        ("ladfd",4)
    ]
    
    for test_case in test_cases:
        result = solution.lengthOfLongestSubstring(test_case[0])
        color = console_color.ConsoleColor.RED
        if test_case[1] == result:
            color = console_color.ConsoleColor.GREEN
        console_color.print_colored(f"\"{test_case[0]}\" => \"{result}\", expected result is \"{test_case[1]}\"", color)
            

if __name__ == "__main__":
    main()
