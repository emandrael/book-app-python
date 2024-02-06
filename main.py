def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print('--- Begin report of books/frankenstein.txt ---')
        print(f"{len(file_contents.split())} words found in the document")
        letters = {}
        for char in file_contents.lower():
            if char.isalpha():
                if char in letters:
                    letters[char] += 1; 
                else:
                    letters[char] = 0;
        sorted_letters = dict(sorted(letters.items(), key=lambda item:item[1], reverse=True))
        
        for letter in sorted_letters:
            print(f"The {letter} was found {letters[letter]} times")
           

main()
