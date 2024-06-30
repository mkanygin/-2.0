meme_dict = {
    "КРИНЖ": "Что-то очень странное или стыдное",
    "ЛОЛ": "Что-то очень смешное"
}

while True:
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict:
        print(meme_dict[word])
    else:
        print("Такого слова нет в словаре")
    
    answer = input("Хотите добавить новое слово? (да/нет): ").lower()
    if answer == "да":
        new_word = input("Введите новое слово большими буквами: ")
        if new_word in meme_dict:
            print("Такое слово уже есть в словаре")
        else:
            new_meme = input("Введите значение нового слова: ")
            meme_dict[new_word] = new_meme
            print("Слово успешно добавлено")
            print("Текущий список слов:", ", ".join(meme_dict.keys()))
    elif answer == "нет":
        print("Выход из программы")
        break
    else:
        print("Пожалуйста, введите 'да' или 'нет'")