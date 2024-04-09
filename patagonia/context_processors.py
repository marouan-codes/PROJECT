# context_processors.py
def custom_context(request):
    # Add your custom context data here
    return {
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
        # Add any other context variables needed
    }