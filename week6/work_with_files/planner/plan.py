from crontab import CronTab


class Planner:
    """Base planner for make job"""
    def __init__(self,
                 user: str or bool):
        self.cron = CronTab(user=user)

    def create_job_every_12_hours(self):
        """create a task every 12 hours"""
        job_every_12_hour = self.cron.new(
            command='python3 /home/kirill/PycharmProjects/testDigitalSpectr/course/week6/work_with_files/services/file_service.py',
            comment='every 12 hours'
        )
        job_every_12_hour.hour.every(12)
        self.cron.write()
        return job_every_12_hour

    def delete_all_job(self):
        """Delete all existing tasks"""
        self.cron.remove_all()


if __name__ == '__main__':
    plan = Planner(user=True)
    plan.delete_all_job()
    job = plan.create_job_every_12_hours()
    print(job)
