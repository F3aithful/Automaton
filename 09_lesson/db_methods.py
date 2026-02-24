from sqlalchemy import create_engine
from sqlalchemy.sql import text

class  CreateOnject:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_tables(self):
        conn = self.db.connect()
        result = conn.execute(text("SELECT * FROM users"))
        rows = result.mappings().all()
        conn.close()
        return rows
    
    def get_user_by_id(self, user_id):
        with self.db.connect() as conn:
            result = conn.execute(
                text(
                    "SELECT * FROM users WHERE user_id = :user_id"),
            {
                "user_id": user_id
                }
        )
        return result.mappings().first()

    def create_object(self, user_id, user_email, subject_id):
        with self.db.connect() as conn:
            conn.execute(
                text(
                    "INSERT INTO users (user_id, user_email, subject_id) " \
                    "VALUES (:user_id, :user_email, :subject_id)"
                    ),
                {
                "user_id": user_id,
                "user_email": user_email,
                "subject_id": subject_id
                }
           )
            conn.commit()

    def update_object(self, user_email, user_id):
        with self.db.connect() as conn:
            conn.execute(
                text(
                    "UPDATE users " \
                    "SET user_email = :user_email " \
                    "WHERE user_id = :user_id"
                    ),
                    {
                        "user_email": user_email,
                        "user_id": user_id
                    }
                )
            conn.commit()

    def delete_object(self, user_id):
        with self.db.connect() as conn:
            conn.execute(
                text(
                    "DELETE FROM users " \
                    "WHERE user_id = :user_id"
                ),
                {
                    "user_id": user_id
                }
            )
            conn.commit()