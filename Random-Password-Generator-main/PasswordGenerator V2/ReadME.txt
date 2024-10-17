# Password-Generator V2
This is a random password generator build using Python.

What's the difference in PasswordGenerator and PasswordGenerator V2 ?
The difference is that PasswordGenerator only generates the password and able to copy to 
clipboard. Once think if the password is not remembered by the user so in order to save the 
generated password in encrypted file using AES Encryption by generating the key, I have implemented
encrypting and decrypting using cryptography python module. It is secure and without the key no one 
can decrypt the encrypted password

Modules Used:
  PyQt5 -> For GUI
  Random -> For randomizing characters
  String -> For generating letters, numbers and punctuation
  pyperclip -> For copying to clipboard
  cryptography -> For generating jey, loading key, encrypting and decrypting file.
  
 
 Note:</b> You need to install PyQt5, pyperclip, cryptography before running the script else the program won't work.
 To install these modules type this two commands in your terminal:
 -> pip install pyqt5
 -> pip install pyperclip
 -> pip install cryptography
