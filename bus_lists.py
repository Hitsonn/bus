from bus_class import Bus


buslist_park = [Bus('777', 'Иванов Иван Иванович', '15'),
                Bus('111', 'Петров Петр Петрович', '11'),
                Bus('333', 'Семенов Семен Семенович', '8'),
                Bus('001', 'Баранов Конствнтин Юрьевич', '15'),
                Bus('002', 'Филимонов Федор Михайлович', '11'),
                Bus('003', 'Сапелкин Дмитрий Инокентьевич', '8')]
buslist_rout = []


def add_bus_park(num):
    global buslist_park, buslist_rout
    buslist_park.append(*list(filter(lambda x: x.car_number == num, buslist_rout)))
    buslist_rout = list(filter(lambda x: x.car_number != num, buslist_rout))
