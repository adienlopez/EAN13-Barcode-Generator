import matplotlib.pyplot as plt
import numpy as np

# Function to create barcode pattern
def ean13_pattern(number):
    codes = {
        'L': ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011'],
        'G': ['0100111', '0110011', '0011011', '0100001', '0011101', '0111001', '0000101', '0010001', '0001001', '0010111'],
        'R': ['1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100', '1001000', '1110100']
    }
    structure = [
        'LLLLLL',
        'LLGLGG',
        'LLGGLG',
        'LLGGGL',
        'LGLLGG',
        'LGGLLG',
        'LGGGLL',
        'LGLGLG',
        'LGLGGL',
        'LGGLGL'
    ]

    # Start sequence
    result = '101'  
    left_structure = structure[int(number[0])]

    # Encode the left part of the barcode
    for i, digit in enumerate(number[1:7]):
        result += codes[left_structure[i]][int(digit)]

    # Center sequence
    result += '01010'  

    # Encode the right part of the barcode
    for digit in number[7:]:
        result += codes['R'][int(digit)]

    # End sequence
    result += '101'  
    return result

# Ask for the barcode number
barcode_number = input("Enter the EAN-13 number: ")

# Check if the number is valid
if len(barcode_number) != 13 or not barcode_number.isdigit():
    print("Invalid EAN-13 number. Please enter a 13-digit number.")
else:
    # Convert pattern to barcode image
    pattern = ean13_pattern(barcode_number)
    barcode_image = np.array([int(x) for x in pattern])

    # Plotting the barcode
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.imshow(barcode_image.reshape(-1, 1).T, cmap='binary', aspect='auto')
    ax.axis('off')  # Turn off the axis

    # Calculate spacing for each digit
    num_spacing = 1 / len(barcode_number)

    # Add the barcode number below the barcode, formatted correctly
    for i, char in enumerate(barcode_number):
        x_position = i * num_spacing
        plt.text(x_position, -0.15, char, ha='center', va='top', transform=ax.transAxes, fontsize=12, family='monospace')

    # Save the barcode
    plt.savefig('barcode_with_entered_number.png', bbox_inches='tight', pad_inches=0.2)
    plt.show()
