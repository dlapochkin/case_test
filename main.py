"""
Case-study #4 Анализ текста
Разработчики:

"""

from textblob import TextBlob

text = input('Введите текст: ')
blob = TextBlob(text)
syllables = 0
sentence = 0
fre = 0

for b in ['.', '!', '?']:
    if text.count(b) > 0:
        sentence += text.count(b)
print('Предложений:', sentence)

print('Слов:', text.count(' ') + 1)

if blob.detect_language() == 'ru':
    syllables = sum(1 for x in text.lower() if x in 'уеоаыяиюэ')
else:
    syllables = sum(1 for x in text.lower() if x in 'aeiouy')
asl = (text.count(' ') + 1) / sentence
asw = syllables / (text.count(' ') + 1)
print('Слогов:', syllables)
print('Средняя длина предложения в словах:', asl)
print('Средняя длина слова в слогах:', asw)

if blob.detect_language() == 'ru':
    fre = 206.835 - (1.3 * (asl)) - (60.1 * asw)
else:
    fre = 206.835 - (1.015 * asl) - (84.6 * asw)
print('Индекс удобочитаемости Флеша:', fre)

if fre > 80:
    print('Текст очень легко читается (для младших школьников).')
elif fre > 50:
    print('Простой текст (для школьников).')
elif fre > 25:
    print('Текст немного трудно читать (для студентов).')
else:
    print('Текст трудно читается (для выпускников ВУЗов).')

if blob.detect_language() == 'ru':
    blob = blob.translate(to="en")
if blob.sentiment.polarity > 0.33:
    tonality = 'Положительная'
elif blob.sentiment.polarity < -0.33:
    tonality = 'Отрицательная'
else:
    tonality = 'Нейтральная'
print('Тональность текста:', tonality)
obj = format(1 - blob.sentiment.subjectivity, '.1%')
print('Объективность:', obj)