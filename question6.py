string = input("enter the string : ")
list_words = string.split()
set_words = set(list_words)

#number of unique words used
print("number of unique words used :", len(set_words))

#getting unique words
print(set_words)
