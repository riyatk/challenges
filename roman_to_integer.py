def roman_to_integer(s):
    total = 0
    symbols = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    length = len(s)

    for i in range(length):
        if (i+1 < length) and symbols[s[i]] < symbols[s[i+1]]:
            total = total - symbols[s[i]]
        else:
            total = total + symbols[s[i]]
    return total
print(roman_to_integer("MCMXCIV"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("III"))