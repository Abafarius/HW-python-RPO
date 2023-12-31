def format_time(hours, minutes=None, seconds=None):

    if minutes is None:
        minutes = 0
    if seconds is None:
        seconds = 0
    #VN: можно сразу задать им значения по умолчанию 0 и избавиться от этих 4-х строк
    

    if not all(isinstance(value, int) for value in [hours, minutes, seconds]):
        raise ValueError("Все аргументы должны быть целыми числами")
    

    if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
        raise ValueError("Недопустимые значения времени")
        #VN: ^^^^^^ неплохой вариант с raise!
    

    time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    
    return time_string


hours = 10
minutes = 30
seconds = 45
formatted_time = format_time(hours, minutes, seconds)
print(formatted_time)