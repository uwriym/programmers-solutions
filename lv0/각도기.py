# https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(angle):
    if angle < 90: return 1
    elif angle == 90: return 2
    elif angle < 180: return 3
    elif angle == 180: return 4


# main 함수
def main():
    print(solution(70))


# 프로그램 실행
if __name__ == "__main__":
    main()
