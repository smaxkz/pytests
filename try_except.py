try:
    text = input('Введите что-нибудь -->')
except EOFError:
    print('\nНу зачем вы сделали мне EOF?')
except KeyboardInterrupt:
    print('\nВы отменили операцию')
else:
    print('Вы ввели: {0}'.format(text))
