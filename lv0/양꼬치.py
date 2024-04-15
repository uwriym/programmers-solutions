# https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    yang = n * 12000
    drink = k * 2000 - (n // 10) * 2000
    return yang + drink


# main 함수
def main():
    print(solution(10, 3))


# 프로그램 실행
if __name__ == "__main__":
    main()
