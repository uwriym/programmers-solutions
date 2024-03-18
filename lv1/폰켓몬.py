# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    return int(len(set(nums)) if len(set(nums)) < len(nums) / 2 else len(nums) /2)


# main 함수
def main():
    print(solution([3,1,2,3]))


# 프로그램 실행
if __name__ == "__main__":
    main()
