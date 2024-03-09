# https://school.programmers.co.kr/learn/courses/30/lessons/181920

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num + 1):
        answer.append(i)
    return answer
    # return list(range(start_num, end_num + 1))


# main function
def main():
    result = solution(3, 10)
    print(result)


# run program
if __name__ == "__main__":
    main()
