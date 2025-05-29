letter = '''Dear <|NAME|>,
You are selected!
<|DATE|> is the date of joining.

'''
print(letter.replace("<|NAME|>", "Abhinav").replace("<|DATE|>", "1st January 2024"))
