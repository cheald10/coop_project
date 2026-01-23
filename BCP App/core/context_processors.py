from .models import Division

def current_division(request):
    """
    Injects `division` into the template context when the URL
    contains a `division_id` or `pk` that refers to a Division.
    """
    division = None
    resolver_match = getattr(request, "resolver_match", None)

    if not resolver_match:
        return {"division": None}

    kwargs = resolver_match.kwargs

    # Common patterns in your URLs: division_id or pk
    division_id = kwargs.get("division_id") or kwargs.get("pk")

    if division_id:
        try:
            division = Division.objects.get(pk=division_id)
        except Division.DoesNotExist:
            division = None

    return {"division": division}
