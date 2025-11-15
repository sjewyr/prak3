import socket

def hostname(request):
    """Добавляет hostname в контекст шаблонов для демонстрации балансировки нагрузки"""
    return {'hostname': socket.gethostname()}
