# more scalable way to do it, since we're placing everything in functions we are more able to scale things as we need as it makes things more adaptable to changes when we need them
book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    print(text)

def get_book_text(book_path):
    with open(book_path) as bp:
        book_contents = bp.read()
    return book_contents

main()


# less scalable way to do it
# with open("books/frankenstein.txt") as f:
#     file_contents = f.read()
#     print(file_contents)

# with open("books/randomtext.txt") as r: # will ERROR if you don't have proper relative path in quotes
#     file_contents = r.read()
#     print(file_contents)