text = "abcdefg"
print(dir(text))
help(text.isidentifier)
print(text.isidentifier()) # is abcdefg a valid identifier
print("1234".isidentifier()) # is 1234 a valid identifier
print("anananananananananananana".count("ana"))
print("anananananananananananana".replace("ana", "bob"))
print("anananananananananananana".replace("ana", "bob").count("bob"))
print("anananananananananananana".find("ana", 1))
print("bbbbbabbbbbabbbbabbbabb".split("a"))
print("this is a sentence and I want the words".split(" "))
sentence = "Hello, kind-sir; how may! I be of service today?"
punctuation = ",-;!?"
# sanitize the sentence
for p in punctuation:
    sentence = sentence.replace(p," ") # replace punctuation with nothing
print(sentence)
# split the sentence into words
words = sentence.split(" ")
print(words)
