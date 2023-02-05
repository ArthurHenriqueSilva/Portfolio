'''
Purpose: Create a application that allows the user to create or decode QR Codes based on his input.

Input: Message to be encoded or the QR code to be decoded.

Output: Message encoded to QR CODE or Full information of decoded QR Code.
'''

import qrcode
import cv2
from pyzbar.pyzbar import decode
from PIL import Image


# Key_exit is a tool to keep the procces looping until the user ask to stop.
key_exit = True
while key_exit:
    # Loop that will take the option from the user. The user is only allowed to put ineger input
    while True:
        try:
            option = int(input("1: Encode QR | 2: Decode QR\n"))
        except ValueError as e:
            print("Invalid input!")
        else:
            break
    
    #Option that take the data from user, encode to QR, save the QR in png and open an window with the img.
    if option == 1:  
        data = input("Put the message that you want to encode in QR: ")
        img = qrcode.make(data)
        img.save("Your_QR/My_QR_CODE.png")
        img = cv2.imread('Your_QR/My_QR_CODE.png')
        cv2.imshow("This is your QR CODE!", img)
        cv2.waitKey(0)

    # Option that take the adress of the QR CODE saved in particular folder and decode this with all the stats from that img.
    elif option == 2:
        adressIMG = "Your_QR\My_QR_CODE.png"
        img = Image.open(adressIMG)
        decoded = decode(img)
        print(decoded[0])

    # Default
    else:
        print("Invalid request!")

    # last part of the loop control, ensuring only alphabeticals as input.
    while True:
        msg = input("Do you want to repeat the process ? (Yes/Y): ").upper()
        if msg.isalpha():
            break
            
    key_exit = True if msg == "Yes" or msg == "Y" else False