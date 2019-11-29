import sys

def show_contacts(phone_book):
    if phone_book == {}:
        print('No existen contactos en la agenda')
    else:
        for name, phone in phone_book.items():
            print(name, ':', phone)

def add_contact(phone_book, name, phone):
    phone_book[name] = phone

def remove_contact(phone_book, name):
    if name in phone_book:
        del(phone_book[name])
    else:
        print('El contacto no existe')

def menu():
    phone_book = {}

    while True:
        print('''
        1. Mostrar lista de contactos.
        2. Añadir contacto (nombre y teléfono).
        3. Borrar contacto (nombre).
        4. Salir.''')

        menu = input('Introduzca un valor: 1 - 4: ')

        if menu == '1':
            show_contacts(phone_book)
        elif menu == '2':
            name = input('Introduzca el nombre del contacto: ')
            if name not in phone_book:
                phone = input('Introduzca el número del contacto: ')
                add_contact(phone_book, name, phone)
            else:
                print('Este contacto ya existe')
        elif menu == '3':
            name = input('Introduzca el contacto que desea eliminar: ')
            remove_contact(phone_book, name)
        elif menu == '4':
            break
        else:
            print('Menú incorrecto.')
    return exit()

print(menu())
