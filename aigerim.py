...
1) one_iterable = [2, 1, 3, 4, 7, 11]
   another_iterable = ['P', 'y', 't', 'h', 'o', 'n']
   for n, letter in zip(one_iterable, another_iterable):     
   print(letter, n)
...

...
2) def palindromic(sequence):
    """Возвращает True, если последовательность является палиндромом."""
    for n, m in zip(sequence, reversed(sequence)):
        if n != m:
            return False
    return True
...

...
3) def palindromic(sequence):
    """Возвращает True, если последовательность является палиндромом."""
    return all(
        n == m
        for n, m in zip(sequence, reversed(sequence))
    )
...

...
4) def palindromic(sequence):
    """Возвращает True, если последовательность является палиндромом."""
    return not any(
        n != m
        for n, m in zip(sequence, reversed(sequence))
    )
...

...
5) class RomanNumeral:

    """Римская цифра, представленная как строка и число."""

    SYMBOLS = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    def __init__(self, number):
        self.value = number

    @classmethod
    def from_string(cls, string):
        return cls(cls.roman_to_int(string))

    @staticmethod
    def roman_to_int(numeral):
        total = 0
        for symbol, next_symbol in zip_longest(numeral, numeral[1:]):
            value = RomanNumeral.SYMBOLS[symbol]
            next_value = RomanNumeral.SYMBOLS.get(next_symbol, 0)
            if value < next_value:
                value = -value
            total += value
        return total
        ...