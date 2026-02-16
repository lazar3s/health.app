This project has two main folders:
1. backend/  --> The Python API (FastAPI) & Database.
2. frontend/ --> The Mobile App (Flutter).

 PART 1: BACKEND SETUP (Python)
 (Everyone needs to do this to run the server)

STEP 1: Navigate to the backend folder
   Open your terminal and type:
   cd backend

STEP 2: Install Libraries
   Run this command to install FastAPI, Database tools, and Security tools:
   pip install -r requirements.txt

STEP 3: Create the Secret Password File (.env)
   I did not upload my passwords to GitHub for security.
   You must create a new file inside the 'backend' folder named ".env".
   
   Paste this text inside your new .env file:
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/creation_db
   SECRET_KEY=our_team_secret_key_123

   (Replace "YOUR_PASSWORD" with the password you set for pgAdmin).

STEP 4: Run the Server
   We renamed "main.py" to "server.py" to make it clearer.
   Run this command to start the app:
   uvicorn server:app --reload

   If it works, go to: http://127.0.0.1:8000/docs to see the API.

 PART 2: FRONTEND SETUP (Flutter)

STEP 1: Navigate to the folder
   cd frontend

STEP 2: Generate the App Files
   (Only do this if the folder is empty. If files are there, skip this).
   flutter create .

STEP 3: Run the App
   Make sure a simulator is open or a phone is plugged in.
   flutter run

 FILE GUIDE


server.py      -> The main file. Run this to start the server.
db_connect.py  -> Connects to the PostgreSQL database.
sql_tables.py  -> Defines our data tables (User, HealthProfile).
api_shapes.py  -> Defines what data we send/receive (Input/Output).
auth_tools.py  -> Handles password hashing and login tokens.

Goodluck.