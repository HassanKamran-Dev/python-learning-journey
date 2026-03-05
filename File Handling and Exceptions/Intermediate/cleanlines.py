def clean_file_safely(filepath):
    try:
        # Using "r+" for combined read/write power
        with open(filepath, "r+", encoding="utf-8") as file:
            # 1. Load data
            lines = file.readlines()
            
            # 2. Filter (Your list comprehension)
            clean = [line for line in lines if line.strip()]
            
            # 3. Rewind and Overwrite
            file.seek(0)
            file.writelines(clean)
            
            # 4. Chop off the old leftover data
            file.truncate()
            
        print(f"Done! '{filepath}' is now clean.")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' doesn't exist.")
    except PermissionError:
        print(f"Error: You don't have permission to edit '{filepath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
clean_file_safely("emptyspaces.txt")