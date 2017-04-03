def precision(number, prec):
    """
    :return: small number rounded to readable format
    """
    return float(format(number, '.{}f'.format(prec)))


def newton(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return float(n) / k * newton(n - 1, k - 1)


