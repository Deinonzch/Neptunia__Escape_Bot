from Class.Menu.Menu import *


class BasicMenu(Menu):
    _done = False

    def _run_menu(self):
        self._done = True

    def _exit_menu(self):
        self._done = False

    def is_done(self):
        if self._done:
            return True
        else:
            return False
