import keyboard
from autoClicker import AutoClicker, time

def main():
    clicker = AutoClicker(click_interval=0.2)  # Modifica l'intervallo di clic qui

    print("Premi 's' per avviare/fermare l'auto-clicker, 'q' per uscire.")
    while True:
        if keyboard.is_pressed('s'):  # Tasto per attivare/disattivare
            if clicker.running:
                clicker.stop_clicking()
                print("Auto-clicker fermato.")
            else:
                clicker.start_clicking()
                print("Auto-clicker avviato.")
            time.sleep(0.5)  # Evita input ripetuti

        if keyboard.is_pressed('q'):  # Tasto per uscire
            if clicker.running:
                clicker.stop_clicking()
            print("Uscita dal programma.")
            break

if __name__ == "__main__":
    main()