import pyautogui
import time
import random
import mss
import numpy as np
from PIL import Image
import gc
import logging
import keyboard

class GameStuff:
    """
    A class that encapsulates game-related functionality and automation.

    Args:
        window_name (str): The name of the game window.

    Attributes:
        window_name (str): The name of the game window.
        direction_keys (list): The list of keys used for directional input.
        window_list (list): A list of windows with the given window name.
        target_window: The target window to interact with.
        sleep_time (float): The sleep time between actions.
        logger (logging.Logger): The logger instance for logging information.
        last_key_press_time (float): The timestamp of the last key press.
        key_press_interval (float): The interval between random key presses.
        key_press_probability (float): The probability of performing a random key press.
        paused (bool): Flag indicating if the automation is paused.

    Methods:
        toggle_pause(event): Toggles the pause state of the automation.
        find_window(): Finds the game window with the specified window name.
        activate_window(): Activates the target game window and performs initialization steps.
        setup_screenshot(): Sets up the screenshot region and performs automated actions based on game conditions.
        random_key_press(): Performs a random key press to bypass anti-AFK mechanisms.
    """

    def __init__(self, window_name):
        self.window_name = window_name
        self.direction_keys = ["a", "d"]
        self.window_list = pyautogui.getWindowsWithTitle(self.window_name)
        self.target_window = []
        self.sleep_time = random.uniform(0.1, 0.2)

        self.logger = logging.getLogger("GameStuff")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

        # Create a file handler to save logs to a file
        file_handler = logging.FileHandler("game.log")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Create a stream handler to print logs to the console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        self.last_key_press_time = time.time()
        self.key_press_interval = 10.0
        self.key_press_probability = 0.5

        self.paused = False

        # Register F1 key press event listener to toggle pause state
        keyboard.on_press_key("F1", self.toggle_pause)

    def toggle_pause(self, event):
        """
        Toggles the pause state of the automation when the F1 key is pressed.

        Args:
            event (keyboard.KeyboardEvent): The keyboard event object.
        """
        self.paused = not self.paused
        self.logger.info("Script paused" if self.paused else "Script resumed")

    def find_window(self):
        """Finds the game window with the specified window name."""
        if self.window_list:
            self.target_window = self.window_list[0]
            self.logger.info(f"Window Name: {self.target_window.title} | Game Resolution: {self.target_window.width}x{self.target_window.height}")
        else:
            self.logger.error("Window not found!")

    def activate_window(self):
        """Activates the target game window and performs initialization steps."""
        if self.target_window:
            self.target_window.activate()
            screen_center_w = self.target_window.left + (self.target_window.width/2)
            screen_center_h = self.target_window.top + (self.target_window.height/2)
            pyautogui.moveTo(screen_center_w, screen_center_h)
            time.sleep(self.sleep_time)
            pyautogui.click()
            time.sleep(self.sleep_time)

    def setup_screenshot(self):
        """
        Sets up the screenshot region and performs automated actions based on game conditions.

        Important:
            This method contains the main automation loop.
        """
        screenshot_region = {"mon": 1, "top": self.target_window.top, "left": self.target_window.left + round(self.target_window.width/3), "width": round(self.target_window.width/3), "height": self.target_window.height}
        screenshot = mss.mss()
        while True:
            if not self.paused:
                screenshot_image = Image.fromarray(np.array(screenshot.grab(screenshot_region)))
                while pyautogui.locate("imgs/interact.png", screenshot_image, grayscale=True, confidence=.6) is None:
                    gc.collect()
                    screenshot_image = Image.fromarray(np.array(screenshot.grab(screenshot_region)))

                    # Check if it's time to perform a random key press
                    current_time = time.time()
                    if current_time - self.last_key_press_time >= self.key_press_interval:
                        self.last_key_press_time = current_time
                        if random.random() < self.key_press_probability:
                            self.random_key_press()

                self.logger.info("Interactable object found!")
                pyautogui.press('e')
                time.sleep(self.sleep_time)
            else:
                time.sleep(1)

    def random_key_press(self):
        """Performs a random key press to bypass anti-AFK mechanisms."""
        key = random.choice(self.direction_keys)
        pyautogui.keyDown(key)
        self.logger.info(f"Random key pressed: {key} to bypass anti-AFK")
        time.sleep(0.25)
        pyautogui.keyUp(key)


# Instantiate the GameStuff class and perform the automation steps
game_class = GameStuff("New World")

# Find the game window
game_class.find_window()

# Activate the game window and perform initialization
game_class.activate_window()

# Setup the screenshot region and start the automation loop
game_class.setup_screenshot()