# A number of people are standing in a circle waiting to be executed.
# Counting begins at a specified point in the circle and proceeds around
# the circle in a specified direction. After a specified number of people
# are skipped, the next person is executed. The procedure is repeated with
# the remaining people, starting with the next person, going in the same
# direction and skipping the same number of people, until only one person
# remains, and is freed.

def binary(n):
    if n <= 1:
        code.append(1)
        return code
    result = n % 2
    if result == 0:
        code.append(0)
        return binary(n // 2)
    else:
        code.append(1)
        return binary(n // 2)
code = []
binary(7)
code = code[::-1]
code.append(code[0])
code.pop(0)
code = code[::-1]
count = 0
total = 0
for i in code:
    if i == 1:
       count += 2**total
    total += 1
print(count)