from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import base64
import random
import string


def generate_random_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join( random.choice( chars ) for _ in range( length ) )
    return random_password


def decrypt():
    password = code.get()
    if password == generated_password:
        screen2 = Toplevel( screen )
        screen2.title( "Decryption" )
        screen2.geometry( "400x250" )
        screen2.configure( bg="#2C3E50" )

        message = Text1.get( 1.0, END )
        decode_message = message.encode( "ascii" )
        base64_bytes = base64.b64decode( decode_message )
        decrypted_message = base64_bytes.decode( "ascii" )

        Label( screen2, text="DECRYPTED", font=("arial", 14), fg="white", bg="#2C3E50" ).pack( pady=10 )
        Text2 = Text( screen2, font=("Roboto", 10), bg="#34495E", fg="white", relief=GROOVE, wrap=WORD, bd=0 )
        Text2.pack( fill=BOTH, expand=True, padx=10, pady=10 )
        Text2.insert( END, decrypted_message )
    elif not password:
        messagebox.showerror( "Decryption", "Input password" )
    else:
        messagebox.showerror( "Decryption", "Invalid password" )


def encrypt():
    password = code.get()
    if password == generated_password:
        screen1 = Toplevel( screen )
        screen1.title( "Encryption" )
        screen1.geometry( "450x250" )
        screen1.configure( bg="#2C3E50" )

        message = Text1.get( 1.0, END )
        encode_message = message.encode( "ascii" )
        base64_bytes = base64.b64encode( encode_message )
        encrypted_message = base64_bytes.decode( "ascii" )

        Label( screen1, text="ENCRYPTED", font=("arial", 14), fg="white", bg="#2C3E50" ).pack( pady=10 )
        Text2 = Text( screen1, font=("Roboto", 10), bg="#34495E", fg="white", relief=GROOVE, wrap=WORD, bd=0 )
        Text2.pack( fill=BOTH, expand=True, padx=10, pady=10 )
        Text2.insert( END, encrypted_message )
    elif not password:
        messagebox.showerror( "Encryption", "Input password" )
    else:
        messagebox.showerror( "Encryption", "Invalid password" )


def main_screen():
    global screen
    global code
    global Text1
    global generated_password

    screen = Tk()
    screen.geometry( "400x400" )
    screen.title( "Secret Tool" )
    screen.configure( bg="#1A242F" )

    generated_password = generate_random_password()
    code = StringVar()

    Label( screen, text="Enter text for encryption and decryption", fg="white", bg="#1A242F",
           font=("calibri", 13) ).pack( pady=10 )
    Text1 = Text( screen, font=("Roboto", 12), bg="white", fg="black", relief=GROOVE, wrap=WORD, bd=0 )
    Text1.pack( padx=20, pady=10, fill=BOTH, expand=True )

    Label( screen, text="Randomly Generated Password:", fg="white", bg="#1A242F", font=("calibri", 13) ).pack()
    Label( screen, text=generated_password, fg="lightblue", bg="#1A242F", font=("calibri", 13) ).pack( pady=5 )

    Entry( screen, textvariable=code, width=19, bd=0, font=("arial", 15), show="*" ).pack( pady=10 )

    button_frame = Frame( screen, bg="#1A242F" )
    button_frame.pack( pady=20, fill=BOTH, expand=True )
    ttk.Style().configure( "TButton", font=("calibri", 11), foreground="white", background="#3E606F" )

    Button( button_frame, text="ENCRYPT", height=2, width=15, bg="#3E606F", fg="white", bd=0, command=encrypt ).grid(
        row=0, column=0, padx=10, pady=10 )
    Button( button_frame, text="DECRYPT", height=2, width=15, bg="#3E606F", fg="white", bd=0, command=decrypt ).grid(
        row=0, column=1, padx=10, pady=10 )
    Button( screen, text="RESET", height=2, width=45, bg="#3E606F", fg="white", bd=0,
            command=lambda: [code.set( "" ), Text1.delete( 1.0, END )] ).pack( pady=10, fill=BOTH, expand=True )

    screen.mainloop()


main_screen()
