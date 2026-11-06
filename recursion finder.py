with open("word list.txt") as f: # replace the "word list.txt" with the name of the word list you want to use. It needs to be in the same file folder as the code after you download it
    all_words = [line.strip() for line in f]
inpword = "prearrangements" # put whatever word you want in here. It doesn't even have to be an actual word that exists in the word list you give it
words = []
for word in all_words:
    if word in inpword and word != inpword:
        words.append(word)
words.sort(key=len)
length = len(words[0])
ranked_pairs = []
recurses = [inpword]
for word in words:
    if len(word) > length:
        length = len(word)
        ranked_pairs.sort(reverse=True)
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
ranked_pairs.sort(reverse=True)
for score, word in ranked_pairs:
    if word in inpword:
        inpword = word
        recurses.append(word)
for word in recurses:
    print(word)
