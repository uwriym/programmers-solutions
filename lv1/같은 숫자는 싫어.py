# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    result = [arr[0]]
    for e in arr:
        if result[-1] != e: result.append(e)
    return result


# main 함수
def main():
    print(solution([1,1,3,3,0,1,1]))


# 프로그램 실행
if __name__ == "__main__":
    main()
