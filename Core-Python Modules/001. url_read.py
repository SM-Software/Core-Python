from urllib.request import urlopen

story = urlopen('https://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    # decoding from bytes to string
    words = line.decode('utf8').split()
    for word in words:
        story_words.append(word)
story.close()
print(story_words)