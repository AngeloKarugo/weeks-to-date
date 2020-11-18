from datetime import datetime
import math

today = datetime.now()

year = input('Enter the year: \n')
month = input('Enter the month: \n')
day = input('Enter the day: \n')


def weeks_to_date(year, month, day):
    """
    calculate the number of weeks to a certain date, playing around with date functions
    """
    target = datetime(year=int(year), month=int(month), day=int(day))

    gap = target - today

    if gap.days > 7:
        weeks = math.floor(gap.days / 7)
        remainder_days = gap.days - (weeks * 7)
    elif gap.days < -7:
        weeks = math.ceil(gap.days / 7)
        remainder_days = gap.days - (weeks * 7)
    else:
        weeks = 0
        remainder_days = gap.days

    return {'weeks': weeks, 'remainder_days': remainder_days}


if weeks_to_date(year, month, day)['weeks'] < 0:
    # target date is in the past
    if weeks_to_date(year, month, day)['remainder_days'] == 0:
        print(day+'/'+month+'/'+year+' was exactly', abs(weeks_to_date(year, month, day)
                                                          ['weeks']), 'weeks ago.')
    else:
        print(day+'/'+month+'/'+year+' was ', abs(weeks_to_date(year, month, day)
                                                  ['weeks']), 'weeks ', abs(weeks_to_date(year, month, day)['remainder_days']), 'days ago.')
else:
    print(weeks_to_date(year, month, day)['weeks'], 'weeks ', weeks_to_date(
        year, month, day)['remainder_days'], ' days to ' + day + '/'+month+'/'+year)
