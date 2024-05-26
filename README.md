# WhatsApp Birthday Wisher

## Overview
This project automates the process of sending birthday wishes via WhatsApp using Selenium and Python. It interacts with WhatsApp Web to send customized birthday messages to contacts whose birthdays are on the current date. Additionally, it provides a convenient way to schedule the execution of the script using Windows Task Scheduler.

## Features
- Sends personalized birthday messages to contacts on WhatsApp.
- Utilizes Selenium for web automation.
- Easy customization of message templates using `messages.txt`.
- Includes a `taskscript.bat` file for scheduling execution with Windows Task Scheduler.
- Utilizes `main.py` for the main Python script.
- Includes `BDayBotDataset.csv` for storing date of birth information.

## Prerequisites
- Python 3.x installed on your system.
- Google Chrome browser installed.
- ChromeDriver executable in PATH or current directory. (Download from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads))
- WhatsApp Web logged in and authenticated on the Chrome browser.

## Installation
1. Clone or download the repository to your local machine.

## Usage
1. Update the message templates in `messages.txt` with your customized birthday wishes.
2. Update `BDayBotDataset.csv` with the date of birth information of your contacts.
3. Run the `main.py` script using the command `python main.py`.
4. Follow the on-screen prompts to authenticate and start the process.
5. Optionally, schedule the script to run automatically using Windows Task Scheduler by executing `taskscript.bat`.

## Configuration
- `messages.txt`: Contains message templates for birthday wishes. Customize these messages as per your preference.
- `taskscript.bat`: Batch script to execute the Python script. Edit this script to specify the path to your Python executable and the location of `main.py`.
- `BDayBotDataset.csv`: CSV file containing date of birth information of contacts. Format: Name,DOB (MM/DD/YYYY).

## Important Notes
- Ensure that you have an active internet connection throughout the execution of the script.
- This script uses automation and may be against WhatsApp's terms of service. Use it responsibly and at your own risk.
- Make sure to respect privacy and only send messages to contacts who are comfortable receiving them.

## Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for any bugs or feature requests.

## License
This project is licensed under the [Apache License 2.0](LICENSE).
