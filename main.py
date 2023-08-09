import sys 
import PyQt5.QtWidgets as pyqt5
import finplot as fplt
import pandas as pd

fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000"
fplt.candle_bear_color = "#0000FF"

class MyWindow(pyqt5.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 300, 800, 600)
        
        table_widget = pyqt5.QTableWidget()

        button_load = pyqt5.QPushButton("load")
        button_load.clicked.connect(lambda state, widget = table_widget: self.slot_button_load(state, widget))

        button_save = pyqt5.QPushButton("Save")
        button_save.clicked.connect(lambda state, widget = table_widget: self.slot_button_save(state, widget))

        widget= pyqt5.QGraphicsView()
        layout = pyqt5.QVBoxLayout(widget)
        self.setCentralWidget(widget)

        self.ax = fplt.create_plot(init_zoom_periods=50)
        self.axs = [self.ax] # finplot requres this property
        self.axo = self.ax.overlay()

        layout.addWidget(self.ax.vb.win)       
        layout.addWidget(table_widget)
        layout.addWidget(button_load)
        layout.addWidget(button_save)

    def finplot_display(self,filename):
        csv_df = pd.read_csv(filename,index_col='Date')
        csv_df.index = pd.to_datetime(csv_df.index)
        
        self.ax.reset() 
        self.axo.reset()

        fplt.candlestick_ochl(csv_df[['Open', 'Close', 'High', 'Low']])
        fplt.show(qt_exec=False)
    
    def df_calculate(self, df):
        calc_df = df
        calc_df['avg'] = (calc_df['Open'] + calc_df['Close'] + calc_df['High'] + calc_df['Low']) / 4
        return calc_df
    
    def create_table_widget(self, widget, df):
        widget.setRowCount(len(df.index))
        widget.setColumnCount(len(df.columns))
        widget.setHorizontalHeaderLabels(df.columns)
        widget.setVerticalHeaderLabels(df.index)

        for row_index, row in enumerate(df.index):
            for col_index, column in enumerate(df.columns):
                value = df.loc[row][column]
                
                item = pyqt5.QTableWidgetItem(str(value))
                
                widget.setItem(row_index, col_index, item)

    def slot_button_load(self, state, widget):
        filename = pyqt5.QFileDialog.getOpenFileName(self, '', './','csv(*.csv)')

        if filename[0]:
            df = pd.read_csv(filename[0], index_col = 0)
            self.finplot_display(filename[0])
            print(df)
            calc_df = self.df_calculate(df)
            self.create_table_widget(widget, calc_df)

    def slot_button_save(self, state, widget):
        filename = pyqt5.QFileDialog.getSaveFileName(self, '', './','csv(*.csv)')

        if filename[0]:
            row_list = list()
            head_list = list()
            index_list = list()

            for col_index in range(widget.columnCount()):
                head_list.append(widget.horizontalHeaderItem(col_index).text())

            for row_index in range(widget.rowCount()):
                index_list.append(widget.verticalHeaderItem(row_index).text())

            for row_index in range(widget.rowCount()):
                col_list = list()
                for col_index in range(widget.columnCount()):
                    item = widget.item(row_index, col_index)
                    content = item.text()
                    col_list.append(content)
                row_list.append(col_list)
            save_df = pd.DataFrame(row_list, columns = head_list, index = index_list)
            save_df.index.name = "Date"
            save_df.to_csv(filename[0])


if __name__ == "__main__":
    app = pyqt5.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()