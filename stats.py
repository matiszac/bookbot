import sys

def read_book(book_name):
    book_path = f"books/{book_name}"
    # open file in read mode
    with open(book_path, 'r') as file:
        # iterate and print each line in file
        for line in file:
            print(line.strip()) # strip() removes trailing newline chars

def get_book_content(book_path):
    try:
        with open(book_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(e)
        sys.exit(1)

def count_words(book_content):
    words = book_content.split()
    return len(words)

def count_chars(book_content):
    content = book_content.lower()
    chars = {}
    for char in content:
        key = char
        if char == " ":
            key = "<space>"
        elif char == "\n":
            key = "<new_line>"
        if not key in chars:
            chars[key] = 1
        else:
            chars[key] += 1
    return chars

def get_sorted_dict_from_chars_dict(chars_count_dict):
    sorted_dict_list = []
    for char, count in sorted(chars_count_dict.items(), key=lambda item: item[1], reverse=True):
        if str.isalpha(char):
          sorted_dict_list.append({"char": char, "num": count})
    return sorted_dict_list

def report_findings_on(book_path):
    book_content = get_book_content(book_path)
    word_count = count_words(book_content)
    char_count_dict = count_chars(book_content)
    sorted = get_sorted_dict_from_chars_dict(char_count_dict) # lol
    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print(f'----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print(f'--------- Character Count -------')
    for record in sorted:
        print(f'{record['char']}: {record['num']}')
    print(f'============= END ===============')