# https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    answer = []
    for c in my_string:
        try:
            answer.append(int(c))
        except:
            next
    answer.sort()
    return answer

# short
# return sorted([int(c) for c in my_string if c.isdigit()])

# main function
def main():
    result = solution("hi12392")
    print(result)

# [1,2,3]
# run program
if __name__ == "__main__":
    main()
