def main():
    file_name = input("File name: ")

    with open(f"{file_name}.txt", "w") as f:
        while True:
            tekst = input("Enter new line of content: ")
            if tekst == "stop":
                break
            f.write(tekst + "\n")


if __name__ == "__main__":
    main()
