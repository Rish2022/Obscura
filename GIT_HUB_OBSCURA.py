
import secrets
import hashlib
import os
import random
import psutil
from Git_hub_Vanar_Raksha_Guhya import Vanar_Guhya_Raksha
import sys
import PyQt6
from PyQt6.QtWidgets import QComboBox, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, \
    QApplication, QLabel, QMessageBox, QTextEdit, QFileDialog, QDialog
from PyQt6.QtCore import QSize,Qt,QUrl,QTimer,QTime,QEvent
from PyQt6.QtGui import QIcon,QMovie,QFont,QTextCursor, QTextListFormat
import webbrowser
from PyQt6.QtWebEngineWidgets import QWebEngineView
from datetime import datetime


class Genjutsu(QWidget):

    def __init__(self):
        super().__init__()

        Display_Screen_Size_Device = self.screen().availableGeometry()
        Display_Screen_Width = Display_Screen_Size_Device.width()
        Display_Screen_Height = Display_Screen_Size_Device.height()

        Genjutsu_Height = int(Display_Screen_Height * 0.25)
        Genjutsu_Width = int(Display_Screen_Width*0.25)


        self.resize(Genjutsu_Height,Genjutsu_Width)

        self.setWindowTitle("🦑 Obscura 🦑")

        #LET'S ADD THEM COLOURS


        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a; 
                color: #e0e0e0;
                font-family: 'Courier New', Courier, monospace;
            }
            QPushButton {
                background-color: #2b2b2b;
                border: 2px solid #555555;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                color: #00ffcc; /* A toxic/misty cyan color */
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #00ffcc;
                color: #1a1a1a;
                border: 2px solid #ffffff;
            }
            QLineEdit {
                background-color: #0d0d0d;
                border: 1px solid #00ffcc;
                border-radius: 5px;
                color: #ffffff;
                font-size: 14px;
                padding: 8px;
            }
        """)

        self.Genjutsu_Layout = QVBoxLayout()
        self.setLayout(self.Genjutsu_Layout)

# GENJUTSU TOOL BOX
        self.Scramble_Button = QPushButton("Let's Hide! 🕷️")


        self.DE_Scramble_Button = QPushButton("Let's Unhide!🦑 ")


        Button_Font = QFont()
        Button_Font.setPointSize(35)

        self.Scramble_Button.setFont(Button_Font)
        self.Scramble_Button.setStyleSheet("""
                    QPushButton {
                        border: 2px solid #ff00ff;
                        color: #ff00ff;
                    }
                    QPushButton:hover {
                        background-color: #ff00ff;
                        color: #1a1a1a;
                        border: 2px solid #ffffff;
                    }
                """)
        self.DE_Scramble_Button.setFont(Button_Font)
        self.DE_Scramble_Button.setStyleSheet("""
                    QPushButton {
                        border: 2px solid #00ffcc;
                        color: #00ffcc;
                    }
                    QPushButton:hover {
                        background-color: #00ffcc;
                        color: #1a1a1a;
                        border: 2px solid #ffffff;
                    }
                """)


        self.Genjutsu_Tools_Layout = QHBoxLayout()


        #Now the Text Edit
        self.Master_Password_KEY = QLineEdit()
        self.Master_Password_KEY.setPlaceholderText("Choose me very Carefully 🦉")
        # announcing the Horizontal layout

        self.Genjutsu_Tools_Layout.addWidget(self.Scramble_Button)
        self.Genjutsu_Tools_Layout.addWidget(self.DE_Scramble_Button)
        self.Genjutsu_Tools_Layout.addWidget(self.Master_Password_KEY)


# ADDING THE HORIZONTAL BLOCK TO THE VERTICAL ONE

        self.Genjutsu_Layout.addLayout(self.Genjutsu_Tools_Layout)

        # THE ACUTAL PLACE WEHERE WE CAN UPLOAD STUFF WHICH INCLUDES ANYTHING

#THE PASSWORD CLASS




#   ALL OF THEM WIRES
        self.Scramble_Button.clicked.connect(self.Gopaniya_Karnam)
        self.DE_Scramble_Button.clicked.connect(self.Rahasya_Vimochanam)


    def Gopaniya_Karnam(self):
        password = self.Master_Password_KEY.text()
        if not password:
            QMessageBox.warning(self,"Password Missing","oh the Secretive one , the lock must be made with a key!")
            return
        File_Path_To_Lock,Lock_File_Type= QFileDialog.getOpenFileName(self,"oh the Secretive one , i need a file too! ")
        if not File_Path_To_Lock:
            QMessageBox.warning(self,"NO FILE CHOSEN"," One can lock air but not emptiness , choose a file oh the secretive one!")
            return
        with open(File_Path_To_Lock,"rb") as file:
            raw_data = file.read()

        # CALLING THE ENGINE
        Vault = Vanar_Guhya_Raksha(Master_Password=password)
        Rakshit_Data = Vault.Guhya_Data(raw_data)

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Locked File As", "", "Vanar Vault (*.vanar)")
        if not save_path:
            return

        with open(save_path,"wb") as created_file:
            created_file.write(Rakshit_Data)

            QMessageBox.information(self,"Success!"," File Locked.🐺")

    def Rahasya_Vimochanam(self):
        password_break = self.Master_Password_KEY.text()

        if not password_break:
            QMessageBox.warning(self, "REALLY? that's not the password","are you sure you are the Secretive one!, this is definitely not the key!")
            return
        File_Path_To_Decrypt,Open_File_Type = QFileDialog.getOpenFileName(self, "Select Locked File", "", "Vanar Vault (*.vanar)")
        if not File_Path_To_Decrypt:
            return

        with open(File_Path_To_Decrypt,"rb") as file:
            Guhya_Data = file.read()



            QMessageBox.information(None, "DONE!", "Success! File Loaded. 🐻")

        Rahasya_Decryption = Vanar_Guhya_Raksha.Rahasya_Bhedan(Guhya_Data,password_break)

        if Rahasya_Decryption == b"TAMPER_DETECTED":
            QMessageBox.critical(self, "Security Alert 🐺", "You are not the intended user. 🐭")
            return
        elif Rahasya_Decryption == b"ERROR":
            QMessageBox.critical(self, "System Error", "Vault malfunction.")
            return


        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Unlocked File As",
            "",
            "All Files (*);;Images (*.jpg *.png);;Video (*.mp4 *.mkv);;Audio (*.mp3 *.wav);;Doc (*.pdf );;Doc (*.txt );;Doc (*.xlsx )")

        if not save_path:
            return

        with open(save_path, "wb") as unlocked_file:
            unlocked_file.write(Rahasya_Decryption)

        QMessageBox.information(self, "Success", "File unlocked! 🦚")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Genjutsu_MainWindow = Genjutsu()

    Genjutsu_MainWindow.show()
    sys.exit(app.exec())


