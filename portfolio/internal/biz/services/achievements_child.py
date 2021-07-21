from portfolio.internal.biz.dao.achievements_child import AchievementsChildDao
from portfolio.models.achievements_child import AchievementsChild


class AchievementsChildService:

    @staticmethod
    def add_achievement(achievements_child: AchievementsChild):
        achievements_child, err = AchievementsChildDao().add_achievement(achievements_child)
        if err:
            return None, err
        return achievements_child, None
