# Cambodia Holidays ICS Generator

## Subscribe to Holidays

You can subscribe to the Cambodia public holidays directly using the following links:

- [Chinese Version (中文订阅)](https://raw.githubusercontent.com/ceeyang/cambodia-holiday-calender/main/cambodia_holidays_zh.ics)
- [English Version](https://raw.githubusercontent.com/ceeyang/cambodia-holiday-calender/main/cambodia_holidays_en.ics)
- [Khmer Version](https://raw.githubusercontent.com/ceeyang/cambodia-holiday-calender/main/cambodia_holidays_km.ics)

Click on the link corresponding to the language you prefer, and add it to your calendar application for easy access to Cambodia public holidays.

## Overview

This project generates `.ics` calendar files for Cambodia's public holidays for the years 2024 and 2025 in three languages: Chinese, English, and Khmer. These `.ics` files can be used to subscribe to the holiday events in various calendar applications, such as iOS, Google Calendar, and Microsoft Outlook.

The holiday data is stored in JSON files (`cambodia_holidays_zh.json`, `cambodia_holidays_en.json`, `cambodia_holidays_km.json`), making it easy to add or modify holiday information in any of the three supported languages.

## Features

- Generates `.ics` calendar files for Cambodia public holidays in three languages: Chinese, English, and Khmer.
- Easy to extend holiday data by editing the JSON files.
- Simple and convenient tool for creating multi-language calendar subscriptions for Cambodia holidays.

## Project Structure

- `cambodia_holidays_zh.json`: Contains holiday information in Chinese.
- `cambodia_holidays_en.json`: Contains holiday information in English.
- `cambodia_holidays_km.json`: Contains holiday information in Khmer.
- `generate_ics.py`: Python script that reads the JSON files and generates `.ics` files for each language.

## Installation

To run this project, you need Python 3.x installed. Additionally, the `ics` library is required. You can install it via pip:

```sh
pip install ics
```

## Usage

1. Clone the repository to your local machine.

```sh
git clone <repository-url>
cd cambodia-holidays-ics-generator
```

2. Run the Python script to generate `.ics` files for the holidays.

```sh
python generate_ics.py
```

3. After running the script, you will find three `.ics` files for Chinese, English, and Khmer:
   - `cambodia_holidays_zh.ics`
   - `cambodia_holidays_en.ics`
   - `cambodia_holidays_km.ics`

4. Use the `.ics` files to import or subscribe to the calendar in your preferred calendar application.

## JSON File Format

The holiday information is stored in JSON files. Each holiday entry is represented as follows:

```json
{
  "name": "Holiday Name",
  "date": "YYYY-MM-DD"
}
```

Each JSON file contains an array of such holiday entries, allowing you to easily add, remove, or modify holidays.

## Contributing

If you would like to contribute, feel free to open an issue or submit a pull request. Contributions to improve the code, fix bugs, or add new features are always welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- The `ics` library for generating `.ics` files.
- Contributors and supporters of the project.

## Contact

If you have any questions or feedback, please feel free to reach out via GitHub or email.
