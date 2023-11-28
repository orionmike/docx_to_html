
from pathlib import Path

from bs4 import BeautifulSoup

from config import IND
from libs.files import file_read_docx


def remove_emty_tags(soup):
    for x in soup.find_all():
        if len(x.get_text(strip=True)) == 0:
            x.extract()
    return soup


def filter_tags(soup):
    for tag in soup.find_all(['html', 'body', 'div', 'span']):
        tag.unwrap()
    return soup


def get_code_file(path_file: str) -> str:

    docx_file = Path(path_file)

    if (docx_file.suffix != '.docx'):
        print(f'{IND} Не обнаружил файлов (.docx)')
        file_code = 'Это не файл .docx'
    else:
        file_code = file_read_docx(docx_file)

    return file_code


def get_html_code(content):

    try:
        html_code = None

        if content:
            soup = BeautifulSoup(str(content), 'lxml')
            soup = remove_emty_tags(soup)
            soup = filter_tags(soup)
            text = str(soup)

            html_code = text.replace(' ', '')
            # html_code = soup.prettify()
            print(f'{IND} create final code: OK')
        else:
            print(f'{IND} f:get_html_code -> not data')

    except Exception as e:
        print(f'{IND} get_html_code: {e}')

    return html_code


def get_html(path_file_docx: str):

    file_code = get_code_file(path_file_docx)
    code_result = get_html_code(file_code)

    return code_result
