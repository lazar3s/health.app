# Creation App - Database Setup Guide

## Prerequisites
- PostgreSQL 18 installed
- pgAdmin 4

## Setup Instructions

### Step 1: Create Database
Open pgAdmin Query Tool and run:
CREATE DATABASE creation_db;

### Step 2: Run Schema (Creates all 18 tables)
1. Open pgAdmin
2. Right-click creation_db → Query Tool
3. File → Open → Select schema.sql
4. Press F5 to run

### Step 3: Load Dummy Data
1. Open Query Tool again
2. File → Open → Select seed_data.sql
3. Press F5 to run

### Step 4: Connect to Backend
Create a .env file in the backend folder:
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/creation_db
SECRET_KEY=our_team_secret_key_123

## Database Tables (18 total)
1.  users
2.  user_profiles
3.  avatars
4.  health_goals
5.  biomarker_data
6.  activity_tracking
7.  wellness_logs
8.  medications
9.  appointments
10. badges
11. user_badges
12. user_gamification
13. challenges
14. challenge_participants
15. user_follows
16. messages
17. chatbot_conversations
18. health_reports
19. notifications
20. audit_logs

## Sample Users for Testing
| Email | Role |
|-------|------|
| john.doe@example.com | User |
| jane.smith@example.com | User |
| mike.wilson@example.com | User |
| dr.sarah@hospital.com | Healthcare Professional |
| admin@creation.com | Admin |

## Created by
Ahmed Khan - Database Administrator
Group 2 - F29SO Software Engineering