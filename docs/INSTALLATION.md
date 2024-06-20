# Installation Guide

## Prerequisites
- Python 3.7+
- Node.js
- pip
- npm or yarn

## Steps

1. Clone the repository:

git clone https://github.com/yourusername/Healthcare-Accessibility.git

cd Healthcare-Accessibility


2. Install backend dependencies:

cd backend

pip install -r requirements.txt


3. Install frontend dependencies:

cd ../frontend/web

npm install


4. Run initial setup:

cd ../../backend

python manage.py migrate

python manage.py runserver

For the frontend:

cd ../frontend/web

npm start

