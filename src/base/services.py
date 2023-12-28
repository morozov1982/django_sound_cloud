from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, filename):
    """Построение пути к файлу аватара, format: (media)/avatar/<user_id>/<filename>"""
    return f"avatar/{instance.id}/{filename}"


def validate_size_image(image):
    """Проверка размера файла"""
    megabytes_limit = 2
    if image.size > 1024 * 1024 * megabytes_limit:
        raise ValidationError(f"Максимальный размер файла {megabytes_limit} Мб")
