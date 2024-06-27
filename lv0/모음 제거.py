# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    answer = ''
    chars_to_check = 'aeiou'
    for c in my_string: answer += '' if c in chars_to_check else c
    return answer


# main function
def main():
    result = solution("nice to meet you")
    print(result)


# run program
if __name__ == "__main__":
    main()
