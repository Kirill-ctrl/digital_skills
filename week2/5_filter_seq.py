from datetime import date, datetime

seq_event = [
    {
        'name': 'event_1',
        'date': '2021-05-31',
    },
    {
        'name': 'event_2',
        'date': '2021-07-30'
    },
    {
        'name': 'event_3',
        'date': '2020-12-29'
    },
    {
        'name': 'event_4',
        'date': '2020-05-12'
    },
    {
        'name': 'event_5',
        'date': '2021-03-29',
    },
    {
        'name': 'event_6',
        'date': '2021-05-29',
    },
    {
        'name': 'event_7',
        'date': '2021-07-12'
    },
    {
        'name': 'event_8',
        'date': '2020-12-17'
    },
    {
        'name': 'event_9',
        'date': '2020-05-12'
    },
    {
        'name': 'event_10',
        'date': '2022-08-29',
    }
]

#  Выводит только будущие события
for item in filter(lambda object_dict: datetime.strptime(object_dict['date'], "%Y-%m-%d").date() > date.today(),
                   seq_event):
    print(item)
