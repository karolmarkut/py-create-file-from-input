def main():
    File_name = input("File name: ")
    with open(f"{File_name}.txt", "a") as f:
        while True:
            tekst = input("Wpisz coś (wpisz 'stop', aby zakończyć): ")
            if tekst == "stop":
                break
            f.write(tekst + "\n")
        print(f"{File_name} \n, {tekst} \n")
    pass


if __name__ == "__main__":
    main()
