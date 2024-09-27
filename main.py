import os
import sys

from PySide6.QtCore import *
from PySide6 import QtGui
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6 import QtWidgets

from main_window import Ui_MainWindow
from ui_funcs import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_toggle.setCheckable(True)
        self.ui.btn_toggle.clicked.connect(lambda: UiFunctions.toggleMenu(self, 250))

        self.timer = QTimer()
        self.timer.timeout.connect(lambda :UiFunctions.activate_change(self))

        self.ui.btn_activate.clicked.connect(lambda:UiFunctions.start_loader(self))

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet('border-radius:10px;')

        self.left_bar_items = [
            {'name': 'Change Skins'},
            {'name': 'About Us'},
            {'name': 'Settings'},
        ]

        self.ui.btn_menu_1.clicked.connect(lambda: UiFunctions.item_btn_choised(self, 0))
        self.ui.btn_menu_2.clicked.connect(lambda: UiFunctions.item_btn_choised(self, 1))
        self.ui.btn_menu_3.clicked.connect(lambda: UiFunctions.item_btn_choised(self, 2))
        self.set_icons_skins()

        [self.ui.comboBox.addItem(el.split(".")[0]) for el in os.listdir('./photos/0')]
        [self.ui.comboBox_2.addItem(el.split(".")[0]) for el in os.listdir('./photos/1')]
        [self.ui.comboBox_3.addItem(el.split(".")[0]) for el in os.listdir('./photos/2')]
        [self.ui.comboBox_4.addItem(el.split(".")[0]) for el in os.listdir('./photos/3')]
        [self.ui.comboBox_5.addItem(el.split(".")[0]) for el in os.listdir('./photos/4')]
        [self.ui.comboBox_6.addItem(el.split(".")[0]) for el in os.listdir('./photos/5')]
        [self.ui.comboBox_7.addItem(el.split(".")[0]) for el in os.listdir('./photos/6')]
        [self.ui.comboBox_8.addItem(el.split(".")[0]) for el in os.listdir('./photos/7')]
        [self.ui.comboBox_9.addItem(el.split(".")[0]) for el in os.listdir('./photos/8')]

        self.connect_combo_boxes()


    def set_icons_skins(self):
        PHOTO_PATH = './photos'
        skin_labels = self.ui.left_side_menu.findChildren(QLabel)
        path_categories = os.listdir(PHOTO_PATH)
        for skin_label in range(0, len(skin_labels)):
            photo_categories = os.listdir(PHOTO_PATH + f'/{path_categories[skin_label]}')
            pixmap = QPixmap(f'./photos/{path_categories[skin_label]}/{photo_categories[0]}').scaled(155, 45)
            skin_labels[skin_label].setPixmap(pixmap)
            skin_labels[skin_label].setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def connect_combo_boxes(self):
        '''
               Найти все фреймы и итерироваться по ним

               :return:
               '''

        frames = self.ui.left_side_menu.findChildren(QFrame)
        for block in frames:
            if block.findChild(QComboBox):
                cmb_box = block.findChildren(QComboBox)[0]
                lbl_img = block.findChildren(QLabel)[0]
                cmb_box.currentIndexChanged.connect(
                    lambda _, cmb_box=cmb_box, lbl_img=lbl_img: self.combo_box_switch(cmb_box, lbl_img))

        #    if isinstance(block,QFrame):
        #        if isinstance(block.findChild(QComboBox),QComboBox):
        #            print(block)
        # combo_boxs = self.ui.left_side_menu.findChildren(QComboBox)
        # for i,combo_box in enumerate(combo_boxs):
        #     combo_box.currentIndexChanged.connect(lambda _, index=i,obj=combo_box: self.combo_box_swtich(index,obj))

    def combo_box_switch(self, obj, lbl_img):
        id_skin = lbl_img.objectName().split('_')[-1]
        path = f'./photos/{id_skin}'
        skin_text = obj.currentText()
        current_photo = path + f'/{skin_text}.jpg'
        #print(current_photo)
        pixmap = QPixmap(current_photo).scaled(155, 45)
        lbl_img.setPixmap(pixmap)
        lbl_img.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
