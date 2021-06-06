from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = ""
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_service"] = 1145141919
        ctxt["skill"] = [
            "Python",
            "C++",
            "Javascript",
            "Ruby",
            "Go is GOD"
        ]
        return ctxt
