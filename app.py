import keyboard
from autoClicker import AutoClicker, time

def main():
    # Chiede all'utente di specificare l'intervallo di clic
    try:
        click_interval = float(input("Inserisci l'intervallo di clic in secondi (es. 0.2): "))
    except ValueError:
        print("Input non valido. Verrà utilizzato l'intervallo predefinito di 0.2 secondi.")
        click_interval = 0.2

    clicker = AutoClicker(click_interval=click_interval)

    print("Premi 's' per avviare/fermare l'auto-clicker, 'q' per uscire.")
    while True:
        if keyboard.is_pressed('s'):  # Tasto per attivare/disattivare
            if clicker.running:
                clicker.stop_clicking()
                print("Auto-clicker fermato.")
            else:
                clicker.start_clicking()
                print(f"Auto-clicker avviato con un intervallo di {click_interval} secondi.")
            time.sleep(0.5)  # Evita input ripetuti

        if keyboard.is_pressed('q'):  # Tasto per uscire
            if clicker.running:
                clicker.stop_clicking()
            print("Uscita dal programma.")
            break

if __name__ == "__main__":
    main()
