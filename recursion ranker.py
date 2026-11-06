with open("word list.txt") as f: # replace the "word list.txt" with the name of the word list you want to use. It needs to be in the same file folder as the code after you download it
    words = [line.strip() for line in f]
words.sort(key=len)
length = len(words[0])
ranked_pairs = []
for word in words:
    if len(word) > length:
        length = len(word)
        ranked_pairs.sort(reverse=True)
        print(length) # this will print a lot of numbers in the output. Every new number it prints is a new length of words it checks. This is a way to track the code's progress.
    recursive = False
    score = 0
    for order, rank in ranked_pairs:
        if rank in word:
            recursive = True
            score = order + 1
            break
    if recursive:
        ranked_pairs.append((score, word))
    else:
        ranked_pairs.append((0, word))
ranked_pairs.sort()
for score, word in ranked_pairs:
    print(word, score, sep = "\t")
