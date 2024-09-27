from PySide6.QtCore import QPropertyAnimation, QTimer
from PySide6 import QtCore

from main import MainWindow

COUNTER = 0


class UiFunctions(MainWindow):

    def toggleMenu(self, maxWidth):
        # Получаем ширину левого меню
        width = self.ui.frame_left_menu.width()
        maxExtend = maxWidth
        standard = 100

        # Если текущий размер онка (когда нажали на кнопку) стоит по дефолту(в обычно режиме)
        if width == 100:
            # То устанавливается значение , на которое будет расскрываться меню
            widthExtended = maxExtend
        else:
            # Если она уже расскрыта
            # То ставится значение в обычном режиме
            widthExtended = standard

        # Анимация leftBar
        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b'minimumWidth')
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.setEndValue(widthExtended)
        self.animation.start()

    # Когда идет нажатие на кномпу , отображаем нужную страницу
    def item_btn_choised(self, index):
        self.ui.pages_widget.setCurrentIndex(index)


    def start_loader(self):
        self.timer.start(35)
        QTimer.singleShot(1500, lambda: self.ui.label_status.setText('Find data...'))
        QTimer.singleShot(5500, lambda: self.ui.label_status.setText('Change skins...'))

    def activate_change(self):
        if self.ui.progressBar.value() == 100:
            self.ui.progressBar.setValue(0)

        global COUNTER
        COUNTER += 0.5
        self.ui.progressBar.setValue(COUNTER)
        if COUNTER > 100:
            self.timer.stop()
            self.ui.label_status.setText('Skins injected!')
            #self.close()
            COUNTER = 0

