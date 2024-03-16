# https://school.programmers.co.kr/learn/courses/30/lessons/181915

def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer
    # return ''.join([my_string[idx] for idx in index_list])


# main 함수
def main():
    print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))


# 프로그램 실행
if __name__ == "__main__":
    main()
