units = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

tens = [
    '',
    'teen',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]

special_cases = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    15: 'fifteen',
    18: 'eighteen'
}
    
magnitudes = [
    '',
    'thousand',
    'million',
    'billion',
    'trillion',
    'quadrillion',
    'quintillion',
    'sextillion',
    'septillion',
    'octillion',
    'nonillion',
    'decillion',
    'undecillion',
    'duodecillion',
    'tredecillion',
    'quatuordicillion',
    'quindecillion',
    'sexdecillion',
    'septendecillion',
    'octodecillion',
    'novemdecillion',
    'vigintillion'
]

def up_to_one_hundred(n):
    if n < 10:
        return unit[n]
    if n in special_cases.keys():
        return special_cases[n]
    
    left_digit  = ten[n//10]
    right_digit = unit[n%10]
    
    if right_digit == 'zero':
        return left_digit
    elif n < 20:
        return f"{right_digit}{left_digit}"
    else:
        return f"{left_digit}-{right_digit}"

def up_to_one_thousand(n):    
    if n < 100:
        return up_to_one_hundred(n)
    
    left_digit = n//100
    rest = n%100
    
    if rest == 0:
        return f'{unit[left_digit]} hundred'
    else:
        return f'{unit[left_digit]} hundred {up_to_one_hundred(rest)}'

def wordy_int(n):
    chunks = []
    while n > 1000:
        chunks.append(n%1000)
        n = n//1000
    chunks.append(n)
    
    final = []
    for chunk, magnitude in zip(chunks, magnitudes):
        if chunk > 0:
            final.append(f'{hundreds(chunk)} {magnitude}')
    
    return ' '.join(reversed(final))