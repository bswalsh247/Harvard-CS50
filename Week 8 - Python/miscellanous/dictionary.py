# We can re-implement all the examples from weeks 1 through 5 in Python, 
# and even the entire speller program.

# More interestingly, we can look at just the dictionary.py file:

class Dictionary: # equivalant of a structure in C

    def __init__(self): # declare funtion
        self.words = set() # set is a function that returns to me an empty set a collection of values that faciliatea contstant time look ups on whether something is there and constant time insertions

    def check(self, word):
        return word.lower() in self.words

    def load(self, dictionary):
        file = open(dictionary, "r")
        for line in file:
            self.words.add(line.rstrip("\n"))
        file.close()
        return True

    def size(self):
        return len(self.words)

    def unload(self):
        return True


# Here, we create a words property when each Dictionary is initialized, and set 
# it to an empty set. In Python, sets are abstracted (so we don’t know anything 
# about how it’s implemented in memory anymore, or whether it’s a hash table, 
# or trie, or something else entirely) but we can easily operate with it.

# We can add items to self.words with self.words.add(), check if a word is in it with 
# word in self.words(), and get the size with len(self.words).

# And since Python mananges our memory for us, we don’t even need to worry about 
# unloading it or freeing it.

# As we see above, a higher-level language like Python, which has implemented many 
# lower-level features that would take dozens of lines in C, allows us to write more 
# and more sophisticated programs without having to worry about all of the details.

