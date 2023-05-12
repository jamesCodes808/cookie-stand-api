from rest_framework.permissions import BasePermission, SAFE_METHODS

class isOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True

        # if we're allowing the purchaser to be null in Model
        # then this will check for that case and allow access
        if obj.owner is None:
            return True

        return obj.owner == request.user