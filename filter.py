text = input('Введите текст для редактирования: ')
print('Количесто слов: ', len(text.split()))
print('Слова: ',text.split())
for i in range (len(text.split())):
    if text.split()[i][0].isupper():
        text = text.replace(text.split()[i],text.split()[i][0]+'*'*(len(text.split()[i])-1))
    elif text.split()[i][0] == '«':
        text = text.replace(text.split()[i], '«' + text.split()[i][1] + '*' * (len(text.split()[i]) - 3) + '»')
print(text)


def word_check():
    a = 0
    while a==0:
        num = input(f'Введите номер слова для обработки до {len(text.split())}: ')
        print(text.split()[int(num)-1])
        num_sym = input(f'Введите номер символа для обработки до {len(text.split()[int(num)-1])}: ')
        print((text.split()[int(num)-1])[int(num_sym)-1])
        sym = (text.split()[int(num)-1])[int(num_sym)-1]
        if sym.isupper():
            print('Этот символ заглавный')
        else:
            print('Этот символ строчный')
        a = int(input('Для повтора нажмите 0: '))


