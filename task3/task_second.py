file_names = ['Apple', 'Facebook', 'Yandex', 'Vk', 'EpicGames', 'Kaspersky']


def define_len():
    file_names_wtout_duplicates = []
    for file in file_names:
        file = file.lower()
        new_str = ''
        for letter in file:
            if letter.isalpha() and letter not in new_str:
                new_str += letter
            else:
                new_str += '_'
        file_names_wtout_duplicates.append(new_str)
    max_len = len(max(file_names_wtout_duplicates, key=len))
    new_file_names = []
    for file in file_names_wtout_duplicates:
        if len(file) <= max_len:
            new_file_names.append(file.ljust(max_len, '_'))
    return print(*new_file_names, sep=', ', end='.')
