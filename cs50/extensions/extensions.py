file_name = str(input("File name?: "))
file_name = file_name.strip().casefold()
splitted = file_name.split(".")

if splitted[-1] == "gif":
    print("image/gif")
elif splitted[-1] == "jpg" or splitted[-1] == "jpeg":
    print("image/jpeg")
elif splitted[-1] == "png":
    print("image/png")
elif splitted[-1] == "pdf":
    print("application/pdf")
elif splitted[-1] == "txt":
    print("text/plain")
elif splitted[-1] == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
