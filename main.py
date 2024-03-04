with open("books/Frankenstein.txt") as f:
    content = f.read() 

print("--- Begin report of frankenstein.txt ---")

lowercasebook = content
lowered_string = lowercasebook.lower()
#print(lowered_string) this will print the book if you remove the numberkey
letter_dict = {}
for i in lowered_string:
    if i.isalpha():
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
#print(letter_dict) this prints dict of characters

letter_tuples = list(letter_dict.items())

def sort_on(tup):
    return tup[1]

letter_tuples.sort(reverse=True, key=sort_on)
#print(letter_tuples) 

for i in letter_tuples:
    print("The " + i[0] +" character was found " + str(i[1]) + " times")


book_name = "books/Frankenstein.txt".split("/")
true_name = book_name[1].split(".")



words = len(content.split())
print("The total word count of " + true_name[0] + " is " + str(words))

print("--- End report ---")