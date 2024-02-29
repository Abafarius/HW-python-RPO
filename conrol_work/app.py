from client import AbcClient
from server import AbcServer
from model import AbcModel
from view import AbcView
from wiktionary import Wiktionary


class AbcApplication:
    port = 10101

    def __init__(self, lang='ru', mode='client', hostname='localhost'):
        if mode == 'server':
            self.connector = AbcServer(hostname, self.port)
        elif mode == 'client':
            self.connector = AbcClient(hostname, self.port)
        else:
            raise RuntimeError(f"Unknown mode: '{mode}'")
        
        self.model = AbcModel()
        self.view = AbcView()
        self.wiktionary = Wiktionary(lang)

    def start(self):
        word = '_'
        self.view.show('Wait...')
        self.connector.connect()
        if isinstance(self.connector, AbcServer):
            word = self.my_turn(word)

        while True:
            word = self.opponent_turn(word)
            if not word:
                self.view.show_win()
                break
            word = self.my_turn(word)
            if not word:
                self.view.show_loose()
                self.connector.end()
                break
        

    def my_turn(self, last_word):
        attempts_left = 3
        while attempts_left:
            attempts_left -= 1
            word = self.view.ask_word()
            if last_word != '_' and word[0] != last_word[-1]:
                self.view.show_mistake(last_word[-1], attempts_left)
            elif self.model.is_used(word):
                self.view.show_duplicate(attempts_left)
            elif not self.wiktionary.is_exists(word):
                self.view.show_unknown()
            else:
                self.model.add(word)
                return word
        return ''
    

    def opponent_turn(self, last_word):
        if last_word != '_':
            self.connector.send(last_word)
        word = self.connector.receive()
        self.view.show_word(word)
        self.model.add(word)
        return word
    

