from number_theory_functions import modular_exponent

originalNumber = 23539673
powNumber = 3434462
baseNumber = 1000

print('the third digit of {:d}^{:d} is {:d}'.format(originalNumber, powNumber,
                                                     int(modular_exponent(originalNumber, powNumber, baseNumber) / 100)))
