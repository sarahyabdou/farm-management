from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only allow owners to edit or delete.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
