data_file = open("dictionary.txt", "r")

def clean_word(word):
    """Return word in lowercase stripped of whitespace."""
    return word.strip().lower()

def get_vowels_in_word(word):
    """Return vowels in string word - include repeats."""
    vowel_str = "aeiou"
    vowels_in_word = ""
    for char in word:
        if char in vowel_str:
            vowels_in_word += char
    return vowels_in_word

# Main program
print("Find words containing vowels 'aeiou' in that order:")

# For each word in the file
for word in data_file:
    word = clean_word(word)  # Clean the word

    # If the word is too small, skip it
    if len(word) <= 6:
        continue

    # Get vowels in the word
    vowel_str = get_vowels_in_word(word)

    # Check if you have exactly 'aeiou' vowels in order
    if vowel_str == 'aeiou':
        # Print the word
        print(word)

# Close the file when done
data_file.close()
