from course.week7.connection.base_session import SessionConn
from course.week7.models.category import Category


class CategoryService:

    @staticmethod
    def get_list_category():
        with SessionConn.get_session() as sess:
            res = sess.query(Category).all()
        return [
            {
                "id": item.Category._id,
                "title": item.Category.title
            }
            for item in res
        ]

    @staticmethod
    def get_category_by_id(category_id: int):
        with SessionConn.get_session() as sess:
            res = sess.query(Category).filter(Category.id == category_id).first()
        return res
