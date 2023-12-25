file_path = 'index.html'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
    exit()
file.close()

title_start = html_content.find("<p>") + len("<p>")
title_end = html_content.find("</p>")
title = html_content[title_start:title_end].strip()

headers = ['<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>']
for header_tag in headers:
    header_start = html_content.find(header_tag) + len(header_tag)
    header_end = html_content.find('</' + header_tag[1:])
    header_text = html_content[header_start:header_end].strip()
    print(header_text)
    print(title)
