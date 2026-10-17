text = input("Введите текст: ")
words = text.lower().split()
for i in range(len(words)):
    words[i] = words[i].strip(":;?!,.")
cnt=0
for word in words:
    if 'а' not in word:
        print(word)
        cnt+=1
if cnt ==0:
    print("Нет совпадений")
print(f'Количество подходящих слов: {cnt}')