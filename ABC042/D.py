import math
import sys
import itertools

def solve(begin, end):
    return math.factorial((end[0]-begin[0]) + (end[1] - begin[1])) / (math.factorial(end[0] - begin[0]) * math.factorial(end[1] - begin[1]))

def main():
    input_data = sys.stdin.read().split()
    start = [1,1]
    goal = [int(input_data[0]), int(input_data[1])]
    limited = [int(input_data[2]), int(input_data[3])]
    limited_ranges = [range(goal[0] - limited[0] + 1, goal[0]), range(1, limited[1])]

    total_pattern = solve(start, goal)
    limited_pattern = sum(solve(start, list(limited_point)) * solve(list(limited_point), goal) for limited_point in itertools.product(*limited_ranges))

    pattern = total_pattern - limited_pattern
    print(pattern % (10**9 + 7))


if __name__ == "__main__":
    main()