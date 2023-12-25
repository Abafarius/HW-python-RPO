file_path = "input.txt"  # Путь к вашему текстовому файлу с URL

try:
    with open(file_path, "r") as file:
        url = file.readline().strip()
except FileNotFoundError:
    print("File not found!")
    exit
# Разбиваем URL на части
protocol_end = url.find("://")
protocol = url[:protocol_end]

url_no_protocol = url[protocol_end + 3:]
domain_end = url_no_protocol.find("/")
domain = url_no_protocol[:domain_end]

path_start = domain_end
path_end = url_no_protocol.find("?")
if path_end == -1:
    path_end = len(url_no_protocol)

path = url_no_protocol[path_start:path_end]

query_params = url_no_protocol[path_end + 1:].split("&")
query_params_dict = {}
for param in query_params:
    key, value = param.split("=")
    query_params_dict[key] = value

# Выводим результат
print("Protocol:", protocol)
print("Domain name:", domain)
print("Requset:", path)
print("Parameters:")
for key, value in query_params_dict.items():
    print(f"   {key} = {value}")