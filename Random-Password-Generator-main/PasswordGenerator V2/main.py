from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import string
import random
import pyperclip

ui, _ = loadUiType( "userInterface.ui" )  # Load the UI file


class MainApp( QMainWindow, ui ):  # Class to create the main window
    def __init__(self, parent=None):
        super( MainApp, self ).__init__( parent )
        self.setupUi( self )
        self.setWindowTitle( "Random Password Generator" )
        self.apply_theme()
        self.handle_buttons()
        self.generated_password = ""

    def apply_theme(self):  # Apply custom UI styling
        with open( "darkTheme.css", "r" ) as style:
            self.setStyleSheet( style.read() )

    def handle_buttons(self):  # Set up button interactions
        self.pushButton.clicked.connect( self.generate_password )
        self.pushButton_2.clicked.connect( self.copy_to_clipboard )

    def generate_password(self):
        # Define character set for password
        chars = string.ascii_letters + string.digits + string.punctuation
        password_length = self.spinBox.value()  # Get length from spin box

        # Generate a random password
        self.generated_password = ''.join( random.choice( chars ) for _ in range( password_length ) )

        # Display the generated password
        self.textBrowser.setText( self.generated_password )

    def copy_to_clipboard(self):
        pyperclip.copy( self.generated_password )
        self.label_3.setText( "Copied!" )  # Feedback to the user


def main():
    app = QApplication( sys.argv )
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
