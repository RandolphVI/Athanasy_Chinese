init python:
    # список поддерживаемых языков в порядке их переключения,
    # начиная с того, на котором игра создавалась - None
    # языков может быть любое количество

    languages = [None, "english", "chinese"]

    # переключить язык на следующий по списку
    # по окончании списка, начинаем с начала
    def next_language():
        if _preferences.language in languages:
            i = languages.index(_preferences.language) + 1
        else:
            i = 0
        if i >= len(languages):
            i = 0
        Language(languages[i])()
    # действие для кнопок
    NextLanguage = renpy.curry(next_language)

# выбор языка при первом запуске

# label splashscreen:
    # scene bg_black
    # if persistent.lang is None:
        # menu:
            # "ENGLISH":
                # $ Language(languages[1])()
            # "РУССКИЙ":
                # $ Language(languages[0])()
        # $ persistent.lang = True
    # return
