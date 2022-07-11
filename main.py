#


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


def roman_to_int(numeral):
    return_int = 0
    letters = list(numeral)
    while len(letters) > 0:
        if len(letters) == 1:
            return_int += get_int(letters.pop(0))
        else:
            if get_int(letters[0]) < get_int(letters[1]):
                return_int += get_int(letters[0] + letters[1])
                letters.pop(0)
                letters.pop(0)
            else:
                return_int += get_int(letters.pop(0))
    return return_int

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

    #print(str(2) + ':' + int_to_roman(2) + ':' + str(roman_to_int(int_to_roman(2))))