filename = input("Input the Filename: ")

ext= filename.split(".")
if len(ext) > 1:
    extension = ext[-1]
    print(f"The extension of the file is: '{extension}'")
else:
    print("Invalid filename.")
