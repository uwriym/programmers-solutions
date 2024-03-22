# https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    if a > b: a, b = b, a 
    return sum(range(a, b + 1))


# main 함수
def main():
    print(solution(3, 5))


# 프로그램 실행
if __name__ == "__main__":
    main()
