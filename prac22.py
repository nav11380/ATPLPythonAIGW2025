quote = "be acceptable.work hard"
print('quote is:',quote,id(quote))
new_quote = quote.upper()
print('quote now is:',quote,id(quote))
print('new_quote now is:',new_quote,id(new_quote))

lower_case_quote = quote.lower()
print('lower_case_quote now is:',lower_case_quote,id(lower_case_quote))

print('Captalised',quote.capitalize())
print('Title case:',quote.title())
print('Swapcase:',quote.swapcase())
