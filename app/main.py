from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, init_db
from app.crud import create_user, create_appointment, get_appointments

app = FastAPI()

# Initialize the database
init_db()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user_endpoint(name: str, email: str, db: Session = Depends(get_db)):
    return create_user(db, name, email)

@app.post("/appointments/")
def create_appointment_endpoint(user_id: int, service_id: int, date_time: str, db: Session = Depends(get_db)):
    return create_appointment(db, user_id, service_id, date_time)

@app.get("/appointments/")
def get_appointments_endpoint(db: Session = Depends(get_db)):
    return get_appointments(db)
