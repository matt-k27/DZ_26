print('DZ26')


def is_even(number):
    return not int(bin(number)[-1])


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

print('Thank you for using')
