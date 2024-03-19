# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    return s[len(s)//2-1:len(s)//2+1] if len(s)%2 == 0 else s[len(s)//2:len(s)//2+1]


# main 함수
def main():
    print(solution("qwerty"))


# 프로그램 실행
if __name__ == "__main__":
    main()
