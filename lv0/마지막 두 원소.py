# https://school.programmers.co.kr/learn/courses/30/lessons/181927

def solution(num_list):
    last_num = num_list[-1]
    before_last_num = num_list[-2]
    if last_num > before_last_num:
        num_to_append = last_num - before_last_num
    else:
        num_to_append = last_num * 2
    num_list.append(num_to_append)
    return num_list


# main function
def main():
    result = solution([5, 2, 1, 7, 5])
    print(result)


# run program
if __name__ == "__main__":
    main()
