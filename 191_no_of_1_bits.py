## 191. Number of 1 Bits
'''
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
'''
# Difficuly: Easy
# Bit manipulation: Apply algorithm for calculating Hamming weight.

def hammingWeight(n: int) -> int:
    a0 = (n >> 0) & 0b01010101010101010101010101010101
    a1 = (n >> 1) & 0b01010101010101010101010101010101
    b = a0 + a1
    b0 = (b >> 0) & 0b00110011001100110011001100110011
    b2 = (b >> 2) & 0b00110011001100110011001100110011
    c = b0 + b2
    c0 = (c >> 0) & 0b00001111000011110000111100001111
    c4 = (c >> 4) & 0b00001111000011110000111100001111
    d = c0 + c4
    d0 = (d >> 0) & 0b00000000111111110000000011111111
    d8 = (d >> 8) & 0b00000000111111110000000011111111
    e = d0 + d8
    e0 = (e >> 0) & 0b00000000000000001111111111111111
    e16 = (e >> 16) & 0b00000000000000001111111111111111
    f = e0 + e16

    return f

if __name__ == '__main__':
    print(hammingWeight(0b00000000000000000000000000001011))
    num = 0b1111111111111111
    while num != 0:
        print("{:016b}".format(num))
        num >>= 1