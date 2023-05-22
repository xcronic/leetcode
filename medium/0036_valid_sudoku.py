import os
import console_color as console_color

class Solution(object):
    def isValidSudoku(self, board):
        value_to_appearances_map = {}
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                value = int(board[i][j])
                if value < 1 or value > 9:
                    return False
                if value in value_to_appearances_map:
                    if is_valid(value_to_appearances_map[value], i, j):
                        value_to_appearances_map[value].append((i, j, calc_box(i, j)))
                    else:
                        return False
                else:
                    value_to_appearances_map[value] = [(i, j, calc_box(i,j))]
        return True
    
def is_valid(value_appearances, i, j):
    for (x,y, box) in value_appearances:
        if x == i:
            return False
        if y == j:
            return False
        if box == calc_box(i,j):
            return False
    return True

def calc_box(i,j):
    return i/3 * 10+j/3
    

def main():
    os.system('clear')
    solution = Solution()
    
    test_cases = [
        ([[".",".",".","9",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".","3",".",".",".",".",".","1"],
          [".",".",".",".",".",".",".",".","."],
          ["1",".",".",".",".",".","3",".","."],
          [".",".",".",".","2",".","6",".","."],
          [".","9",".",".",".",".",".","7","."],
          [".",".",".",".",".",".",".",".","."],
          ["8",".",".","8",".",".",".",".","."]], False),

        ([[".",".","4",".",".",".","6","3","."],
          [".",".",".",".",".",".",".",".","."],
          ["5",".",".",".",".",".",".","9","."],
          [".",".",".","5","6",".",".",".","."],
          ["4",".","3",".",".",".",".",".","1"],
          [".",".",".","7",".",".",".",".","."],
          [".",".",".","5",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."]], False),

        ([["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]], False),

        ([["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]], True)
    ]
    
    for test_case in test_cases:
        result = solution.isValidSudoku(test_case[0])
        color = console_color.ConsoleColor.RED
        if test_case[1] == result:
            color = console_color.ConsoleColor.GREEN
        console_color.print_colored(f"\"{test_case[0]}\" => \"{result}\", expected result is \"{test_case[1]}\"", color)
            

if __name__ == "__main__":
    main()
