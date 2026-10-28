#Question 1
def binary(n):
    return format(n & 255, '08b')

for a, b in [(120, 62), (-120, -62)]:
    result = a + b

    print("\nOperands:", a, "and", b)
    print("Binary 1:", binary(a))
    print("Binary 2:", binary(b))
    print("Binary Result:", binary(result))
    print("Decimal Result:", result if -128 <= result <= 127 else result - 256)

    if result < -128 or result > 127:
        print("Overflow: Yes")
    else:
        print("Overflow: No")

#Question 2
def left_shift(binary, n):
    for i in range(n):
        binary = binary[1:] + '0'
        print(binary)
    return binary

def right_shift(binary, n):
    for i in range(n):
        binary = '0' + binary[:-1]
        print(binary)
    return binary

a = "10110110"
b = "11010100"

print("a) Logical Left Shift")
print("Original:", a)
print("Steps:")
print("Final Result:", left_shift(a, 3))

print("\nb) Logical Right Shift")
print("Original:", b)
print("Steps:")
print("Final Result:", right_shift(b, 3))

