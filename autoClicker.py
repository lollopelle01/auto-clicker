import threading
import time
import pyautogui

class AutoClicker:
    def __init__(self, click_interval=0.1):
        self.click_interval = click_interval
        self.running = False
        self.thread = None

    def start_clicking(self):
        """Avvia il ciclo di auto-click."""
        self.running = True
        self.thread = threading.Thread(target=self._click_loop)
        self.thread.start()

    def stop_clicking(self):
        """Ferma il ciclo di auto-click."""
        self.running = False
        if self.thread:
            self.thread.join()
            self.thread = None

    def _click_loop(self):
        """Esegue i clic del mouse a intervalli regolari."""
        while self.running:
            pyautogui.click()
            time.sleep(self.click_interval)