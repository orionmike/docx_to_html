from datetime import datetime

from config import IND


def time_execute(start_time) -> None:

    end = datetime.now()
    total = end - start_time
    total_str = total  # strftime('%Y-%m-%d %H:%M:%S')
    print(f'{IND} Время выполнения операции: {total_str}')


def get_time_now() -> str:
    return datetime.now().strftime("%H:%M:%S")


def dt_doc(datetime) -> str:
    dt = f'{datetime.strftime("%Y-%m-%d_%H-%M-%S")}__'
    return dt


def get_file_name() -> str:
    file_name = None
    dt = datetime.now()
    file_name = f'{dt.strftime("%Y-%m-%d_%H-%M-%S")}.html'

    return file_name
