import re


def get_input():
    s = input("Credit Card Number : ")
    return s


def t1(s):
    if s[0] in '456':
        return True
    else:
        return False


def t2(s):
    match1 = re.search(r'(\d{4})-(\d{4})-(\d{4})-(\d{4})', s)
    match2 = re.search(r'\d{16}', s)

    if match1:
        return True
    elif match2:
        if len(s) == 16:
            return True
        else:
            return False
    else:
        return False


def t3(s):
    x = ''
    if '-' in s:
        x = s.replace('-', '')

    for i in range(10):
        pattern = str(i) + str(i) + str(i) + str(i)

        match = re.search(pattern, x)
        if match:
            return False
        else:
            return True


def luhn_algo_test(s):
    x = s
    if '-' in s:
        x = s.replace('-', '')

    arr = []
    brr = []

    for i in range(len(x)):
        if i % 2 == 0:
            arr.append(2 * int(x[i]))
        else:
            arr.append(int(x[i]))

    for i in arr:
        if i > 9:
            n = str(i)
            sum = int(n[0]) + int(n[-1])
            brr.append(sum)

        else:
            brr.append(i)

    fsum = 0
    for i in brr:
        fsum += i

    if fsum % 10 == 0:
        return True
    else:
        return False


def main():
    s = get_input()
    print()
    if t1(s) == True and t2(s) == True and t3(s) == True and luhn_algo_test(s) == True:
        print('VALID')

    else:
        print('INVALID')


if __name__ == '__main__':
    main()
