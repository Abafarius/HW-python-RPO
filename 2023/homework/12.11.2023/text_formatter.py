filename = 'article.txt'
try:
    file = open(filename, encoding='utf-8')
except FileNotFoundError:
    print("File not Found")
    exit()

text = file.read()
file.close()

max_line_length = int(input("Введите максимальную длину строк в символах: "))

try:
    max_line_length = int(max_line_length)
except ValueError:
    print("Value error. Enter a natural integer number")
    exit()

paragraphs = text.split('\n\n')
formatted_paragraphs = []

for paragraph in paragraphs:
    
    formatted_paragraph = '    '

    
    sentences = [s.strip() for s in paragraph.split('.') if s.strip()]

    for sentence in sentences:
        
        words = sentence.split()

        
        words[0] = words[0].capitalize()

        
        current_line = ''
        for word in words:
            if len(current_line) + len(word) <= max_line_length:
                current_line += word + ' '
            else:
                
                formatted_paragraph += current_line.rstrip() + '\n' + '    '
                current_line = word + ' '

        
        formatted_paragraph += current_line.rstrip() + '.'

    
    formatted_paragraphs.append(formatted_paragraph)


formatted_text = '\n\n'.join(formatted_paragraphs)
print(formatted_text)