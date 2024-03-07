# https://school.programmers.co.kr/learn/courses/30/lessons/181918

def solution(arr):
    stk = []
    i = 0
    time = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk += [arr[i]]
            i += 1
        else:
            stk.pop()

        time += 1
    return stk


# main function
def main():
    result = solution([1, 4, 2, 5, 3])
    print(result)


# run program
if __name__ == "__main__":
    main()
