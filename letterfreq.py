def most_frequent(input_string):
    char_frequency = {}
    
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            char_frequency[char] = char_frequency.get(char, 0) + 1

    sorted_chars = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)

    for char, frequency in sorted_chars:
        print(char, "=", frequency)

input_string = input("Please enter a string: ")
print("Character frequencies in the input string:")
most_frequent(input_string)





