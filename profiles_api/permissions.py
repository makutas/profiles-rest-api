from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True # HTTP GET method is safe
        # here we need to check if user who is trying to make other requests for the object
        # such as PUT or PATCH has authenticated to that object as a authenticated user.
        return obj.id == request.user.id
        # this will return True if object id is equal to user id - otherwise False


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
        # checks if object getting modified has the same user profile id as the user
        # modifying the profile.