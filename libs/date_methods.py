import calendar
from datetime import datetime, timedelta


def generate_weeks_of_year(year):
    weeks = []
    for month in range(1, 13):
        month_calendar = calendar.monthcalendar(year, month)
        for week in month_calendar:
            if week[calendar.SUNDAY]:
                start_date = datetime(year, month, week[calendar.SUNDAY])
                # end_date = start_date + timedelta(6)
                week_index = (start_date.date() - datetime(year, 1, 1).date()).days // 7
                week_start = start_date.strftime("%Y%m%d")
                week_days = {}
                for i in range(7):
                    day = start_date + timedelta(i)
                    day_of_week = calendar.day_name[day.weekday()]
                    day_date = day.strftime("%Y%m%d")
                    week_days[day_of_week] = day_date
                weeks.append((week_index, week_start, week_days))
    return weeks

def get_week_indices_of_month(year, month):
    month_calendar = calendar.monthcalendar(year, month)
    week_indices = []
    for week in month_calendar:
        if week[calendar.SUNDAY]:
            start_date = datetime(year, month, week[calendar.SUNDAY])
            week_index = (start_date.date() - datetime(year, 1, 1).date()).days // 7
            week_indices.append(week_index)
    return week_indices

if __name__ == '__main__':
    print('If you are seeing this, common.py is running as the primary script.')

    # twenty_twenty_three = generate_weeks_of_year(2023)
    # print(twenty_twenty_three)

    print(get_week_indices_of_month(2023, 1))