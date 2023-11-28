
from bs4 import BeautifulSoup
from config import IND
from pathlib import Path

from libs.files import file_read_docx


def clear_style_attributes(html):

    cleaner = lxml.html.clean.Cleaner(
        safe_attrs_only=True, safe_attrs=frozenset())
    html = cleaner.clean_html(html)
    return html


def remove_all_attrs_except_saving(soup):
    whitelist = ['a', 'img']
    for tag in soup.find_all(True):
        if tag.name not in whitelist:
            tag.attrs = {}
        else:
            attrs = dict(tag.attrs)
            for attr in attrs:
                if attr not in ['src', 'href']:
                    del tag.attrs[attr]
    return soup


def remove_emty_tags(soup):
    for x in soup.find_all():
        if len(x.get_text(strip=True)) == 0:
            x.extract()

    return soup


def filter_tags(soup):
    for tag in soup.find_all(['html', 'body', 'div', 'span']):
        tag.unwrap()
    return soup


'''
def replace_tag(soup):

    try:

        li_first_list = soup.find_all('p', class_='MsoListParagraphCxSpFirst')

        # print(f'count li_start = {len(li_first_list)}')

        if li_first_list:

            for p in li_first_list:

                p.name = 'li'
                p.string = p.text.replace('·', '')

                # print(p)

        li_middle_list = soup.find_all('p', class_='MsoListParagraphCxSpMiddle')

        # print(f'count li_middle = {len(li_middle_list)}')

        if li_middle_list:

            for p in li_middle_list:

                p.name = 'li'
                p.string = p.text.replace('·', '')

                # print(p)

        li_last_list = soup.find_all('p', class_='MsoListParagraphCxSpLast')

        # print(f'count li_last = {len(li_last_list)}')

        if li_last_list:

            for p in li_last_list:

                p.name = 'li'
                p.string = p.text.replace('·', '')

                # ul_end = soup.new_tag("ul")
                # p.insert_after(ul_end)

                # print(p)
                # result += p

        # print(soup)

        # return BeautifulSoup(result, 'lxml')

        return soup

    except Exception as e:
        print(f'{Fore.RED}{IND} f: replace_tag -> {e}')

def set_style(soup):
    for h1 in soup.find_all('h1'):
        h1['style'] = CSS_H1

    for h2 in soup.find_all('h2'):
        h2['style'] = CSS_H2

    for h3 in soup.find_all('h3'):
        h3['style'] = CSS_H3

    for p in soup.find_all('p'):
        p['style'] = CSS_P

    for li in soup.find_all('li'):
        li['style'] = CSS_LI

    return soup
'''


def get_code_file(file):

    docx_file = Path(file)

    if (docx_file.suffix != '.docx'):
        print(f'{IND} Не обнаружил файлов (.docx)')
        file_code = 'Это не файл .docx'
    else:
        file_code = file_read_docx(docx_file)

    return file_code


# def save_files(html_code):

#     try:
#         file_txt = file_name(datetime.now(), 'txt')
#         file_html = file_name(datetime.now(), 'html')

#         path_fodler_output = Path(FOLDER_RESULT)
#         if not path_fodler_output.exists():
#             path_fodler_output.mkdir()

#         with open(f'{FOLDER_RESULT}/{file_txt}', 'w') as f1:
#             f1.write(html_code)
#         with open(f'{FOLDER_RESULT}/{file_html}', 'w') as f2:
#             f2.write(html_code)

#         print('')
#         print(f'{IND}{Fore.GREEN} file txt: /{FOLDER_RESULT}/{file_txt}')
#         print(f'{IND}{Fore.GREEN} file html: /{FOLDER_RESULT}/{file_html}')

#     except Exception:
#         print(f'\n{IND}{Fore.RED} f: save_files -> Сохранение файлов НЕ свершилось')

#     return file_html, file_txt


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


def get_html(file_docx):

    file_code = get_code_file(file_docx)
    code_result = get_html_code(file_code)

    return code_result
