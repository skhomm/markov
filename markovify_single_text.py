# подключаем библиотеку
import markovify

# отправляем в переменную всё содержимое текстового файла
text = open('tolstoy.txt', encoding='utf8').read()

# сразу обрабатываем весь текст одной командой
# на этом этапе библиотека уже взяла корпус, нашла все пары, построила связи между словами и выяснила вероятности появления новых слов
text_model = markovify.Text(text)

# выводим 30 предложений
for i in range(10):
    print(text_model.make_sentence())