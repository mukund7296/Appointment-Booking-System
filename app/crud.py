from sqlalchemy.orm import Session
from app.models import User, Appointment, Service

def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_appointment(db: Session, user_id: int, service_id: int, date_time):
    appointment = Appointment(user_id=user_id, service_id=service_id, date_time=date_time)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def get_appointments(db: Session):
    return db.query(Appointment).all()
