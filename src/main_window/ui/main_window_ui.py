# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(728, 654)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 102, 102, 255), stop:1 rgba(0, 191, 255, 255));\n"
"font-family: Roboto;")
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout_3 = QVBoxLayout(self.main_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.header_frame = QFrame(self.main_widget)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QSize(0, 270))
        self.header_frame.setMaximumSize(QSize(16777215, 270))
        self.header_frame.setStyleSheet(u"background: none;")
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.balance_frame = QFrame(self.header_frame)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setMinimumSize(QSize(300, 270))
        self.balance_frame.setMaximumSize(QSize(300, 270))
        self.balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 8, 16, 16)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.current_period_btn = QPushButton(self.balance_frame)
        self.current_period_btn.setObjectName(u"current_period_btn")
        self.current_period_btn.setStyleSheet(u"QPushButton {\n"
"    color: #c8fafa;\n"
"    border: none;\n"
"    background: transparent;\n"
"    font-size: 13px;\n"
"    text-decoration: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #185353;\n"
"}\n"
"QPushButton:checked {\n"
"    font-weight: bold;\n"
"	text-decoration: underline;\n"
"}")
        self.current_period_btn.setCheckable(True)
        self.current_period_btn.setChecked(True)
        self.current_period_btn.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.current_period_btn)

        self.previous_period_btn = QPushButton(self.balance_frame)
        self.previous_period_btn.setObjectName(u"previous_period_btn")
        self.previous_period_btn.setStyleSheet(u"QPushButton {\n"
"    color: #c8fafa;\n"
"    border: none;\n"
"    background: transparent;\n"
"    font-size: 13px;\n"
"    text-decoration: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #185353;\n"
"}\n"
"QPushButton:checked {\n"
"    font-weight: bold;\n"
"	text-decoration: underline;\n"
"}")
        self.previous_period_btn.setCheckable(True)
        self.previous_period_btn.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.previous_period_btn)

        self.year_period_btn = QPushButton(self.balance_frame)
        self.year_period_btn.setObjectName(u"year_period_btn")
        self.year_period_btn.setStyleSheet(u"QPushButton {\n"
"    color: #c8fafa;\n"
"    border: none;\n"
"    background: transparent;\n"
"    font-size: 13px;\n"
"    text-decoration: none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #185353;\n"
"}\n"
"QPushButton:checked {\n"
"    font-weight: bold;\n"
"	text-decoration: underline;\n"
"}")
        self.year_period_btn.setCheckable(True)
        self.year_period_btn.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.year_period_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.balance_widget = QWidget(self.balance_frame)
        self.balance_widget.setObjectName(u"balance_widget")
        self.balance_widget.setStyleSheet(u"border: none;\n"
"border-radius: none;\n"
"background: none;")
        self.verticalLayout_6 = QVBoxLayout(self.balance_widget)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 2, 0, 2)
        self.balance_container = QHBoxLayout()
        self.balance_container.setSpacing(4)
        self.balance_container.setObjectName(u"balance_container")
        self.balance_icon = QLabel(self.balance_widget)
        self.balance_icon.setObjectName(u"balance_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.balance_icon.sizePolicy().hasHeightForWidth())
        self.balance_icon.setSizePolicy(sizePolicy1)
        self.balance_icon.setMinimumSize(QSize(28, 28))
        self.balance_icon.setMaximumSize(QSize(28, 28))
        self.balance_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.balance_container.addWidget(self.balance_icon)

        self.balance_title_lbl = QLabel(self.balance_widget)
        self.balance_title_lbl.setObjectName(u"balance_title_lbl")
        self.balance_title_lbl.setStyleSheet(u"color: #c8fafa;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.balance_container.addWidget(self.balance_title_lbl)


        self.verticalLayout_6.addLayout(self.balance_container)

        self.balance_lbl = QLabel(self.balance_widget)
        self.balance_lbl.setObjectName(u"balance_lbl")
        self.balance_lbl.setStyleSheet(u"color: #c8fafa;\n"
"font-size: 28px;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.verticalLayout_6.addWidget(self.balance_lbl)


        self.verticalLayout.addWidget(self.balance_widget)

        self.outcome_widget = QWidget(self.balance_frame)
        self.outcome_widget.setObjectName(u"outcome_widget")
        self.verticalLayout_5 = QVBoxLayout(self.outcome_widget)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(8, 4, 4, 4)
        self.outcome_container = QHBoxLayout()
        self.outcome_container.setSpacing(4)
        self.outcome_container.setObjectName(u"outcome_container")
        self.outcome_container.setContentsMargins(-1, 0, -1, -1)
        self.outcome_icon = QLabel(self.outcome_widget)
        self.outcome_icon.setObjectName(u"outcome_icon")
        sizePolicy1.setHeightForWidth(self.outcome_icon.sizePolicy().hasHeightForWidth())
        self.outcome_icon.setSizePolicy(sizePolicy1)
        self.outcome_icon.setMinimumSize(QSize(24, 24))
        self.outcome_icon.setMaximumSize(QSize(24, 24))
        self.outcome_icon.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.outcome_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.outcome_container.addWidget(self.outcome_icon)

        self.outcome_lbl = QLabel(self.outcome_widget)
        self.outcome_lbl.setObjectName(u"outcome_lbl")
        self.outcome_lbl.setStyleSheet(u"color: #c8fafa;\n"
"font-size: 16px;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")

        self.outcome_container.addWidget(self.outcome_lbl)


        self.verticalLayout_5.addLayout(self.outcome_container)

        self.outcome_balance_lbl = QLabel(self.outcome_widget)
        self.outcome_balance_lbl.setObjectName(u"outcome_balance_lbl")
        self.outcome_balance_lbl.setStyleSheet(u"color: #c8fafa;\n"
"font-size: 22px;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.verticalLayout_5.addWidget(self.outcome_balance_lbl)


        self.verticalLayout.addWidget(self.outcome_widget)

        self.income_widget = QWidget(self.balance_frame)
        self.income_widget.setObjectName(u"income_widget")
        self.verticalLayout_4 = QVBoxLayout(self.income_widget)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(8, 4, 4, 4)
        self.income_container = QHBoxLayout()
        self.income_container.setSpacing(4)
        self.income_container.setObjectName(u"income_container")
        self.income_container.setContentsMargins(-1, 0, -1, -1)
        self.income_icon = QLabel(self.income_widget)
        self.income_icon.setObjectName(u"income_icon")
        sizePolicy1.setHeightForWidth(self.income_icon.sizePolicy().hasHeightForWidth())
        self.income_icon.setSizePolicy(sizePolicy1)
        self.income_icon.setMinimumSize(QSize(24, 24))
        self.income_icon.setMaximumSize(QSize(24, 24))
        self.income_icon.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.income_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.income_container.addWidget(self.income_icon)

        self.income_lbl = QLabel(self.income_widget)
        self.income_lbl.setObjectName(u"income_lbl")
        self.income_lbl.setStyleSheet(u"color: #c8fafa;\n"
"font-size: 16px;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.income_container.addWidget(self.income_lbl)


        self.verticalLayout_4.addLayout(self.income_container)

        self.income_balance_lbl = QLabel(self.income_widget)
        self.income_balance_lbl.setObjectName(u"income_balance_lbl")
        self.income_balance_lbl.setStyleSheet(u"color: #c8fafa;\n"
"font-size: 22px;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.verticalLayout_4.addWidget(self.income_balance_lbl)


        self.verticalLayout.addWidget(self.income_widget)

        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout.addWidget(self.balance_frame)

        self.category_frame = QFrame(self.header_frame)
        self.category_frame.setObjectName(u"category_frame")
        self.category_frame.setMinimumSize(QSize(0, 270))
        self.category_frame.setMaximumSize(QSize(16777215, 270))
        self.category_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;")
        self.verticalLayout_2 = QVBoxLayout(self.category_frame)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.title_container = QHBoxLayout()
        self.title_container.setObjectName(u"title_container")
        self.category_title_lbl = QLabel(self.category_frame)
        self.category_title_lbl.setObjectName(u"category_title_lbl")
        self.category_title_lbl.setStyleSheet(u"color: #c8fafa;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.title_container.addWidget(self.category_title_lbl)

        self.category_edit_btn = QPushButton(self.category_frame)
        self.category_edit_btn.setObjectName(u"category_edit_btn")
        self.category_edit_btn.setMinimumSize(QSize(24, 24))
        self.category_edit_btn.setMaximumSize(QSize(24, 24))
        self.category_edit_btn.setStyleSheet(u"color: #c8fafa;\n"
"width: 230px;\n"
"height: 50px;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.category_edit_btn.setIconSize(QSize(24, 24))

        self.title_container.addWidget(self.category_edit_btn)


        self.verticalLayout_2.addLayout(self.title_container)

        self.outcome_frame = QFrame(self.category_frame)
        self.outcome_frame.setObjectName(u"outcome_frame")
        self.outcome_frame.setStyleSheet(u"background: none;\n"
"border: none;")
        self.outcome_layout = QHBoxLayout(self.outcome_frame)
        self.outcome_layout.setSpacing(0)
        self.outcome_layout.setObjectName(u"outcome_layout")
        self.outcome_layout.setContentsMargins(4, 4, 4, 4)

        self.verticalLayout_2.addWidget(self.outcome_frame)

        self.income_frame = QFrame(self.category_frame)
        self.income_frame.setObjectName(u"income_frame")
        self.income_frame.setStyleSheet(u"background: none;\n"
"border: none;")
        self.income_layout = QHBoxLayout(self.income_frame)
        self.income_layout.setSpacing(0)
        self.income_layout.setObjectName(u"income_layout")
        self.income_layout.setContentsMargins(4, 4, 4, 4)

        self.verticalLayout_2.addWidget(self.income_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.category_frame)


        self.verticalLayout_3.addWidget(self.header_frame)

        self.buttons_container = QHBoxLayout()
        self.buttons_container.setObjectName(u"buttons_container")
        self.new_btn = QPushButton(self.main_widget)
        self.new_btn.setObjectName(u"new_btn")
        self.new_btn.setStyleSheet(u"QPushButton {\n"
"color: #c8fafa;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;\n"
"width: 230px;\n"
"height: 50px;\n"
"font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"\n"
"")
        self.new_btn.setIconSize(QSize(24, 24))

        self.buttons_container.addWidget(self.new_btn)

        self.edit_btn = QPushButton(self.main_widget)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setStyleSheet(u"QPushButton {\n"
"color: #c8fafa;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;\n"
"width: 230px;\n"
"height: 50px;\n"
"font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"\n"
"")
        self.edit_btn.setIconSize(QSize(24, 24))

        self.buttons_container.addWidget(self.edit_btn)

        self.delete_btn = QPushButton(self.main_widget)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setStyleSheet(u"QPushButton {\n"
"color: #c8fafa;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 6px;\n"
"width: 230px;\n"
"height: 50px;\n"
"font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"\n"
"")
        self.delete_btn.setIconSize(QSize(24, 24))

        self.buttons_container.addWidget(self.delete_btn)


        self.verticalLayout_3.addLayout(self.buttons_container)

        self.table_container = QTableView(self.main_widget)
        self.table_container.setObjectName(u"table_container")
        self.table_container.setMinimumSize(QSize(0, 200))
        self.table_container.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid  rgba(255, 255, 255, 40);\n"
"border-bottom-left-radius: 6px;\n"
"border-bottom-right-radius: 6px;\n"
"}")
        self.table_container.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_container.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_container.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_container.setShowGrid(False)
        self.table_container.setSortingEnabled(True)
        self.table_container.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.table_container)

        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Finance tracker", None))
        self.current_period_btn.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.previous_period_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.year_period_btn.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434", None))
        self.balance_icon.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.balance_title_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.balance_lbl.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.outcome_icon.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.outcome_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u0442\u044b", None))
        self.outcome_balance_lbl.setText(QCoreApplication.translate("MainWindow", u"-1000", None))
        self.income_icon.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.income_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        self.income_balance_lbl.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.category_title_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.category_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.new_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e", None))
    # retranslateUi

