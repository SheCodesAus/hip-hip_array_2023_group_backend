from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user

# below is from django REST api module
# from rest_framework import permissions

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True 
#         return obj.owner == request.user  ## if owner of the object is same as user, then the person does have permissions

