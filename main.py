value = [12]
print(value)
censor = ['тест1', 'тест2', 'тест3', 'тест4', 'тест']
symbols = ' ,.!?'
if isinstance(value, str):
    temp_array = []
    temp_word = ''
    for ind, symbol in enumerate(value):
        if symbol not in symbols:
            temp_word = temp_word + symbol
            if ind == len(value) - 1:
                temp_array.append(temp_word)
        else:
            if temp_word == '':
                temp_array.append(symbol)
            else:
                temp_array.append(temp_word)
                temp_word = ''
                temp_array.append(symbol)

    # print(temp_array)

    for ind, word in enumerate(temp_array):
        if (word.lower() or word.upper()) in censor:
            new_word = word[0] + ('*' * (len(word) - 1))
            temp_array[ind] = new_word

    # print(temp_array)

    recovered_text = ''
    for words in temp_array:
        recovered_text = recovered_text + words
    print(recovered_text.strip())

else:
    print('Текст не подлежит модерации, т.к. не является текстом!')

