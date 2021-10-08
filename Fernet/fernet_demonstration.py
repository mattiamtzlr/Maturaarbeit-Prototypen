# from os import system
# system("pip install cryptography")

import cryptography
from cryptography.fernet import Fernet
import base64

passwordEntered = False
while not passwordEntered:
    password = input("Passwort: ")  # get the user's password

    if len(password) < 32:
        while len(password) < 32:
            password += password[0]  # extend the password's length until it is 32 characters long

        # encode the extended password to url-safe base64 bytes
        key = base64.urlsafe_b64encode(bytes(password, "utf-8"))
        fernet = Fernet(key)  # give the key to Fernet

        passwordEntered = True

    elif len(password) > 32:
        print("Das Passwort kann höchstens 32 Zeichen lang sein.\n")  # prevent too long passwords


# saving message:
def save():
    message = input("\nNachricht: ")
    # add unique extension for consistency:
    dest = input("Name der Zieldatei (ohne Dateityp): ") + ".enc"

    with open(dest, "w") as f:
        f.write(str(fernet.encrypt(bytes(message, "utf-8")), "utf-8"))  # write message to file
        f.close()

    print(f"Die Nachricht wurde in der Datei '{dest}' gespeichert.\n")


# loading and decrypting message:
def load():
    src = input("\nName der Ursprungsdatei (ohne Dateityp): ") + ".enc"  # get filename and add extension

    try:
        with open(src) as f:
            messageEncrypted = f.read()
            output = fernet.decrypt(bytes(messageEncrypted, "utf-8"))  # decrypt message
            f.close()

        print(f"\nEntschlüsselte Nachricht: \n{str(output, 'utf-8')}\n")
        print(f"Nachricht wurde aus der Datei '{src}' gelesen.")

    except FileNotFoundError:
        print(f"Fehler: Datei '{src}' konnte nicht gefunden werden.")  # prevent errors by FileNotFoundError

    except cryptography.fernet.InvalidToken:
        print(f"Fehler: Dieses Passwort ist nicht korrekt um '{src}' zu entschlüsseln.")


# app:
actionChosen = False
while not actionChosen:
    action = input("Gewünschte Aktion? Nachricht [s]peichern / Nachricht [l]aden: ")  # "menu"
    if action.lower() in ["s", "speichern"]:
        actionChosen = True
        save()
    elif action.lower() in ["l", "laden"]:
        actionChosen = True
        load()
