# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    num_list = list(x for x in range(0, n + 1))
    even_num_list = list(x * 2 for x in range(0, n // 2 + 1))
    return list(set(num_list) - set(even_num_list))


# main function
def main():
    result = solution(10)
    print(result)

# [1,2,3]
# run program
if __name__ == "__main__":
    main()
