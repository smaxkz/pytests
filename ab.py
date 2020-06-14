import pickle

class Contact():
    '''Представляет контакт.'''
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.abDict = {}
        self.abDict[self.name] = self.phone

    def tell(self):
        for key, value in self.abDict.items():
            print(key, value)

contactFile = 'contacts.data'

print('Выберите операцию:')
selectOperation = int(input('\nВвести контакты - нажмите 1 \
                             \nПрочесть конакты - нажмите 2\n'))
if selectOperation == 1:
    # создание контактов
    countInputs = int(input('Сколько контактов собираетесь ввести? '))
    contacts = []
    for i in range(0, countInputs):
        nameInput = input('Введите имя контакта: ')
        phoneInput = input('Введите телефон контакта: ')
        cc = Contact('{0}'.format(nameInput), '{0}'.format(phoneInput))
        contacts.append(cc)
        continue
    else:
        print('Ввод закончен')
    
    try:
        contacts
    except:
        print('Список contacts не создан')
    else:
        f = open(contactFile, 'wb')
        pickle.dump(contacts, f)
        f.close()
        del contacts
else:
    # чтение контактов из файла
    try:
        open(contactFile)
    except:
        print('Файл contactsFile отсутствует')
    else:
        f = open(contactFile, 'rb')
        storedContacts = pickle.load(f)
        f.close()

        for contact in storedContacts:
            contact.tell()
