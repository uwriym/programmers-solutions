# https://school.programmers.co.kr/learn/courses/30/lessons/120809

solution = lambda array: list(x * 2 for x in array)

# main function
def main():
    result = solution([1, 2, 3, 4, 5])
    print(result)


# run program
if __name__ == "__main__":
    main()
