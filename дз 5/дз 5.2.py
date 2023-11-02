
input_string = input("Введите строку: ")

sentences = input_string.split('. ')

corrected_sentences = []

for sentence in sentences:
    words = sentence.split()


    for i in range(len(words)):

        if words[i] and (i == 0 or words[i - 1][-1] in ".!?"):
            words[i] = words[i].capitalize()


    corrected_sentences.append(" ".join(words))

output_string = ". ".join(corrected_sentences)

print(output_string)


