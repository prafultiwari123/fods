def copy_file():
    try:
        # Take input file name
        input_file = input("Enter the name of the input file: ")
        
        # Try opening the input file for reading
        with open(input_file, 'r') as infile:
            content = infile.read()

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    try:
        # Take output file name
        output_file = input("Enter the name of the output file: ")

        # Check if output file already exists
        with open(output_file, 'x') as outfile:  # 'x' mode creates file only if it doesn't exist
            outfile.write(content)
            print(f"File copied successfully to '{output_file}'.")
    except FileExistsError:
        print(f"Error: The file '{output_file}' already exists. Choose a different name.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    copy_file()
