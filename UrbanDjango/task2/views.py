from django.shortcuts import render
# from django.views.generic import TemplateView


def func_page(request):
    return render(request, 'func_template.html')


# class ClassPage(TemplateView):
#     template_name = 'class_template.html'
