def fib(n):
    result = [1, 1]
    for i in range(2, n + 1):
        temp = result[i-1] + result[i-2]
        result.append(temp)

    return result[-2]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()