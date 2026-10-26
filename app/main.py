def main():
    file_name = input("Enter name of the file: ")

    file_name = file_name + ".txt"
    with open(f"{file_name}", "w") as f:
        while True:
            tekst = input("Enter new line of content: ")
            f.write(tekst + "\n")
            if tekst == "stop":
                break


if __name__ == "__main__":
    main()
