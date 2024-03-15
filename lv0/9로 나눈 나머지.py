# https://school.programmers.co.kr/learn/courses/30/lessons/181914

def solution(number):
    # return int(number) % 9
    return sum(map(int, number)) % 9


# main 함수
def main():
    print(solution("123"))


# 프로그램 실행
if __name__ == "__main__":
    main()
