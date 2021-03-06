from institute.models import InstituteProfile


class AttachInstituteDataMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        institute = InstituteProfile.objects.get(active=True)
        self.institute = institute

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        response.context_data["request_institute"] = self.institute
        return response
