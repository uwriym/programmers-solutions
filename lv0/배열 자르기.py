# https://school.programmers.co.kr/learn/courses/30/lessons/120833

solution = lambda numbers, num1, num2: numbers[num1:num2+1]
        
        
# main function
def main():
    result = solution([1, 2, 3, 4, 5], 1, 3)
    print(result)


# run program
if __name__ == "__main__":
    main()
