import csv


def get_by_date(date, name=None, filename='dump.csv'):
    fields = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']

    dictobj = csv.DictReader(open('sorted_for_date.csv'))  # чтение данных
    dictobj = list(dictobj)
    # поиск примерно среднего индекса по алгоритму фибоначи
    size = len(dictobj) - 1
    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    mid = None
    while (f2 < size + 1):
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while (f2 > 1):
        index = min(start + f0, size)
        if dictobj[index]['date'] < date:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif dictobj[index]['date'] > date:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            mid = index
            break
    if (f1) and (dictobj[size]['date'] == date):
        mid = size

    # присвоим начальные значения границам, не выходящие за допустимые пределы
    begin = max(0, mid)
    end = min(mid + 1, size)

    if mid:
        writer = csv.DictWriter(open(filename, "w", newline=''), fieldnames=fields)  # запись данных
        writer.writeheader()
        list_rows = []
        if name:  # если есть отбор по имени
            while dictobj[begin]['date'] == date:  # перебираем строки вверх от среднего индекса
                if dictobj[begin]['Name'] == name:
                    writer.writerow(dictobj[begin])
                    list_rows.append(dictobj[begin])
                begin -= 1
                if begin < 1:
                    break
            while dictobj[end]['date'] == date:  # перебираем строки вниз от среднего индекса
                if dictobj[end]['Name'] == name:
                    writer.writerow(dictobj[end])
                    list_rows.append(dictobj[end])
                end += 1
                if end > size - 1:
                    break
        else:  # если нет отбора по имени
            while dictobj[begin]['date'] == date:  # перебираем строки вверх от среднего индекса
                writer.writerow(dictobj[begin])
                list_rows.append(dictobj[begin])
                begin -= 1
                if begin < 1:
                    break
            while dictobj[end]['date'] == date:  # перебираем строки вниз от среднего индекса
                writer.writerow(dictobj[end])
                list_rows.append(dictobj[end])
                end += 1
                if end > size - 1:
                    break
        return list(list_rows)  # list_rows только для демострации вывода

    return None


if __name__ == '__main__':
    rez = get_by_date(date="2013-02-11", name="PCLN", filename='dump.csv')
    for each in rez:
        print(each)
