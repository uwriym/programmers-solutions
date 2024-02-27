# https://school.programmers.co.kr/learn/courses/30/lessons/181931?language=python3

def solution(a, b, included):
    result = 0
    time = 0
    for i in included:
        if i:
            result += (a + (b * time))
        time += 1

    return result


# main 함수
def main():
    print(solution(7, 1, [False, False, False, True, False, False, False]))


# 프로그램 실행
if __name__ == "__main__":
    main()
