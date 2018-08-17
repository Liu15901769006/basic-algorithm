# coding=utf-8
import datetime
import calendar


def add_months(dt, months):
    month = dt.month - 1 + months
    year = dt.year + int(month / 12)
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def getbetweenmonth(begin_date, end_date):
    date_list = []
    # begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    # end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        period = []
        month_start = begin_date.strftime("%Y-%m-01")
        period.append(month_start)

        last_day = calendar.monthrange(begin_date.year, begin_date.month)[1]
        month_end = begin_date.strftime("%Y-%m-") + str(last_day)
        period.append(month_end)
        date_list.append(period)

        begin_date = add_months(begin_date, 1)
    return date_list


if __name__ == "__main__":
    # print(getbetweenmonth("2018-01-03", "2018-06-07"))
    t = datetime.date.today()
    m = add_months(t, -5)
    print(t)
    print(m)
    print(getbetweenmonth(m, t))
