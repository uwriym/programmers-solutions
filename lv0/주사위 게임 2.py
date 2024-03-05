# https://school.programmers.co.kr/learn/courses/30/lessons/181930

def solution(a, b, c):
    all_plus = a + b + c
    add_two_squares = add_squares(a, b, c, 2)
    add_three_squares = add_squares(a, b, c, 3)

    print(f"all_plus: {all_plus}")
    print(f"add_two_squares: {add_two_squares}")
    print(f"add_three_squares: {add_three_squares}")

    if a == b and b == c:
        return all_plus * add_two_squares * add_three_squares
    elif a == b or b == c or c == a:
        return all_plus * add_two_squares
    else:
        return all_plus


def add_squares(a, b, c, square):
    return (a**square) + (b**square) + (c**square)


# main function
def main():
    print(solution(4, 4, 4))


# run program
if __name__ == "__main__":
    main()
