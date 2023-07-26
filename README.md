# WhatsApp Chat Filter

WhatsApp Chat Filter is a Python script that allows you to extract messages from a WhatsApp chat between two specified dates and save them into a new file. It is a handy tool for filtering out specific conversations or analyzing chat data within a particular timeframe.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)

## Introduction

Have you ever wanted to focus on specific conversations within a lengthy WhatsApp chat? WhatsApp Chat Filter simplifies this task by taking the `.txt` file exported from whastapp and providing you with a new file containing messages that fall between the two dates you specify.

## Features

- Filter WhatsApp chat messages between two specified dates.
- Saves the filtered messages into a new file for easy access.

## Requirements
- Python 3.x (any python3 version should work smoothly)

## Installation

1. Clone the repository to your local machine:

```bash
$ git clone https://github.com/Joao-G11/whatsapp-chat-filter.git
```

2. Navigate to the project directory:

```bash
$ cd whatsapp-chat-filter
```

3. Ensure you have Python 3.x installed on your system. You can check this by running:

```bash
$ python3 --version
```

If Python is not installed, you can download it from the official website: https://www.python.org/downloads/

## Usage

1. Export your WhatsApp chat from the WhatsApp app. Open the chat, click on the three-dot menu, select "More," and choose "Export chat." Choose "Without Media" to get a `.txt` file.

2. Place the exported chat file into the project directory.

3. Run the script with the following command:

```bash
$ python3 chat_filter.py path_to_chat_file first_date second_date
```

The dates have the following format: yy.MM.dd.hh.mm.ss

- yy: year (e.g.,23 for year 2023)
- MM: month
- dd: day
- hh: hour
- mm: minute
- ss: second

4. The filtered chat will be saved to a new file named `filtered_chat.txt` in the same directory.

## Example

Suppose you have exported your WhatsApp chat to a file named `chat.txt`, and you want to filter messages between July 1, 2023, and July 15, 2023. After running the script, the filtered messages will be available in `filtered_chat.txt`.

This would be the command to run the example:
```bash
$ python3 chat_filter.py chat.txt 23.07.01.00.00.00 23.07.15.00.00.00
```

## Contributing

Contributions to this project are welcome and encouraged! If you find any issues, have suggestions, or want to add new features, feel free to open an issue or submit a pull request.




