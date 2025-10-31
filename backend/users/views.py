import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import User
from .email_service import send_notification_email

@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    """
    Endpoint para crear un nuevo usuario
    Ahora se comunica con el notification-service
    """
    try:
        # Leer datos del request
        data = json.loads(request.body.decode('utf-8'))
        
        print("📥 Datos recibidos:", data)
        
        # Validar campos requeridos
        required_fields = ['name', 'email', 'phone']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({'error': f'Campo requerido: {field}'}, status=400)
        
        # Verificar si el email ya existe
        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({'error': 'El email ya está registrado'}, status=400)
        
        # Crear usuario en la base de datos
        user = User.objects.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        
        print(f"✅ Usuario creado: {user.name} ({user.email})")
        
        # 🎯 NUEVO: Llamar al microservicio de notificaciones
        try:
            notification_data = {
                'name': user.name,
                'email': user.email, 
                'phone': user.phone,
                'created_at': user.created_at.isoformat()
            }
            
            # URL del notification-service (en K8s será: http://notification-service:5000)
            notification_url = "http://notification-service:5000/notify"
            
            response = requests.post(
                notification_url,
                json=notification_data,
                headers={'Content-Type': 'application/json'},
                timeout=5  # Timeout de 5 segundos
            )
            
            if response.status_code == 200:
                print("✅ Notificación enviada al microservicio")
            else:
                print(f"⚠️ Microservicio respondió con error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error comunicando con notification-service: {e}")
            # No fallar la aplicación principal si el microservicio falla
        
        # Devolver respuesta exitosa
        return JsonResponse({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'created_at': user.created_at.isoformat(),
            'message': 'Usuario creado exitosamente'
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        print(f"❌ Error general: {e}")
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["GET"])
def list_users(request):
    """
    Endpoint para listar todos los usuarios
    """
    try:
        users = User.objects.all().order_by('-created_at')
        users_list = []
        
        for user in users:
            users_list.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'phone': user.phone,
                'created_at': user.created_at.isoformat()
            })
        
        print(f"📋 Listando {len(users_list)} usuarios")
        return JsonResponse(users_list, safe=False)
        
    except Exception as e:
        print(f"❌ Error listando usuarios: {e}")
        return JsonResponse({'error': str(e)}, status=500)
