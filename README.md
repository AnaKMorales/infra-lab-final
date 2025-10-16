# Sistema de Registro de Usuarios - Ejercicio 1

## Descripción
Aplicación Full-Stack para registro de usuarios con notificaciones por email.

## Estructura Principal
infra-lab-final/
├── backend/
│ ├── users/ (app Django)
│ ├── user_registration/ (configuración)
│ ├── manage.py
│ └── requirements.txt
└── frontend/
└── index.html

text

## Instalación
```bash
# Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend (otra terminal)
cd frontend
python3 -m http.server 8001
