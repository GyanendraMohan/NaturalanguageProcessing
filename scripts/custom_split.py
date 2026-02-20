def split_text(text):
    res = []
    curr_word = ""
    for char in text:
        if char.isalnum():
            curr_word += char
        else:
            if curr_word:
                res.append(curr_word)
                curr_word = ""
    if curr_word:
        res.append(curr_word)
    return res

text = "i am learning natural language processing. it is interesting!"
tokens = split_text(text)
print(tokens)   