from crontab import CronTab

if __name__ == '__main__':
    cron = CronTab(user='kirill')

    cron.remove_all()

    job_every_3_hours = cron.new(
        command='python3 /home/kirill/PycharmProjects/course_digital/week3/tasks/wrapper_cls.py',
        comment='every 3 hours'
    )
    job_every_3_hours.hour.every(3)
    cron.write()

    job_every_day_in_15_15 = cron.new(
        command='python3 /home/kirill/PycharmProjects/course_digital/week3/tasks/wrapper_cls.py',
        comment='every day in 15:15'
    )
    job_every_day_in_15_15.hour.also.on(15)
    job_every_day_in_15_15.minute.also.on(15)
    cron.write()

    job_every_sunday = cron.new(
        command='python3 /home/kirill/PycharmProjects/course_digital/week3/tasks/wrapper_cls.py',
        comment='every sunday in 00:00'
    )
    job_every_sunday.dow.on('SUN')
    job_every_sunday.hour.also.on(0)
    job_every_sunday.minute.also.on(0)
    cron.write()

    print(job_every_3_hours)
    print(job_every_day_in_15_15)
    print(job_every_sunday)
