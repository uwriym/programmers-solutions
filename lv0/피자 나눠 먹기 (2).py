# https://school.programmers.co.kr/learn/courses/30/lessons/120815

def solution(n):
    for i in range(1, n + 1):
        if i * 6 % n == 0: return i


# main function
def main():
    result = solution(99)
    print(result)


# run program
if __name__ == "__main__":
    main()
