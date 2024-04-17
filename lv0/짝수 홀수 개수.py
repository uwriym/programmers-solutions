# https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    odd, even = 0, 0
    for n in num_list:
        if n % 2 == 0: even += 1
        else: odd += 1
    return [even, odd]


# main 함수
def main():
    print(solution([1, 2, 3, 4, 5]))


# 프로그램 실행
if __name__ == "__main__":
    main()
