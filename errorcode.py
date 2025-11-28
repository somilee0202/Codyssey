import builtins

error = dir(builtins)
try:
    for e in error:
        if "Error" in e:
            print(e)
except FileNotFoundError:
    print("The specified file was not found.")
except UnicodeDecodeError:
    print("There was an error decoding the file. Please check the file encoding.")
except ValueError:
    print("There was a value error while processing the file. Please check the data format.")
except Exception:
    print(f"An error occurred")