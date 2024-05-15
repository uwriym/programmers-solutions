# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    num_list = s.split(' ')
    result = 0
    buffer = None
    for i  in num_list:
        if i == 'Z' and buffer != None:
            result -= int(buffer)
        else:
            result += int(i)
            buffer = i
    return result


# main function
def main():
    result = solution("-1 -2 -3 Z")
    print(result)

# [1,2,3]
# run program
if __name__ == "__main__":
    main()
