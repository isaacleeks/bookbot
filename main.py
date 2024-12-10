def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        
        words = file_contents.split()

        # print(len(words))

        chars_dict = {}
        lower_case_text = file_contents.lower()

        for char in lower_case_text:
            if char.isalpha() == True:
                if char in chars_dict:
                    chars_dict[char] += 1
                else:
                    chars_dict[char] = 1

        def sort_on(dict):
            return dict["count"]
                
        chars_list = []

        for key in chars_dict:
            new_dict = {"char": key, "count": chars_dict[key]}
            chars_list.append(new_dict)
        
        chars_list.sort(reverse=True, key=sort_on)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")

        for alphabet in chars_list:
            print(f" The {alphabet['char']} character was found {alphabet['count']} times")

        print("--- End report ---")

        
        # print(f"sliced_chars: {sliced_chars}")




main()