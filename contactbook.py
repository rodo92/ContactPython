from contact import Contact
from utility import Utility
import csv
class ContactBook:

    def __init__(self):
        self._contacts = []
        self.utility = Utility()

    def _save(self):
        with open('contact.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def edit(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name == name.lower():
                print('\n\t¿Qué es lo que desea editar?')
                option = int(input('\tnombre[1], telefeno[2], email[3]: '))

                if option == 1:
                    txt = str(input('\tIngrese el nuevo nombre : ')).lower()
                    self._contacts[idx].name = txt
                elif option == 2:
                    txt = str(input('\tIngrese el nuevo telefono : ')).lower()
                    self._contacts[idx].phone = txt
                elif option == 3:
                    txt = str(input('\tIngrese el nuevo email : ')).lower()
                    self._contacts[idx].email = txt

                return 1
                break
        else:
            return 0

    def search(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name == name.lower():
                self._print_cuztomizer(self._contacts[idx])
                return idx
                break
        else:
            self._not_found()

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name == name.lower():
                del self._contacts[idx]
                self._save()
        else:
            return 0

    def show_all(self):
        if len(self._contacts) == 0:
            self.utility.render('No existen contactos registrados')
        for contact in self._contacts:
            self._print_cuztomizer(contact)

    def _not_found(self):
        self.utility.render('No se encontraron registros.')

    def _print_cuztomizer(self, contact):
        print('\n\t---------------------------------------------------')
        print('\t| Nombre: \t{}' . format(contact.name))
        print('\t| Telefono: \t{}' . format(contact.phone))
        print('\t| Email: \t{}' . format(contact.email))
