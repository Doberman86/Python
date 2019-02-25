def lucky_ticket(ticket_number):
    tn_list=str(ticket_number)
    if len(tn_list) != 6: return False
    first=0
    last=0
    for i in range(3):
        first+=int(tn_list[i])
        last+=int(tn_list[-i-1])
    return first==last

def test(got, expected):
    prefix = "OK" if got == expected else "X"
    print("{0} - Получено: {1} | Ожидалось: {2}".format(prefix, repr(got), repr(expected)))

print("Задача 1. Округление.")
test(my_round(5.234,2),5.23)
test(my_round(5.255,2),5.26)
test(my_round(-5.245,1),-5.2)
test(my_round(-5.255,1),-5.3)

print("\nЗадача 2. Билет.")
test(lucky_ticket(345534),True)
test(lucky_ticket("045414"),True)
test(lucky_ticket(345043),False)
test(lucky_ticket(345542),False)
