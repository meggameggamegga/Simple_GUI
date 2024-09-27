# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setMaximumSize(QSize(1000, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(45,45,45);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color:rgb(35,35,35);")
        self.top_bar.setFrameShape(QFrame.Shape.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toogle = QFrame(self.top_bar)
        self.frame_toogle.setObjectName(u"frame_toogle")
        self.frame_toogle.setMaximumSize(QSize(100, 40))
        self.frame_toogle.setStyleSheet(u"background-color:rgb(117, 126, 255);")
        self.frame_toogle.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_toogle.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toogle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.frame_toogle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet(u"border:0px solid;\n"
"color:white;\n"
"font-weight:700;")
        icon = QIcon()
        icon.addFile(u":/fonts/menu-boxed.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toggle.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btn_toggle)


        self.horizontalLayout.addWidget(self.frame_toogle)

        self.frame_top = QFrame(self.top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"\n"
"background-color:rgba(31, 40, 56, 1);\n"
"")
        self.frame_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_top)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_top)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(130, 91, 255, 255), \n"
"        stop:1 rgba(85, 57, 204, 255)\n"
"    );\n"
"font-weight:700;\n"
"font-size:25px;\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(100, 0))
        self.frame_left_menu.setMaximumSize(QSize(100, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color:rgba(31, 40, 56, 1);")
        self.frame_left_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setStyleSheet(u"")
        self.frame_top_menus.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.btn_menu_1 = QPushButton(self.frame_top_menus)
        self.btn_menu_1.setObjectName(u"btn_menu_1")
        self.btn_menu_1.setMinimumSize(QSize(0, 40))
        self.btn_menu_1.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color:rgba(31, 40, 56, 1);\n"
"	border:0px solid;\n"
"	font-weight:900;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(85,170,255);\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:focus {\n"
"	background-color:rgb(85,170,255);\n"
"	border-radius:15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_menu_1)

        self.btn_menu_2 = QPushButton(self.frame_top_menus)
        self.btn_menu_2.setObjectName(u"btn_menu_2")
        self.btn_menu_2.setMinimumSize(QSize(0, 40))
        self.btn_menu_2.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color:rgba(31, 40, 56, 1);\n"
"	border:0px solid;\n"
"	font-weight:900;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(85,170,255);\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:focus {\n"
"	background-color:rgb(85,170,255);\n"
"	border-radius:15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_menu_2)

        self.btn_menu_3 = QPushButton(self.frame_top_menus)
        self.btn_menu_3.setObjectName(u"btn_menu_3")
        self.btn_menu_3.setMinimumSize(QSize(0, 40))
        self.btn_menu_3.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color:rgba(31, 40, 56, 1);\n"
"	border:0px solid;\n"
"	font-weight:900;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(85,170,255);\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:focus {\n"
"	background-color:rgb(85,170,255);\n"
"	border-radius:15px;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_menu_3)


        self.verticalLayout_4.addWidget(self.frame_top_menus, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_bottom_info = QFrame(self.frame_left_menu)
        self.frame_bottom_info.setObjectName(u"frame_bottom_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_bottom_info.sizePolicy().hasHeightForWidth())
        self.frame_bottom_info.setSizePolicy(sizePolicy1)
        self.frame_bottom_info.setMinimumSize(QSize(0, 50))
        self.frame_bottom_info.setMaximumSize(QSize(16777215, 50))
        self.frame_bottom_info.setStyleSheet(u"background-color: rgb(55, 62, 122);")
        self.frame_bottom_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_bottom_info.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_bottom_info)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_icons = QFrame(self.frame_bottom_info)
        self.frame_bottom_icons.setObjectName(u"frame_bottom_icons")
        self.frame_bottom_icons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_bottom_icons.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_bottom_icons)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_bottom_icons)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/fonts/youtube_activity_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg"))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_2)


        self.verticalLayout_6.addWidget(self.frame_bottom_icons)


        self.verticalLayout_4.addWidget(self.frame_bottom_info)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setMaximumSize(QSize(16777215, 16777215))
        self.frame_pages.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.page_check_acc = QWidget()
        self.page_check_acc.setObjectName(u"page_check_acc")
        self.horizontalLayout_4 = QHBoxLayout(self.page_check_acc)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.page_check_acc)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(0, 0))
        self.left_side_menu.setMaximumSize(QSize(698, 458))
        self.left_side_menu.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 36, 51, 255), stop:1 rgba(49, 64, 90, 255));")
        self.left_side_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_side_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.left_side_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_skin_1 = QFrame(self.left_side_menu)
        self.frame_skin_1.setObjectName(u"frame_skin_1")
        self.frame_skin_1.setStyleSheet(u"background-color: transparent;\n"
"border:2px solid rgba(72, 103, 148, 0.35);\n"
"border-radius:10px;")
        self.frame_skin_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_skin_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_skin_1)
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.label_skin_0 = QLabel(self.frame_skin_1)
        self.label_skin_0.setObjectName(u"label_skin_0")
        self.label_skin_0.setMinimumSize(QSize(205, 93))
        self.label_skin_0.setMaximumSize(QSize(16777215, 16777215))
        self.label_skin_0.setStyleSheet(u"background-color:rgba(45, 58, 80, 1);\n"
"border:none;")

        self.verticalLayout_7.addWidget(self.label_skin_0)

        self.comboBox = QComboBox(self.frame_skin_1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color:white;")

        self.verticalLayout_7.addWidget(self.comboBox)


        self.horizontalLayout_15.addWidget(self.frame_skin_1)

        self.frame_skin_2 = QFrame(self.left_side_menu)
        self.frame_skin_2.setObjectName(u"frame_skin_2")
        self.frame_skin_2.setStyleSheet(u"background-color: transparent;\n"
"border:2px solid rgba(72, 103, 148, 0.35);\n"
"border-radius:10px;")
        self.frame_skin_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_skin_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_skin_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_skin_1 = QLabel(self.frame_skin_2)
        self.label_skin_1.setObjectName(u"label_skin_1")
        self.label_skin_1.setStyleSheet(u"background-color:rgba(45, 58, 80, 1);\n"
"border:none;")

        self.verticalLayout_8.addWidget(self.label_skin_1)

        self.comboBox_2 = QComboBox(self.frame_skin_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"color:white;")

        self.verticalLayout_8.addWidget(self.comboBox_2)


        self.horizontalLayout_15.addWidget(self.frame_skin_2)

        self.frame_skin_3 = QFrame(self.left_side_menu)
        self.frame_skin_3.setObjectName(u"frame_skin_3")
        self.frame_skin_3.setStyleSheet(u"background-color: transparent;\n"
"border:2px solid rgba(72, 103, 148, 0.35);\n"
"border-radius:10px;")
        self.frame_skin_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_skin_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_skin_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_skin_2 = QLabel(self.frame_skin_3)
        self.label_skin_2.setObjectName(u"label_skin_2")
        self.label_skin_2.setStyleSheet(u"background-color:rgba(45, 58, 80, 1);\n"
"border:none;")

        self.verticalLayout_9.addWidget(self.label_skin_2)

        self.comboBox_3 = QComboBox(self.frame_skin_3)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"color:white;")

        self.verticalLayout_9.addWidget(self.comboBox_3)


        self.horizontalLayout_15.addWidget(self.frame_skin_3)


        self.gridLayout.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_skin_7 = QFrame(self.left_side_menu)
        self.frame_skin_7.setObjectName(u"frame_skin_7")
        self.frame_skin_7.setStyleSheet(u"background-color: transparent;\n"
"border:2px solid rgba(72, 103, 148, 0.35);\n"
"border-radius:10px;")
        self.frame_skin_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_skin_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_skin_7)
        self.verticalLayout_25.setSpacing(9)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, 9, 9, 9)
        self.label_skin_6 = QLabel(self.frame_skin_7)
        self.label_skin_6.setObjectName(u"label_skin_6")
        self.label_skin_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_skin_6.setStyleSheet(u"background-color:rgba(45, 58, 80, 1);\n"
"border:none;")

        self.verticalLayout_25.addWidget(self.label_skin_6)

        self.comboBox_7 = QComboBox(self.frame_skin_7)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setStyleSheet(u"color:white;")

        self.verticalLayout_25.addWidget(self.comboBox_7)


        self.horizontalLayout_28.addWidget(self.frame_skin_7)

        self.frame_skin_8 = QFrame(self.left_side_menu)
        self.frame_skin_8.setObjectName(u"frame_skin_8")
        self.frame_skin_8.setStyleSheet(u"background-color: transparent;\n"
"border:2px solid rgba(72, 103, 148, 0.35);\n"
"border-radius:10px;")
        self.frame_skin_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_skin_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_skin_8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_skin_7 = QLabel(self.frame_skin_8)
        self.label_skin_7.setObjectName(u"label_skin_7")
        self.label_skin_7.setStyleSheet(u"background-color:rgba(45, 58, 80, 1);\n"
"border:none;")

        self.verticalLayout_26.addWidget(self.label_skin_7)

        self.comboBox_8 = QComboBox(self.frame_skin_8)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setStyleSheet(u"color:white;")

        self.verticalLayout_26.addWidget(self.comboBox_8)


        self.horizontalLayout_28.addWidget(self.frame_skin_8)

        self.frane_skin_9 = QFrame(self.left_side_menu)
        self.frane_skin_9.setObjectName(u"frane_skin_9")
        self.frane_skin_9.setStyleSheet(u"background-color: transparent;\n"
"border:2px solid rgba(72, 103, 148, 0.35);\n"
"border-radius:10px;")
        self.frane_skin_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frane_skin_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frane_skin_9)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_skin_8 = QLabel(self.frane_skin_9)
        self.label_skin_8.setObjectName(u"label_skin_8")
        self.label_skin_8.setStyleSheet(u"background-color:rgba(45, 58, 80, 1);\n"
"border:none;")

        self.verticalLayout_27.addWidget(self.label_skin_8)

        self.comboBox_9 = QComboBox(self.frane_skin_9)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setStyleSheet(u"color:white;")

        self.verticalLayout_27.addWidget(self.comboBox_9)


        self.horizontalLayout_28.addWidget(self.frane_skin_9)


        self.gridLayout.addLayout(self.horizontalLayout_28, 2, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_skin_4 = QFrame(self.left_side_menu)
        self.frame_skin_4.setObjectName(u"frame_skin_4")
        self.frame_skin_4.setStyleSheet(u"background-color: transparent;\n"
"border:2px solid rgba(72, 103, 148, 0.35);\n"
"border-radius:10px;")
        self.frame_skin_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_skin_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_skin_4)
        self.verticalLayout_22.setSpacing(9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, 9, 9, 9)
        self.label_skin_3 = QLabel(self.frame_skin_4)
        self.label_skin_3.setObjectName(u"label_skin_3")
        self.label_skin_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_skin_3.setStyleSheet(u"background-color:rgba(45, 58, 80, 1);\n"
"border:none;")

        self.verticalLayout_22.addWidget(self.label_skin_3)

        self.comboBox_4 = QComboBox(self.frame_skin_4)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"color:white;")

        self.verticalLayout_22.addWidget(self.comboBox_4)


        self.horizontalLayout_24.addWidget(self.frame_skin_4)

        self.frame_skin_5 = QFrame(self.left_side_menu)
        self.frame_skin_5.setObjectName(u"frame_skin_5")
        self.frame_skin_5.setStyleSheet(u"background-color: transparent;\n"
"border:2px solid rgba(72, 103, 148, 0.35);\n"
"border-radius:10px;")
        self.frame_skin_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_skin_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_skin_5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_skin_4 = QLabel(self.frame_skin_5)
        self.label_skin_4.setObjectName(u"label_skin_4")
        self.label_skin_4.setStyleSheet(u"background-color:rgba(45, 58, 80, 1);\n"
"border:none;")

        self.verticalLayout_23.addWidget(self.label_skin_4)

        self.comboBox_5 = QComboBox(self.frame_skin_5)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"color:white;")

        self.verticalLayout_23.addWidget(self.comboBox_5)


        self.horizontalLayout_24.addWidget(self.frame_skin_5)

        self.frame_skin_6 = QFrame(self.left_side_menu)
        self.frame_skin_6.setObjectName(u"frame_skin_6")
        self.frame_skin_6.setStyleSheet(u"background-color: transparent;\n"
"border:2px solid rgba(72, 103, 148, 0.35);\n"
"border-radius:10px;")
        self.frame_skin_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_skin_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_skin_6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_skin_5 = QLabel(self.frame_skin_6)
        self.label_skin_5.setObjectName(u"label_skin_5")
        self.label_skin_5.setStyleSheet(u"background-color:rgba(45, 58, 80, 1);\n"
"border:none;")

        self.verticalLayout_24.addWidget(self.label_skin_5)

        self.comboBox_6 = QComboBox(self.frame_skin_6)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet(u"color:white;")

        self.verticalLayout_24.addWidget(self.comboBox_6)


        self.horizontalLayout_24.addWidget(self.frame_skin_6)


        self.gridLayout.addLayout(self.horizontalLayout_24, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.left_side_menu)

        self.right_side_menu = QFrame(self.page_check_acc)
        self.right_side_menu.setObjectName(u"right_side_menu")
        self.right_side_menu.setMaximumSize(QSize(200, 16777215))
        self.right_side_menu.setStyleSheet(u"\n"
"background-color:rgba(31, 40, 56, 1);\n"
"")
        self.right_side_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_side_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.right_side_menu)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_status = QLabel(self.right_side_menu)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setStyleSheet(u"color:white;\n"
"font-size:25px;\n"
"font-weight:800;")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_status)

        self.frame = QFrame(self.right_side_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u" QProgressBar {\n"
"                border: 2px solid #5e5e5e;\n"
"                border-radius: 5px;\n"
"                background-color: #1e1e1e;\n"
"                text-align: center;\n"
"                color: white;\n"
"                font-weight: bold;\n"
"            }\n"
"QProgressBar::chunk {\n"
"   background-color: #00aaff;\n"
"   width: 10px;\n"
"   margin: 0.5px;\n"
"}")
        self.progressBar.setValue(0)

        self.verticalLayout_11.addWidget(self.progressBar)

        self.btn_activate = QPushButton(self.frame)
        self.btn_activate.setObjectName(u"btn_activate")
        self.btn_activate.setMinimumSize(QSize(0, 50))
        self.btn_activate.setStyleSheet(u"QPushButton {\n"
"        background-color: #1e1e1e;\n"
"        color: white;\n"
"        border: 2px solid #5e5e5e;\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"        font-size: 16px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #3e3e3e;\n"
"        border: 2px solid #00aaff;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #00aaff;\n"
"        border: 2px solid #007acc;\n"
"    }")

        self.verticalLayout_11.addWidget(self.btn_activate)


        self.verticalLayout_10.addWidget(self.frame)


        self.horizontalLayout_4.addWidget(self.right_side_menu)

        self.pages_widget.addWidget(self.page_check_acc)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(28, 36, 51, 255), stop:1 rgba(49, 64, 90, 255));")
        self.frame_2 = QFrame(self.page_settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 20, 521, 81))
        self.frame_2.setStyleSheet(u"background-color:transparent;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight:800;\n"
"font-size:25px;\n"
"color:white;\n"
"background-color:transparent;")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color:transparent;")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.pages_widget.addWidget(self.page_settings)
        self.page_about_us = QWidget()
        self.page_about_us.setObjectName(u"page_about_us")
        self.label_5 = QLabel(self.page_about_us)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 110, 401, 181))
        self.pages_widget.addWidget(self.page_about_us)

        self.verticalLayout_5.addWidget(self.pages_widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Valorant Skin Changer BETA V.1.0.1", None))
        self.btn_menu_1.setText(QCoreApplication.translate("MainWindow", u"Change Skins", None))
        self.btn_menu_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_menu_3.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.label_2.setText("")
        self.label_skin_0.setText(QCoreApplication.translate("MainWindow", u"ICON SKIN", None))
        self.label_skin_1.setText(QCoreApplication.translate("MainWindow", u"ICON SKIN", None))
        self.label_skin_2.setText(QCoreApplication.translate("MainWindow", u"ICON SKIN", None))
        self.label_skin_6.setText(QCoreApplication.translate("MainWindow", u"ICON SKIN", None))
        self.label_skin_7.setText(QCoreApplication.translate("MainWindow", u"ICON SKIN", None))
        self.label_skin_8.setText(QCoreApplication.translate("MainWindow", u"ICON SKIN", None))
        self.label_skin_3.setText(QCoreApplication.translate("MainWindow", u"ICON SKIN", None))
        self.label_skin_4.setText(QCoreApplication.translate("MainWindow", u"ICON SKIN", None))
        self.label_skin_5.setText(QCoreApplication.translate("MainWindow", u"ICON SKIN", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.btn_activate.setText(QCoreApplication.translate("MainWindow", u"Inject", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Path to valorant foilder", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PAGE_ABOUT_US", None))
    # retranslateUi

