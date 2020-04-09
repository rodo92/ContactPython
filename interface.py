# -*- coding: utf-8 -*-
import time, sys, csv
from contactbook import ContactBook
from utility import Utility

class Interface:
    def __init__(self):
        self.cb = ContactBook()
        self.utl = Utility()
        self._restore_data()
        self._greeting()
        pass
    
    def _greeting(self):
        self.utl.render('welcome')
        command = str(input('''
                ¿Qué deseas hacer?

                [a]\tAgregar Contacto
                [e]\tEditar Contacto
                [b]\tBuscar
                [d]\tBorrar Contact
                [l]\tMostrar todo
                [s]\tSalir
            '''))
        self._execute(command)

    def _execute(self, command):
        self.utl.render('welcome')
        if command == 'a':
            name  = str(input('\tIngrese un nombre: ')).lower()
            phone = str(input('\tIngrese un teléfono: '))
            email = str(input('\tIngrese un email: ')).lower()
            self.cb.add(name, phone, email)
            self._render_alert('Contacto registrado con éxito!!!')

        elif command == 'e':
            name = str(input('\tIngrese el nombre del contacto a editar: '))
            response = self.cb.edit(name)
            if response == 1:
                self._render_alert('Contacto actualizado con éxito!!!')
            elif response == 0:
                self._render_alert('No se encontro al contacto en los registros.')

        elif command == 'b':
            name = str(input('\tIngrese el nombre del contacto a buscar: '))
            self.cb.search(name)
            self._render_alert('')

        elif command == 'd':
            name = str(input('\tIngrese el nombre del contacto a eliminar: '))
            self.cb.delete(name)

        elif command == 'l':
            self.cb.show_all()
            self._render_alert('')
            self._render_alert('Contacto eliminado con éxito!!!')

        elif command == 's':
            print('\tAdiós...')
            time.sleep(1)
            sys.exit()

        else:
            print('\tMensaje del sistema: Comando no válido')



    def _restore_data(self):
        try: 
            with open('contact.csv', 'r') as f:
                reader = csv.reader(f)
                for idx, row in enumerate(reader):
                    if idx == 0:
                        continue

                    self.cb.add(row[0], row[1], row[2])
        except Exception:
            print('')

    def _render_alert(self, message):
        print('\t{}' . format(message))
        print('\n\t---------------------------------------------------')
        op = str(input('\tDesea retornar al menú principal [S/N]: ')).lower()
        if op == 's':
            self._greeting()
        elif op == 'n':
            print('\tAdiós...')
            time.sleep(1)
            sys.exit()