# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os
from pathlib import Path


def home(end_name: str, count_sequence_number: int, start_expansions: str,
         end_expansions: str, slice_name: list[int, int],
         directory=Path().cwd()):
    start_number = 1
    start_slice, end_slace = slice_name
    for dirs, folders, files in os.walk(directory):
        for i, file in enumerate(files):
            if file.endswith(start_expansions):
                old_name = Path(dirs) / file
                old_name.rename(
                    f'{dirs}\{file[start_slice:end_slace]}{end_name}{str(start_number).zfill(count_sequence_number)}.{end_expansions}')
                start_number += 1
