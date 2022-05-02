# get started with GUI tools by PYQt5
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QLineEdit,QFileDialog,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from PyQt5.QtCore import pyqtSlot
import wget
import shutil
# defin my window Gui class : 

class My_downloader(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Pyqt5 File Downloder 1.0 ")
        #self.setWindowIcon(QIcon("Images/logo.ico"))
        self.background_color ="#ffffff"
        self.text_color = "#004268"
        self.resize(800,550)
        #set window resaizbale attr to false :
        self.setFixedSize(480,600)
        self.move(200,60)
        # title && Canvas :
        self.label_titel_image1 = QLabel(self)
        self.label_titel_image1.setPixmap(QPixmap("Images/icons8-import-64.png"))
        self.label_titel_image2 = QLabel(self)
        self.label_titel_image2.setPixmap(QPixmap("Images/icons8-import-64.png"))
        self.label_titel_message = QLabel(self)
        self.label_titel_message.setText(" Form web to your loacl machine Now ....")
        # label & entry for url file/folder  :
        self.label_entry_url = QLabel(self)
        self.label_entry_url.setPixmap(QPixmap("Images/icons8-open-in-browser-21.png"))
        self.label_entry_url_txt = QLabel(self)
        self.label_entry_url_txt.setText("URL :      ")
        # entry :
        self.input_entry_url = QLineEdit(self)
        # label & entry for name of output : 
        self.label_entry_name = QLabel(self)
        self.label_entry_name.setPixmap(QPixmap("Images/icons8-output-21.png"))
        self.label_entry_name_text = QLabel(self)
        self.label_entry_name_text.setText("Output Name :   ")
        #entry :
        self.input_entry_name = QLineEdit(self)
        # label & entry for output path : 
        self.label_entry_path = QLabel(self)
        self.label_entry_path.setPixmap(QPixmap("Images/icons8-file-path-21.png"))
        self.label_entry_path_text = QLabel(self)
        self.label_entry_path_text.setText("Output Path:  ")
        #path && button for select folder :
        self.input_entry_path = QLineEdit(self)
        self.input_entry_path.setReadOnly(True)
        self.btn_select_path = QPushButton(self)
         # btn start protocol : 
        self.btn_start = QPushButton(self)
        self.btn_select_path.setText("Select Path !")
        self.btn_start.setText("Download :) ..... ")
        # set default stat of btn is disabled :
        #self.btn_start.setEnabled(False)
        self.btn_start.clicked.connect(self.start)
        #bind-it with event : 
        self.btn_select_path.clicked.connect(self.select_folder)
        # deplace element :
        self.btn_select_path.move(320,390)
        self.btn_start.move(50,500)
        # add css style :
        self.setStyleSheet("""
        background-color:"#ffffff";
        padding:5px;
        """)
        self.label_titel_image2.setStyleSheet("""
        font-size : 18px;
        margin-left:310px;
        margin-top:25px;
        """)
        self.label_titel_image1.setStyleSheet("""
        font-size : 18px;
        margin-left:50px;
        margin-top:25px;
        """)
        self.label_titel_message.setStyleSheet("""
        background-color:"#ffffff";
        color:"#004268";
        font-size : 18px;
        margin-left:50px;
        margin-top:100px;
        """)
        self.label_entry_url.setStyleSheet("""
        font-size : 8px;
        margin-left:50px;
        margin-top:140px;
        """)
        self.label_entry_name.setStyleSheet("""
        font-size : 8px;
        margin-left:50px;
        margin-top:230px;
        """)
        self.label_entry_path.setStyleSheet("""
        font-size : 8px;
        margin-left:50px;
        margin-top:320px;
        """)
        self.label_entry_url_txt.setStyleSheet("""
        font-size : 18px;
        margin-left:70px;
        margin-top:140px;
        color:"#004268";
        """)
        self.label_entry_name_text.setStyleSheet("""
        font-size : 18px;
        margin-left:70px;
        margin-top:230px;
        color:"#004268";
        """)
        self.label_entry_path_text.setStyleSheet("""
        font-size : 18px;
        margin-left:70px;
        margin-top:320px;
        color:"#004268";
        """)

        self.input_entry_url.setStyleSheet("""
        margin-left:50px;
        margin-top:170px;
        width:350px;
        height:20px;
        border:1px solid #004268;
        border-radius: 5px;
        color:"#004268";
        """)
        self.input_entry_name.setStyleSheet("""
        margin-left:50px;
        margin-top:260px;
        width:350px;
        height:20px;
        border:1px solid #004268;
        border-radius: 5px;
        color:"#004268";
        """)
        self.input_entry_path.setStyleSheet("""
        margin-left:50px;
        margin-top:350px;
        width:350px;
        height:20px;
        border:1px solid #004268;
        border-radius: 5px;
        color:"#004268";
        """)
        self.btn_select_path.setStyleSheet("""
        width:80px;
        height:17px;
        background-color:"#004268";
        border:1px solid #27CEFD;
        border-radius: 5px;
        color:"#ffffff";
        """)
        self.btn_start.setStyleSheet("""
        width:320px;
        height:17px;
        background-color:"#004268";
        border:1px solid #27CEFD;
        border-radius: 5px;
        color:"#ffffff";
        """)
    
    def select_folder(self):
        path = os.path.expanduser("~")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        if dlg.exec_():
            self.path = dlg.selectedFiles()[0]
            self.input_entry_path.setText(self.path)
            self.test()
        return
    def start(self):
        if self.test() == True:

            try:
                response_name = wget.download(self.input_entry_url.text())
                print(response_name)
                #teste if is normal file : .extension:
                try:
                    extension = response_name.split('.')[1]
                    self.local_path = self.input_entry_path.text()+"/"+self.input_entry_name.text()+"."+response_name.split('.')[1]
                    #move element :
                    shutil.move(src=os.getcwd()+"/"+response_name, dst=self.local_path)
                except  Exception as e:
                    self.local_path = self.input_entry_path.text()+"/"+self.input_entry_name.text()+".zip"
                    #move element :
                    shutil.move(src=os.getcwd()+"/"+response_name, dst=self.local_path)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Donwload Completed ! ") 
                msg.setInformativeText("Open Folder in explorer ?")
                msg.setWindowTitle("Downloading Info !")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                #msg.buttonClicked.connect(se)
                msg.exec_()
            except Exception as e:
                QMessageBox.warning(self, "Warning", 
                            str(e))
            finally:
                self.input_entry_path.setText("")
                self.input_entry_name.setText("")
                self.input_entry_url.setText("")     
        else:
            QMessageBox.warning(self, "Warning", 
                            "you have to fill in all the fields!")
        return
    def test(self):
        count = 0
        if self.input_entry_path.text()!= "":
            count += 1
        if self.input_entry_url.text()!= "":
            count += 1
        if self.input_entry_name.text()!= "":
            count += 1
        if count == 3:
            self.btn_start.setEnabled(True)
            return True
        return False
if __name__ == "__main__":
    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)
    my_instance = My_downloader()
    my_instance.show()
    app.exec_()





