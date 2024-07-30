def multiply(x: float, y:float)->float: 
    """
    Multiply 2 numbers.
 
    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.
 
    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result
 
 # this function takes string as an input and return bool 
def is_palindrome(string: str)-> bool:
    """
    Check if a string is a palindrome.
 
    A palindrome is a string that reads the same forwards as backwards.
 
    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()
 
 
def palindrome_sentence(sentence:str)->bool:
    """
    Check if a sentence is a palindrome.
 
    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
 
    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
#Iterates over each character char in the input sentence.
    for char in sentence:
#Checks if char is alphanumeric (i.e., a letter or a digit).
# The isalnum() method returns True if the character is alphanumeric and False otherwise.
        if char.isalnum():
            string += char #If char is alphanumeric, it is appended to the string.
    return is_palindrome(string)

# Print the docstring of the is_palindrome function
print("is_palindrome docstring:")
print(is_palindrome.__doc__)

# Print the docstring of the palindrome_sentence function
print("\npalindrome_sentence docstring:")
print(palindrome_sentence.__doc__)
    
word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

# answer = multiply(18, 3)
# print(answer)
