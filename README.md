# EAN-13 Barcode Generator

This Python script generates an EAN-13 barcode based on user input and displays the barcode with the number correctly aligned below it.

## Description

The EAN-13 Barcode Generator is a simple Python script that allows users to input a 13-digit EAN-13 barcode number and generates a corresponding barcode image. The barcode is displayed with the input number correctly aligned below it, mimicking the format commonly seen on product packaging.

## Features

- Converts a 13-digit EAN-13 number into a barcode pattern.
- Displays the barcode using `matplotlib`.
- Aligns the input number below the barcode for easy readability.
- Saves the generated barcode as an image file (`barcode_with_entered_number.png`).

## Usage

1. Run the script.
2. Enter a valid 13-digit EAN-13 number when prompted.
3. The script will generate and display the barcode, and save it as `barcode_with_entered_number.png`.

### Example

```sh
$ python EAN13_Barcode_Generator.py
Enter the EAN-13 number: 5901234123457
