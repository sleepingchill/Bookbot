with open("books/Frankenstein.txt") as f:
    content = f.read() 

book_name = "books/Frankenstein.txt".split("/")
true_name = book_name[1].split(".")


words = len(content.split())
print("The total word count of " + true_name[0] + " is " + str(words))
