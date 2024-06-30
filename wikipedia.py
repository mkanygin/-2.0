meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное" }
while True:
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
    print("Такого слова нет в словаре")
    print("хотите добавить новое слово?")
    answer = input("да/нет")
    if answer == "да":
        new_word = input("введите новое слово большими буквами: ")
        if new_word in meme_dict.keys():
            print("такое слово уже есть в словаре")
        else:
            new_meme = input("введите новое значение: ")
            meme_dict[new_word] = new_meme
            print(meme_dict)
    else:
        print("до свидания")
