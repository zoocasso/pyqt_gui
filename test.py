import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
import pandas as pd

form_class = uic.loadUiType("main_test.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.Qbtn.clicked.connect(self.test)


    def test():
        print(1)
        
    # def create_table_widget(self, widget, df):
    #     widget.setRowCount(len(df.index))
    #     widget.setColumnCount(len(df.columns))
    #     widget.setHorizontalHeaderLabels(df.columns)
    #     widget.setVerticalHeaderLabels(df.index)

    #     for row_index, row in enumerate(df.index):
    #         for col_index, column in enumerate(df.columns):
    #             value = df.loc[row][column]
                
    #             item = pyqt6.QTableWidgetItem(str(value))
                
    #             widget.setItem(row_index, col_index, item)

    # def slot_button_load(self, state, widget):
    #     filename = pyqt6.QFileDialog.getOpenFileName(self, '', './','csv(*.csv)')

    #     if filename[0]:
    #         df = pd.read_csv(filename[0], index_col = 0)
    #         self.create_table_widget(widget, calc_df)

    # def slot_button_save(self, state, widget):
    #     filename = pyqt6.QFileDialog.getSaveFileName(self, '', './','csv(*.csv)')

    #     if filename[0]:
    #         row_list = list()
    #         head_list = list()
    #         index_list = list()

    #         for col_index in range(widget.columnCount()):
    #             head_list.append(widget.horizontalHeaderItem(col_index).text())

    #         for row_index in range(widget.rowCount()):
    #             index_list.append(widget.verticalHeaderItem(row_index).text())

    #         for row_index in range(widget.rowCount()):
    #             col_list = list()
    #             for col_index in range(widget.columnCount()):
    #                 item = widget.item(row_index, col_index)
    #                 content = item.text()
    #                 col_list.append(content)
    #             row_list.append(col_list)
    #         save_df = pd.DataFrame(row_list, columns = head_list, index = index_list)
    #         save_df.index.name = "Date"
    #         save_df.to_csv(filename[0])


if __name__ == "__main__" :
    app = QApplication(sys.argv) 

    myWindow = WindowClass() 

    myWindow.show()

    app.exec()