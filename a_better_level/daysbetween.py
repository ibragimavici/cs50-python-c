def CalcLeapYear (year):
    if year % 4 == 0:
        if year % 100:
            if year % 400:
                return 29
            return 28
        return 29
    return 28


def DaysOfMonths(month, year):
    MonthList = [31, CalcLeapYear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return MonthList[(month-1)]



def DaysBetween (d1, m1, y1, d2, m2, y2):
    DayCount = 0
    DayWhileCounting = d1
    MonthWhileCounting = m1
    YearWhileCounting = y1

    while not (DayWhileCounting, MonthWhileCounting, YearWhileCounting) == (d2, m2, y2):
        DayCount = DayCount + 1
        DayWhileCounting = DayWhileCounting + 1
        if DayWhileCounting > DaysOfMonths(MonthWhileCounting, YearWhileCounting):
            DayWhileCounting = 1
            MonthWhileCounting = MonthWhileCounting + 1
            if MonthWhileCounting > 12:
                MonthWhileCounting = 1
                YearWhileCounting = YearWhileCounting + 1

    return DayCount

def CheckIfPossibleDate(d1, m1, y1, d2, m2, y2):
    if d1 > DaysOfMonths(m1, y1):
        return False
    if d2 > DaysOfMonths(m2, y2):
        return False
    if m1 > 12 or m2 > 12:
        return False

    else:
        return True


def CheckIfBefore (d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return False
    elif y1 == y2:
        if m1 > m2:
            return False
        elif m1==m2:
            if d1 > d2:
                return False
            elif d1 == d2:
                return False
    if CheckIfPossibleDate(d1, m1, y1, d2, m2, y2):
        return True

def DaysBetweenDates (d1, m1, y1, d2, m2, y2):
    if CheckIfBefore(d1, m1, y1, d2, m2, y2):
        print(DaysBetween(d1, m1, y1, d2, m2, y2))

    elif CheckIfBefore(d1, m1, y1, d2, m2, y2) == False:
        print("uncorrect date format")




DaysBetweenDates(20, 11, 2005, 29, 2, 2021)
