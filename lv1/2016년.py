# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    day_counts = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    return days[((sum(day_counts[0:a]) + b) % 7) - 1]


# main 함수
def main():
    print(solution(5, 24))


# 프로그램 실행
if __name__ == "__main__":
    main()
