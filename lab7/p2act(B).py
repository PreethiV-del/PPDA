def word_count_frequency(sentence):
    words = sentence.lower().split()  
    word_count = len(words)
    word_frequency = {}

    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    return word_count, word_frequency

sentence = input("Enter a sentence: ")
count, frequency = word_count_frequency(sentence)
print(f"The number of words in the sentence is: {count}")
print("Word frequency:")
for word, freq in frequency.items():
    print(f"{word}: {freq}")