from .models import Usuario

class UsuarioFactory:
    @staticmethod
    def crear_usuario(email, nombre, password, tipo_usuario='cliente'):
        """
        Crea un usuario del tipo correspondiente (cliente o personal).
        """
        if tipo_usuario == 'cliente':
            return Usuario.objects.create_user(email=email, nombre=nombre, password=password, tipo_usuario='cliente')
        elif tipo_usuario == 'personal':
            return Usuario.objects.create_user(email=email, nombre=nombre, password=password, tipo_usuario='personal')
        else:
            raise ValueError("Tipo de usuario no soportado")