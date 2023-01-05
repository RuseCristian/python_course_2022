from location.models import Log


class RefreshMiddleware:

    def __int__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.method == 'GET':
                new_instance = Log()
                new_instance.user_id = request.user.id
                new_instance.action = 'refresh'
                new_instance.url = request.path
                new_instance.save()
            elif request.method == 'POST':
                action = 'created'
                for item in str(request.path):
                    if item.isdigit():
                        action = 'updated'
                        break
                Log.objects.create(user_id=request.user.id, action=action, url=request.path)
        response = self.get_response(request)
        return self.get_response(request)

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.method == 'GET':
                new_instance = Log()
                new_instance.user_id = request.user.id
                new_instance.action = 'refresh'
                new_instance.url = request.path
                new_instance.save()
            elif request.method == 'POST':
                action = 'created'
                for item in str(request.path):
                    if item.isdigit():
                        action = 'updated'
                        break
                Log.objects.create(user_id=request.user.id, action=action, url=request.path)
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response