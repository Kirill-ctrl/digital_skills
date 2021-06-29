from crontab import CronTab


class Planner:
    def __init__(self,
                 user: str):
        self.cron = CronTab(user=True)

    def create_job_every_12_hours(self):

        job_every_12_hour = self.cron.new(
            command='python3 /home/kirill/PycharmProjects/testDigitalSpectr/course/week6/work_with_files/services/file_service.py',
            comment='every 12 hours'
        )
        job_every_12_hour.hour.every(12)
        self.cron.write()
        return job_every_12_hour

    def delete_all_job(self):
        self.cron.remove_all()


if __name__ == '__main__':
    plan = Planner(user='Kirill')
    plan.delete_all_job()
    job = plan.create_job_every_12_hours()
    print(job)
