from django.contrib.auth.models import User, Group

from rest_framework import permissions


class ManagerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='manager').exists()


class DeveloperPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return all([
            request.user.groups.filter(name='developer').exists(),
            request.method in permissions.SAFE_METHODS
        ])


class DeveloperTaskPermission(DeveloperPermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='developer').exists() and (
            request.method in permissions.SAFE_METHODS or (
            view.action == 'partial_update' and request.data == {'status': 'D'}
            ))


    def has_object_permission(self, request, view, obj):
        print(request.data)
        return obj.owner == request.owner
