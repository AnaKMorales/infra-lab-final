from flask import Flask, request, jsonify
import os
import logging

app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar que el servicio está vivo"""
    return jsonify({"status": "healthy", "service": "notification-service"})

@app.route('/notify', methods=['POST'])
def notify():
    """
    Microservicio de notificaciones
    Recibe: POST /notify con JSON de usuario
    """
    try:
        # Log de la solicitud recibida
        logger.info("📨 Solicitud de notificación recibida")
        
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        # Extraer datos del usuario
        user_name = data.get('name', 'N/A')
        user_email = data.get('email', 'N/A')
        user_phone = data.get('phone', 'N/A')
        
        # Simular envío de notificación (igual que antes)
        print("=" * 60)
        print("🔔 NOTIFICATION-SERVICE: Notificación por email")
        print(f"   Usuario: {user_name}")
        print(f"   Email: {user_email}")
        print(f"   Teléfono: {user_phone}")
        print("=" * 60)
        
        logger.info(f"Notificación procesada para: {user_name}")
        
        return jsonify({
            "status": "success",
            "message": "Notificación procesada exitosamente",
            "user": user_name
        }), 200
        
    except Exception as e:
        logger.error(f"Error en notification-service: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
