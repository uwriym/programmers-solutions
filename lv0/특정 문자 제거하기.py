# https://school.programmers.co.kr/learn/courses/30/lessons/120826

import re

def solution(my_string, letter):
    return re.sub(letter, "", my_string)


# main 함수
def main():
    print(solution("abcdef", "f"))


# 프로그램 실행
if __name__ == "__main__":
    main()
