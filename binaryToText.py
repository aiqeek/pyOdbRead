def binary_to_text(input_file, output_file):
    try:
        with open(input_file, 'rb') as binary_file:
            # Read binary data
            binary_data = binary_file.read()

            # Convert binary data to hexadecimal representation
            hex_representation = binary_data.hex()

            # Write hexadecimal representation to text file
            with open(output_file, 'w') as text_file:
                text_file.write(hex_representation)

        print(f"Conversion successful. Output written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'input.bin' with the name of your binary file
    input_file_name = 'Job-1.odb'

    # Replace 'output.txt' with the desired name for the text file
    output_file_name = 'output.txt'

    binary_to_text(input_file_name, output_file_name)