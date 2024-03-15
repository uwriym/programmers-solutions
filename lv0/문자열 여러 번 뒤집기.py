# https://school.programmers.co.kr/learn/courses/30/lessons/181913

def solution(my_string, queries):
    string_list = list(my_string)
    for query in queries:
        new_list = string_list[query[0]:query[1] + 1]
        new_list.reverse()
        string_list[query[0]:query[1] + 1] = new_list

    return ''.join(string_list)


# main 함수
def main():
    print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))


# 프로그램 실행
if __name__ == "__main__":
    main()
