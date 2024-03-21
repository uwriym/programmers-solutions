# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    temp = []
    for num in arr:
        if num % divisor == 0: temp.append(num)
    temp.sort()
    return temp if len(temp) != 0 else [-1]


# main 함수
def main():
    print(solution([5, 9, 7, 10], 5))


# 프로그램 실행
if __name__ == "__main__":
    main()
