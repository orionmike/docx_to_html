import time
from pathlib import Path

import mammoth

from config import DIR_RESULT, IND, logger
from libs.utils import get_file_name


def file_read(file: Path) -> str:
    with open(file, 'r') as f:
        result = f.read()

    return result


def file_read_docx(file: Path):
    with open(file, 'rb') as f:
        result = mammoth.convert_to_html(f)  # style_map=custom_styles

    return result.value


def save_file_html(html_code: str) -> None:

    try:
        file_name = get_file_name()
        with open(f'{DIR_RESULT}/{file_name}', 'w') as f:
            f.write(html_code)
        return Path(f'{DIR_RESULT}/{file_name}')
    except Exception as e:
        logger.error(f'f: save_file_html -> {e}')


def del_old_files(days: int, path: Path) -> None:
    try:
        current_time = time.time()
        path_folder = Path(path)
        file_list = path_folder.iterdir()

        for file in file_list:
            if file.stat().st_mtime < current_time - days * 86400:  # неделя
                print(f'{IND} Удален старый файл: {file}')
                file.unlink()

    except Exception:
        logger.error(f'{IND} Не смог удалить старые файлы')
