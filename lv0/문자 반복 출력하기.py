# https://school.programmers.co.kr/learn/courses/30/lessons/120825

solution = lambda my_string, n: "".join(list(i * n for i in my_string))


# main 함수
def main():
    print(solution("hello", 3))


# 프로그램 실행
if __name__ == "__main__":
    main()
