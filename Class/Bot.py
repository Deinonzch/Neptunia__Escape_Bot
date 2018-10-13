import keyboard


class Bot:
    _undone = True
    _break = False

    def listener(self):
        while self._undone:
            self._if_end_key_is_pressed_work_is_done()
            self._if_stop_key_is_pressed_do_break()
            self._if_restart_key_is_pressed_back_to_work()

    def _if_end_key_is_pressed_work_is_done(self):
        if keyboard.is_pressed('q'):
            self.finish()

    def finish(self):
        self._undone = False

    def _if_stop_key_is_pressed_do_break(self):
        if keyboard.is_pressed('alt+x'):
            self._stop()

    def _stop(self):
        self._break = True

    def _if_restart_key_is_pressed_back_to_work(self):
        if keyboard.is_pressed('alt+z'):
            self._restart()

    def _restart(self):
        self._break = False

    def _have_break(self):
        while self._break and self._undone:
            print('I have a break')
