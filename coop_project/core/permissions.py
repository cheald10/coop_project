def is_admin(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name="COOP Admins").exists())

def is_leadership(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name="Leadership").exists())

def is_coordinator(user):
    return user.is_authenticated and user.groups.filter(name="Coordinators").exists()
