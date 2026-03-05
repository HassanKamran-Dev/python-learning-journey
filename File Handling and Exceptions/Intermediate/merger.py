def merge_files(file1,file2,output_file):
    try:
        with open(output_file,'w') as outfile:

            with open(file1,'r') as f1:
                outfile.write(f1.read())
            
            outfile.write("\n")

            with open(file2,'r') as f2:
                outfile.write(f2.read())
            
        print(f"Successfully merged {file1} and {file2} into {output_file}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occured {e}")
    

if __name__ == "__main__":
    merge_files("notes1.txt","notes2.txt","merge_all.txt")