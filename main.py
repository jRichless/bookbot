import sys
from stats import get_num_words, get_num_char, char_sort

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents     


def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    text = get_book_text(filepath)
    num_words = get_num_words(text)
    character_dict = get_num_char(text)
    sorted_dict = char_sort(character_dict)

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    
    for item in sorted_dict:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print ("============= END ===============")
                
    

main()

