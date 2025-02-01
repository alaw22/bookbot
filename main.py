def get_number_of_words(book_contents):
    book_contents_list = book_contents.split()
    return len(book_contents_list)

def char_frequency(book_contents):
    char_frequency_dd = {}
    lower_book_contents = book_contents.lower()
    for char in lower_book_contents:
        if char not in char_frequency_dd:
            char_frequency_dd[char] = 1
        else:
            char_frequency_dd[char] += 1

    return char_frequency_dd

def sort_on(char_dd):
    return char_dd["num"]


def convert_to_list_of_dictionaries(char_dd,is_alphanum = True):
    list_of_dicts = []
    for key in char_dd:
        temp_dict = {"char":key,"num":char_dd[key]}
        if is_alphanum and key.isalpha():
            list_of_dicts.append(temp_dict)
    
    return list_of_dicts


with open("books/frankenstein.txt","r") as f:
    file_contents = f.read()

num_words = get_number_of_words(file_contents)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{num_words} words found in the document\n\n")

frankenstein_character_frequency = char_frequency(file_contents)
list_of_frequencies = convert_to_list_of_dictionaries(frankenstein_character_frequency)
list_of_frequencies.sort(reverse=True,key=sort_on)
for i in range(len(list_of_frequencies)):
    char = list_of_frequencies[i]["char"]
    num = list_of_frequencies[i]["num"]
    print(f"The '{char}' character was found {num} times")

print("--- End report ---")
