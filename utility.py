import platform, os, time, sys
class Utility:
    _MESSAGES = {}

    def __init__(self):
        self._MESSAGES['welcome'] = '''
          ____ ___  _   _ _____  _    ____ _____   ____   ___   ___  _  __
         / ___/ _ \| \ | |_   _|/ \  / ___|_   _| | __ ) / _ \ / _ \| |/ /
        | |  | | | |  \| | | | / _ \| |     | |   |  _ \| | | | | | | ' / 
        | |__| |_| | |\  | | |/ ___ \ |___  | |   | |_) | |_| | |_| | . \ 
         \____\___/|_| \_| |_/_/   \_\____| |_|   |____/ \___/ \___/|_|\_\   
        ''';

    def render(self, type_message):
        if type_message == 'welcome':
            self.clear_display()
            print(self._MESSAGES['welcome'])

    def clear_display(self):
        sistema = platform.system()
        if sistema == 'Linux':
            os.system('clear')
        elif sistema == 'Windows':
            os.system('cls')
        else:
            os.system('clear')