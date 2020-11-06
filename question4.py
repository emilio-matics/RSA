import rsa


def main():


    # two prime numbers
    p = 7919
    q = 6841

    # compute n, totient, e
    N = p*q
    totient = (p - 1) * (q - 1)
    e = rsa.chooseE(totient)

    # compute d, 1 < d < totient such that ed = 1 (mod totient)
    # e and d are inverses (mod totient)
    gcd, x, y = rsa.xgcd(e, totient)

    # make sure d is positive
    if (x < 0):
        d = x + totient
    else:
        d = x

    message = input('What would you like to encrypt?\n')


    print('Encrypting...')
    print("N is: {0}".format(N))
    print("e is: {0}".format(e))
    print(rsa.encrypt(message,N,e))


if __name__ == '__main__':

    #test("./corpus_for_test");

    main()