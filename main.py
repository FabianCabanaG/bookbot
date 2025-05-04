from stats import count_words, count_characters
import sys

path = ''

if len(sys.argv) == 1 or len(sys.argv) > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]
assert path != ''

def get_book_text(filepath):
    book_content = ''
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    content = get_book_text(path)
    num_words = count_words(content)
    num_chars = count_characters(content)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{num_chars}
============= END ===============
    """)
main()
