# https://school.programmers.co.kr/learn/courses/30/lessons/181912

def solution(intStrs, k, s, l):
    answer = []
    for intstr in intStrs:
        temp = int(intstr[s:s + l])
        if temp > k:
            answer.append(temp)

    return answer


# main 함수
def main():
    print(solution(["0123456789", "9876543210", "9999999999999"], 50000, 5, 5))


# 프로그램 실행
if __name__ == "__main__":
    main()
