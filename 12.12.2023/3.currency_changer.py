
input_file_name = 'currencies.txt'
with open(input_file_name, 'r', encoding='utf-8') as input_file:
    text = input_file.read()


usd_exchange_rate = 430
eur_exchange_rate = 510


index = 0
while True:
    dollar_index = text.find('$', index)
    euro_index = text.find('€', index)

    if dollar_index == -1 and euro_index == -1:
        break

    if dollar_index != -1 and (euro_index == -1 or dollar_index < euro_index):
        currency_index = dollar_index
        currency = 'USD'
    else:
        currency_index = euro_index
        currency = 'EUR'


    start_index = currency_index
    #VN: start_index = currency_index - 1 подойдёт лучше
    # а условие while должно включать пробел только в том случае, если currency_index - start_index == 1,
    # чтобы учитывать только пробел между суммой и обозначением валюты
    while start_index >= 0 and (text[start_index].isdigit() or text[start_index] == '.' or text[start_index] == ' '):
        #AS: не могу найти правильное условие где будет находится цифра/число/сумма валюты
        start_index -= 1
    start_index += 1
    #VN: ^^^^^^^^ а это тоже только в том случае, если start_index != 0
    #VN: проще было текст разбить по словам, тогда не пришлось бы мучиться с посимвольным определением индексов

    end_index = currency_index
    while end_index < len(text) and (text[end_index].isdigit() or text[end_index] == '.' or text[end_index] == ' '):
        end_index += 1

  
    amount_str = text[start_index:end_index].strip()
    amount = float(amount_str)
    exchange_rate = usd_exchange_rate if currency == 'USD' else eur_exchange_rate
    converted_amount = amount * exchange_rate


    text = text[:start_index] + f'{converted_amount:.2f} ₸' + text[end_index:]


    index = start_index + len(f'{converted_amount:.2f} ₸')


output_file_name = 'output.txt'
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    output_file.write(text)