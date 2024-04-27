# https://school.programmers.co.kr/learn/courses/30/lessons/120822

def solution(my_string):
    return ''.join(list(my_string[i] for i in range(len(my_string) - 1, -1, -1)))

# main function
def main():
    result = solution("jaron")
    print(result)


# run program
if __name__ == "__main__":
    main()
