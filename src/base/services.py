import os.path

from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, filename):
    """Построение пути к файлу аватара, format: (media)/avatar/<user_id>/<filename>"""
    return f"avatar/user_{instance.id}/{filename}"


def get_path_upload_cover_album(instance, filename):
    """Построение пути к файлу обложки альбома, format: (media)/album/<user_id>/<filename>"""
    return f"album/user_{instance.user.id}/{filename}"


def get_path_upload_track(instance, filename):
    """Построение пути к треку, format: (media)/track/<user_id>/<filename>"""
    return f"track/user_{instance.user.id}/{filename}"


def get_path_upload_cover_playlist(instance, filename):
    """Построение пути к обложке плейлиста, format: (media)/playlist/<user_id>/<filename>"""
    return f"playlist/user_{instance.user.id}/{filename}"


def validate_size_image(image):
    """Проверка размера файла"""
    megabytes_limit = 2
    if image.size > 1024 * 1024 * megabytes_limit:
        raise ValidationError(f"Максимальный размер файла {megabytes_limit} Мб")


def delete_old_file(path_file):
    """Удаление старого файла"""
    if os.path.exists(path_file):
        os.remove(path_file)
