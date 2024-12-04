def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_characters(text)
    char_list = convert_to_list(chars)
    sorted_chars = sort_characters(char_list)

    print(f"{num_words} words found in the document")
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")


    print(chars)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_characters(text):

    characters = {}
    for character in text:
        if character.isalpha():
            character = character.lower()
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1       

    return characters

def convert_to_list(characters):
    char_list = [(char,count) for char,count in characters.items()]
    return char_list

def sort_characters(char_list):
    return sorted(char_list, key=lambda item: item[1], reverse=True)
main()