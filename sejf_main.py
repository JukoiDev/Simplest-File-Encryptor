# Copyright (C) 2022 Awli | Proszę, nie usuwaj tego komentarza

import os
from cryptography.fernet import Fernet

KEY_FILE_NAME = 'key.AWLIsafe'

def encrypt(filename, key) -> None: # Szyfring
    f = Fernet(key) # Tworzenie nowej instancji klasy Fernet
    with open(filename, "rb") as file:
        file_data = file.read() # Czytaj plik
    
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data) # Wpisz zaszyfrowane dane do pliku

def decrypt(filename, key) -> None: # Odszyfring
    f = Fernet(key) # Tworzenie nowej instancji klasy Fernet
    with open(filename, "rb") as file:
        encrypted_data = file.read() # Czytaj plik
    
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data) # Wpisz odszyfrowane dane do pliku
    

def printAscii() -> None:
    print('   _____         .__  .__  _________           __  _____ ')
    print('  /  _  \__  _  _|  | |__|/   _____/ ____     |__|/ ____\\')
    print(' /  /_\  \ \/ \/ /  | |  |\_____  \_/ __ \    |  \   __\ ')
    print('/    |    \     /|  |_|  |/        \  ___/    |  ||  |   ')
    print('\____|__  /\/\_/ |____/__/_______  /\___  >\__|  ||__|   ')
    print('        \/                       \/     \/\______|       ')

def main() -> None: # Punkt wejściowy skryptu
    printAscii()
    print('Witaj w programie AwliSejf. Wpisz ścieżkę do folderu z plikiem klucza:')

    key_file_path = str(input())

    if not key_file_path.endswith('\\') or not key_file_path.endswith('\\\\'): # Jeżeli ścieżka kończy się na \ lub \\
        key_file_path = key_file_path + '\\' # Dodaj do ścieżki slashe

    if os.path.exists(key_file_path + KEY_FILE_NAME):
        os.system('cls') # BRZYDKIE!!!

        print('Plik z kluczem istnieje. Co chcesz zrobić ze swoimi plikami?')
        print('1 - Zaszyfrować je, 2 - Odszyfrować je (DOMYŚLNIE 1)')
        choice = int(input() or '1')
        with open(key_file_path + KEY_FILE_NAME, 'rb') as f:
            if choice == 2:
                print('Podaj ścieżkę do pliku lub folderu, aby go(je) odszyfrować: ')
                path = str(input())
                if os.path.isdir(path):
                    raise TypeError('W wersji 1.0 tylko pliki są wspierane.')
                elif os.path.isfile(path): 
                    decrypt(path, f.read())
            else: 
                print('Podaj ścieżkę do pliku lub folderu, aby go(je) zaszyfrować: ')
                path = str(input())
                if os.path.isdir(path):
                    raise TypeError('W wersji 1.0 tylko pliki są wspierane.')
                elif os.path.isfile(path): 
                    encrypt(path, f.read())
            print('Wykonano daną operację!')

    else:
        print('Tworzenie klucza na wybranej przez Ciebie ścieżce...')
        with open(key_file_path + KEY_FILE_NAME, 'wb') as f: # "Otwórz" plik
            f.write(Fernet.generate_key() ) # Stwórz nowy klucz i zapisz go do pliku

if __name__ == '__main__':
    main()