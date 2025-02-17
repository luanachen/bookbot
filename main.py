file_contents = 'books/frankenstein.txt'

def main():
    with open('books/frankenstein.txt') as f:
     file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---") 
    print(f"{count_words(file_contents)} words found in the document")
    char_count = count_characters(file_contents)
    for char in char_count:
        if char.isalpha():
            print(f"The '{char}' character was found {char_count[char]} times")

def count_words(str: str) -> int:
    words = str.split()
    return(len(words))

def count_characters(str: str) -> dict[str, int]:
    char_count = {}
    for char in str.lower():
       if char in char_count:
          char_count[char] += 1
       else:
          char_count[char] = 1
    return char_count
   
main()