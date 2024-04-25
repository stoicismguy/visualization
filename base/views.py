from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .forms import DocumentForm
from .models import Document

# Create your views here.
def index(request):
    return render(request, 'index.html')



class Index(APIView):
    def get(self, request):
        form = DocumentForm()
        return render(request, 'index.html', {"form": form})

    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            newdoc = Document(user=request.user,
                              docfile=request.FILES.get('docfile'))
            newdoc.save()
        form = DocumentForm()
        return render(request, 'index.html', {"form": form})