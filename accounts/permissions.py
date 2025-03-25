from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # Админы могут всё, остальные — нет доступа даже к списку
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Админ может всё, пользователь — только сам себя
        if request.user and request.user.is_staff:
            return True
        return obj == request.user
