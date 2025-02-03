import files_utils

# Тестовые данные
json_data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
csv_data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
txt_data = ["Hello, World!", "This is a test."]
yaml_data = {"name": "Alice", "age": 30}

# Тестирование функций для работы с JSON
files_utils.write_json(*json_data, file_path='test.json')
print(files_utils.read_json('test.json'))
files_utils.append_json({"name": "Charlie", "age": 35}, file_path='test.json')
print(files_utils.read_json('test.json'))

# Тестирование функций для работы с CSV
files_utils.write_csv(*csv_data, file_path='test.csv')
print(files_utils.read_csv('test.csv'))
files_utils.append_csv({"name": "Charlie", "age": 35}, file_path='test.csv')
print(files_utils.read_csv('test.csv'))

# Тестирование функций для работы с TXT
files_utils.write_txt(*txt_data, file_path='test.txt')
print(files_utils.read_txt('test.txt'))
files_utils.append_txt("Appending text.", file_path='test.txt')
print(files_utils.read_txt('test.txt'))

# Тестирование функции для работы с YAML
with open('test.yaml', 'w') as file:
    yaml.dump(yaml_data, file)
print(files_utils.read_yaml('test.yaml'))
