# This dictionnary is the main driver for conversion between Roman numerals and integers
romanNumeralDictionary = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: "CD",
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}

'''
The methodology is to find the greatest applicable numeral for the highest power of 10
then subtracting it from the input value and appending this to a string representing the
roman numeral. This repeats until the input value is different and the resulting string
will be the roman numeral representation of the initial input value.
'''


def int_to_roman(val):
    roman_str = ''
    order = 1000

    while val > 0:
        quotient = val // order

        if quotient == 9:
            roman_str = roman_str + romanNumeralDictionary.get(quotient * order)
            val = val - quotient * order
            quotient -= 9

        if quotient >= 5:
            roman_str = roman_str + romanNumeralDictionary.get(5 * order)
            val = val - 5 * order
            quotient -= 5

        if quotient == 4:
            roman_str = roman_str + romanNumeralDictionary.get(4 * order)
            val = val - 4 * order
            quotient -= 4

        if quotient <= 3:
            for index in range(0, quotient):
                roman_str = roman_str + romanNumeralDictionary.get(order)
                val -= order

        order = order // 10

    return roman_str


'''
The methodology is to treat the input numeral as a string and then convert that string into
a list of character. Then to parse this string one character at a time and adding it to a "running total"
,with a mechanism for detecting subtractive notation.
'''


def roman_to_int(numeral):
    return_int = 0
    letters = list(numeral)
    while len(letters) > 0:
        if len(letters) == 1:
            return_int += get_int(letters.pop(0))
        else:
            if get_int(letters[0]) < get_int(letters[1]):
                return_int += get_int(letters.pop(0) + letters.pop(0))

            else:
                return_int += get_int(letters.pop(0))
    return return_int


'''
This is a helper function that help to find the "key by values" in the dictionary. This is however
very inefficient because the dictionary is disordered. This will be a point for improvement.
'''


def get_int(letter):
    for number, numeral in romanNumeralDictionary.items():
        if numeral == letter:
            return number

    print("There is no valid numeral")


if __name__ == '__main__':

    for index in range(1, 4000):
        roman = int_to_roman(index)
        re_int = roman_to_int(roman)
        print(str(index) + ':' + roman + ':' + str(re_int))
