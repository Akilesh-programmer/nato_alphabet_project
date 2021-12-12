import pandas

# Getting the data read and stored.
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Creating a dictionary with the above data.
nato_dict = {}
for (index, row) in nato_data.iterrows():
    nato_dict[row.letter] = row.code

# Getting input from the user.
user_input = input("What's the word?:  ")
# Making the input uppercase.
user_input = user_input.upper()
letters = [letter for letter in user_input]

# Getting the code word into a list.
code_word = [value for (key, value) in nato_dict.items() if key in letters]
# Printing the final output.
print(code_word)
