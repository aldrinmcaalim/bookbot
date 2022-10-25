# more scalable way to do it, since we're placing everything in functions we are more able to scale things as we need as it makes things more adaptable to changes when we need them
book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    print(text)
    print(count_letters(text))
    print(f"----- Begin Report of {book_path} -----")
    print(f"There are a total of {get_word_count(text)} words in the document!")
    report_char_count(count_letters(text))
    print("----- End of Report -----")

def get_book_text(book_path):
    with open(book_path) as bp:
        book_contents = bp.read()
    return book_contents

def get_word_count(text):
    total_word_count = len(text.split())
    return total_word_count

def count_letters(text):
    count_chars = {}
    lower_cased = text.lower()
    split_into_array = lower_cased.split()
    for word in split_into_array:
        for char in word:
            count_chars[char] = 1 + count_chars.get(char, 0)
    return count_chars

def sort_on(d):
    return d["num"]

def sorted_dictionary(dictionary):
    sorted_arr = []
    for ch in dictionary:
        sorted_arr.append({"char": ch, "num": dictionary[ch]})
    sorted_arr.sort(reverse=True, key=sort_on)
    return sorted_arr

def report_char_count(char_dictionary):
    char_dict_sorted = sorted_dictionary(char_dictionary)
    for letter, count in char_dictionary.items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
        
main()


# less scalable way to do it
# with open("books/frankenstein.txt") as f:
#     file_contents = f.read()
#     print(file_contents)

# with open("books/randomtext.txt") as r: # will ERROR if you don't have proper relative path in quotes
#     file_contents = r.read()
#     print(file_contents)