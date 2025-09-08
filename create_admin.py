from app.core.config import SessionLocal
from app.models.user import User, Role
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_admin_user():
    db: Session = SessionLocal()
    try:
        admin_user = db.query(User).filter(User.username == "admin").first()
        if not admin_user:
            hashed_password = pwd_context.hash("admin123")
            new_admin = User(
                username="admin",
                hashed_password=hashed_password,
                role=Role.ADMIN,
            )
            db.add(new_admin)
            db.commit()
            db.refresh(new_admin)
            print("Admin user created successfully.")
        else:
            print("Admin user already exists.")
    finally:
        db.close()

if __name__ == "__main__":
    create_admin_user()
