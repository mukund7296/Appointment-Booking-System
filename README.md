# Appointment-Booking-System
using Python, SQLite, and Docker. This system will let users book, view, and cancel appointments. The app will be Dockerized and hosted locally. Follow these steps to build it:

---

### **Project Overview**
The Appointment Booking System allows users to:
- Create and store appointments.
- View a list of existing appointments.
- Update or cancel appointments.

### **Technologies**
- Backend: Python (with FastAPI for simplicity and web hosting)
- Database: SQLite
- Frontend: Optional (you can return JSON responses via FastAPI).
- Containerization: Docker

---

#### **Step 1: Create a Project Structure**
Create the following directories and files:

```plaintext
appointment_booking/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── database.py
│   ├── main.py
│   ├── crud.py
│   └── Dockerfile
├── requirements.txt
└── docker-compose.yml
```

#### **Run the Project**

1. **Build the Docker Image**  
   ```bash
   docker-compose build
   ```

2. **Start the Application**  
   ```bash
   docker-compose up
   ```

3. **Access the API**  
   Go to [http://localhost:8000/docs](http://localhost:8000/docs) to see the auto-generated API documentation and interact with the endpoints.

---

### **Bonus**
Add a frontend (optional):
- Use React.js or Flask Templates for booking appointments via a browser.
- Integrate basic HTML forms.

# Output

  <img width="1419" alt="image" src="https://github.com/user-attachments/assets/4c2223ae-353b-429f-bb1b-43591652362f" />


This project is now ready to with Docker, Python, SQLite, and FastAPI in a practical and professional setup! Let me know if you need further explanations or customizations.
