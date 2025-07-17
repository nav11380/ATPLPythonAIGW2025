"""
    Strings are IMMUTABLE.
    Once, created in memory, they cannot be changed

    Anytime, we modify a string, a new string will be created in the memory

"""

# quote = 'Be Exceptional'
quote = 'Be exceptional. Work hard'
print('quote is:', quote, id(quote))
new_quote = quote.upper()


print('quote now is:', quote, id(quote))
print('new_quote now is:', new_quote, id(new_quote))

lower_case_quote = quote.lower()
print('quote now is:', quote, id(quote))
print('lower_case_quote now is:', lower_case_quote, id(lower_case_quote))

print('Capitalize:', quote.capitalize())
print('Title Case:', quote.title())
print('SwapCase:', quote.swapcase())

print('quote:', quote)