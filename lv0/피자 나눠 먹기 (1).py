# https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    return (n // 7) if (n % 7) == 0 else (n // 7) + 1


# main function
def main():
    result = solution(15)
    print(result)

# [1,2,3]
# run program
if __name__ == "__main__":
    main()
