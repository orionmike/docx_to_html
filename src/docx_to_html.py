
import webbrowser
from pathlib import Path

import pyperclip
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from pygments.lexers import HtmlLexer

from config import BACKUP_DAYS, DIR_RESULT
from libs.email_text import get_html
from libs.files import del_old_files, save_file_html
from libs.utils import get_time_now

Config.set('kivy', 'window_icon', Path('icon.ico').resolve())


Window.size = (1024, 600)
kv_file = Path('docx_to_html.kv')
Builder.load_file(str(kv_file.resolve()))


class Container(MDGridLayout):
    file_path = ObjectProperty()
    btn_generate = ObjectProperty()
    html_code = ObjectProperty()

    def btn_press__generate(self):

        if Path(self.file_path.text).suffix == '.docx':
            self.html_code.lexer = HtmlLexer()
            self.html_code.text = get_html(self.file_path.text)
            self.log_output.text += f'{get_time_now()} generate html > OK\n'
        else:
            self.log_output.text += f'{get_time_now()} generate html > error > not file.docx\n'

    def btn_press__copy_code(self):
        if self.html_code.text:
            # print(f'Код скопирован')
            pyperclip.copy(self.html_code.text)
            self.log_output.text += f'{get_time_now()} copy html code > OK\n'
        else:
            self.log_output.text += f'{get_time_now()} copy html code > error > not code\n'

    def btn_press__open_code(self):

        if self.html_code.text:

            file_html = save_file_html(self.html_code.text)
            print(file_html)
            webbrowser.get('windows-default').open_new_tab(f'file:///{file_html.resolve()}')
            del_old_files(BACKUP_DAYS, DIR_RESULT)
            self.log_output.text += f'{get_time_now()} open html code > OK\n'
        else:
            self.log_output.text += f'{get_time_now()} open html code > error > not code\n'


class DocxToHtml(MDApp):

    path = StringProperty()
    log = StringProperty()

    def build(self):

        self.icon = "icon.ico"

        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        Window.bind(on_drop_file=self.on_file_drop)
        c = Container()
        return c

    def on_file_drop(self, window, file_path, x, y):
        self.path = str(file_path.decode('utf-8'))
        print(self.path)

        path = Path(self.path)
        if path.suffix == '.docx':
            return self.path
        else:
            self.log += f'{get_time_now()} error > file does not have an extension > docx\n'


if __name__ == '__main__':
    DocxToHtml().run()
