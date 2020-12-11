from PyQt5.QtWidgets import QMessageBox


class Rules:
    _text = """
    чтобы получить необходимую случайную информацию сначала
    выбери что желаешь чтобы программа тебе сгенерировала: 'буквы'
    где тебе будет выдан результат в виде одной буквы русского алфавита, 
    'бросить кубики' где ты сможешь бросить до 5 кубиков и тебе сразу покажут 
    сумму твоего броска, 'да или нет', где на любой твой вопрос ответит программа абсолютно случайно
    (всё равно что перебирать лепестки цветка выбирая между двумя мыслями), для того чтобы программа
    выполняла действия нажимай на соответсвующие кнопки запуска алгоритма)
    """

    def __init__(self):
        pass

    def show_rules(self):
        msg = QMessageBox()
        msg.setWindowTitle("Правила игры")
        msg.setText(Rules._text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        x = msg.exec_()
