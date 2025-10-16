import smtplib
from email.mime.text import MIMEText
from django.conf import settings

def send_notification_email(user):
    """
    Envía un email de notificación cuando se crea un nuevo usuario
    """
    try:
        # CONFIGURACIÓN TEMPORAL - PARA PRUEBAS
        # En producción usar variables de entorno
        print("=" * 50)
        print("📧 SIMULANDO ENVÍO DE EMAIL")
        print(f"Para: Administrador del Sistema")
        print(f"Asunto: Nuevo usuario registrado")
        print(f"Contenido:")
        print(f"  Nombre: {user.name}")
        print(f"  Email: {user.email}")
        print(f"  Teléfono: {user.phone}")
        print(f"  Fecha: {user.created_at}")
        print("=" * 50)
        
        # Para pruebas reales con Gmail, descomenta esto:
        """
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "tu_email@gmail.com"
        password = "tu_app_password"  # Contraseña de aplicación de Gmail
        
        subject = "🎉 Nuevo usuario registrado"
        body = f'''
        ¡Se ha registrado un nuevo usuario en el sistema!
        
        📋 Información del usuario:
        • Nombre: {user.name}
        • Email: {user.email}
        • Teléfono: {user.phone}
        • Fecha de registro: {user.created_at}
        
        Saludos,
        Sistema de Registro
        '''
        
        msg = MimeText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = sender_email  # Enviar a ti mismo
        
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        """
        
        print("✅ Notificación por email simulada exitosamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error en email: {e}")
        return False
