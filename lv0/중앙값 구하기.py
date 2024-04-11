# https://school.programmers.co.kr/learn/courses/30/lessons/120811

solution = lambda array: sorted(array)[len(array) // 2]

# main function
def main():
    result = solution([1, 2, 7, 10, 11])
    print(result)


# run program
if __name__ == "__main__":
    main()
