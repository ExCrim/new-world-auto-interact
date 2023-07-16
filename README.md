# New World Auto Interaction

This repository contains a Python script for automating actions in a game window. The script utilizes the `pyautogui` library to simulate key presses and mouse clicks, `mss` library for taking screenshots, and `logging` library for logging information.

## Requirements

To run the script, you need to have the following dependencies installed:

- Python 3.x
- `pyautogui` library
- `mss` library
- `numpy` library
- `Pillow` library
- `keyboard` library

You can install the dependencies using the following command:
`pip install -r requirements.txt`  

## Usage

1. Clone the repository or download the script file.

2. Install the required dependencies by running the command mentioned in the Requirements section.

3. Modify the script to set the appropriate values for the `window_name` and other variables according to your game window and requirements.

4. Run the script using the following command:
`python auto_interact.py`

5. The script will search for the game window with the specified name, activate it, and perform automated actions based on game conditions.

6. During the automation, you can press the F1 key to toggle the pause state of the script. The pause state will be logged to the console and a log file named `game.log` will be created to store the logs.

7. Customize the script as needed to fit your specific game and automation requirements. You can modify the key mappings, screenshot regions, action sequences, and more.

## Important Notes

- Make sure to have the game window visible and in focus before running the script.

- The script uses screenshots and image recognition to detect interactable objects. You may need to provide the appropriate images or modify the image recognition parameters to match your game.

- Be cautious while using automation scripts in games to avoid violating game rules or terms of service. Make sure to use the script responsibly and within the allowed limits.

## License

This project is licensed under the [MIT License].
