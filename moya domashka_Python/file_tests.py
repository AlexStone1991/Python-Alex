from file_classes import JsonFile, TxtFile, CsvFile

def test_json_file():
    json_file = JsonFile('test.json')
    data = [{"name": "Алиса", "age": 30}, {"name": "Димон", "age": 25}]

    json_file.write(data)
    read_data = json_file.read()
    print("Read JSON:", read_data)

    json_file.append({"name": "Сергей", "age": 35})
    read_data = json_file.read()
    print("Appended JSON:", read_data)

def test_txt_file():
    txt_file = TxtFile('test.txt')
    data = "Здравствуй Мир! Прощай, Человек - Паук!\n"

    txt_file.write(data)
    read_data = txt_file.read()
    print("Read TXT:", read_data)

    txt_file.append("Appending text.\n")
    read_data = txt_file.read()
    print("Appended TXT:", read_data)

def test_csv_file():
    csv_file = CsvFile('test.csv')
    data = [["Name", "Age"], ["Алиса", 30], ["Димон", 25]]

    csv_file.write(data)
    read_data = csv_file.read()
    print("Read CSV:", read_data)

    csv_file.append([["Сергей", 35]])
    read_data = csv_file.read()
    print("Appended CSV:", read_data)

if __name__ == "__main__":
    test_json_file()
    test_txt_file()
    test_csv_file()
