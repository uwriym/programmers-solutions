# https://school.programmers.co.kr/learn/courses/30/lessons/181928

def solution(num_list):
    even_list, odd_list = "", ""

    for num in num_list:
        if num % 2 == 0:  # even
            even_list += str(num)
        else:
            odd_list += str(num)

    return int(even_list) + int(odd_list)


# main function
def main():
    result = solution([5, 7, 8, 3])
    print(result)


# run program
if __name__ == "__main__":
    main()
