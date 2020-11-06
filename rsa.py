import random


def gcd(a, b):
    """
    Performs the Euclidean algorithm and returns the gcd of a and b
    """
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def xgcd(a, b):
    """
    Performs the extended Euclidean algorithm
    Returns the gcd, coefficient of a, and coefficient of b
    """
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y


def chooseE(totient):
    """
    Chooses a random number, 1 < e < totient, and checks whether or not it is
    co-prime with the totient, that is, gcd(e, totient) = 1
    """
    while (True):
        e = random.randrange(2, totient)

        if (gcd(e, totient) == 1):
            return e


def emil(a,d,n):
    baseModuled = a % n
    binaryPower = [int(d) for d in str(bin(d))[2:]][::-1]

    mul = 1

    for index, bit in enumerate(binaryPower, start=1):
        if bit == 1:
            i = 0
            res = 1
            while(i < 2**(index-1)):
                res *= baseModuled
                res = res % n
                i = i + 1
            mul *= res % n
            mul = mul % n

    return mul



def encrypt(message, N, e):
    """
    Encrypts a message (string) by raising each character's ASCII value to the
    power of e and taking the modulus of n. Returns a string of numbers.

    N - refer to the multiplication of two prime number

    e - refer to random number, 1 < e < (prime1-1)*(prime2-1)

    block_size - refers to how many characters make up one group of numbers in
    each index of encrypted_blocks.
    """

    encrypted_blocks = [ord(c) for c in message]


    for i in range(len(encrypted_blocks)):
        encrypted_blocks[i] = chr(emil(encrypted_blocks[i],e,N)%32 + 101)

    # create a string from the numbers
    encrypted_message = "".join(encrypted_blocks)

    return encrypted_message

