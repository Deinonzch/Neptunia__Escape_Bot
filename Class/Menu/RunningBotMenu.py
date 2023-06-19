from Class.Bot.RunningBot import *
import threading
from Class.Menu.BotMenu import *


class RunningBotMenu(BotMenu):
    __bot = RunningBot()

    def __init__(self, surface, __exit_button):
        super().__init__(surface, __exit_button)

    def _clicked_exit_button(self, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            super().__exit_button.clicked()
            self.draw()
            time.sleep(0.1)
            self._exit_running_bot_menu()
            self.__exit_button.unclicked()

    def clicked_exit_button_of_window(self, event_type):
        if event_type == pygame.QUIT:
            pygame.quit()
            self.__bot.finish()
            sys.exit(0)

    def _exit_running_bot_menu(self):
        if self.__exit_button.is_clicked():
            self.exit()

    def run(self):
        self._run_menu()
        self._run_bot()

    def _run_bot(self):
        self.__bot.run()
        t = threading.Thread(target=self.__bot.running, name='thread1')
        s = threading.Thread(target=self.__bot.listener, name='thread2')
        t.start()
        s.start()

    def exit(self):
        self._exit_menu()
        self._go_off_bot()

    def _go_off_bot(self):
        self.__bot.finish()
