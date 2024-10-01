def main():
    report_findings_on("frankenstein.txt")

def read_book(book_name):
    book_path = f"books/{book_name}"
    # open file in read mode
    with open(book_path, 'r') as file:
        # iterate and print each line in file
        for line in file:
            print(line.strip()) # strip() removes trailing newline chars

def get_book_content(book_name):
    book_path = f"books/{book_name}"
    with open(book_path, 'r') as file:
        return file.read()

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

def report_findings_on(book_name):
    book_content = get_book_content(book_name)
    word_count = count_words(book_content)
    char_count = count_chars(book_content)
    sorted = create_sorted_array_of_char_count_dicts(char_count) # lol
    key, value = "letter", "num"
    print(f"\n--- Begin report of books/{book_name} ---\n")
    print(f"Total words: {word_count}\n")
    for record in sorted:
        print(f"The letter '{record[key]}' was found {record[value]} times.")
    print("\n--- End Report ---\n")

def create_sorted_array_of_char_count_dicts(char_count): # lol
    result = []
    for char in char_count:
        if str.isalpha(char):
            result.append({"letter" : char, "num" : char_count[char]})
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(dict):
    return dict["num"]

main()
