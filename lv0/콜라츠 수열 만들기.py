# https://school.programmers.co.kr/learn/courses/30/lessons/181919

def solution(n):
    answer = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else (3 * n) + 1
        answer.append(n)
    return answer


# main function
def main():
    result = solution(10)
    print(result)


# run program
if __name__ == "__main__":
    main()
