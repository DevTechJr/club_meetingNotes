# Club Meeting Notes Script - `anirudhbv.js`

## Overview

The Club Meeting Notes script is a Python script that can be used to send meeting notes to a group of people via email- `without any copy-pasting bs`. 

The script takes a list of email addresses in a JSON file and a meeting note message in a text file, and sends an email to each email address with the meeting note message.

## Prerequisites

Before using the script, you will need to have:

- Python installed on your computer
- Access to an email account with a username and password
- The email address and password for the account you want to use to send the meeting notes

## Setup

1. Download the `main.py` file from the GitHub repository.
2. Open the `records.json` file and replace the example email addresses with the email addresses of the people you want to send the meeting notes to.
3. Open the `message.txt` file and replace the example meeting note message with the message you want to send.
4. Open the `main.py` file in a text editor.
5. Replace the `your-email@gmail.com` and `your-email-password` fields in the script with the email address and password for the account you want to use to send the meeting notes.
6. Save the changes to the `main.py` file.

## Usage

1. Open a terminal or command prompt window.
2. Navigate to the directory where you saved the `main.py` file.
3. Run the script by typing `python main.py` and pressing enter.
4. The script will send an email to each email address in the `records.json` file with the meeting note message.

## Troubleshooting

If you encounter any issues with the script, here are some common problems and solutions:

- Problem: The script does not run when you type `python main.py` in the terminal.
  - Solution: Make sure you are in the correct directory where the `main.py` file is located.
- Problem: The script does not send any emails.
  - Solution: Check that the email addresses in the `records.json` file are correct and that the email address and password for the account you are using to send the meeting notes are correct.
- Problem: The script sends the meeting notes to some, but not all, of the email addresses in the `emails.json` file.
  - Solution: Check that the email addresses in the `records.json` file are correct and that there are no typos or formatting errors. Also, check that the email addresses are separated by commas and have no spaces between them.

## Conclusion

The Club Meeting Notes script is an easy-to-use tool for sending meeting notes to a group of people via email. By following the setup and usage instructions in this README file, you can quickly and easily send meeting notes to your club or organization members- without any copy-pasting time waste bs.
