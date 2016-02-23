'''
Desarrolla un programa que convierta de una hora
dada en AM/PM a formato de 24 horas.
'''


def to_24hrs(str_time):
    numbers = str_time[0:-2]
    am_pm = str_time[-2:]

    if am_pm == "AM":
        print(numbers)
    elif am_pm == "PM":
        splitted_numbers = numbers.split(":")
        splitted_numbers[0] = str(
            int(splitted_numbers[0]) + 12
            )
        print(":".join(splitted_numbers))
    else:
        print("La hora no está bien formada.")

to_24hrs("07:50:30PM")
to_24hrs("07:50:30AM")
