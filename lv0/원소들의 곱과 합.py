# https://school.programmers.co.kr/learn/courses/30/lessons/181929

def solution(num_list):
    m_result = multiple_all(num_list)
    p_result = plus_all_and_square(num_list)
    if m_result < p_result:
        return 1
    elif m_result > p_result:
        return 0


def multiple_all(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result


def plus_all_and_square(num_list):
    result = 0
    for num in num_list:
        result += num
    return result ** 2


# main function
def main():
    result = solution([5, 7, 8, 3])
    print(result)


# run program
if __name__ == "__main__":
    main()
