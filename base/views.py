from django.shortcuts import render, redirect
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
        return render(request, 'index.html', {"form": form, "user":request.user})

    def post(self, request):
        print("FORM")
        form = DocumentForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            newdoc = Document(user=request.user,
                              docfile=request.FILES.get('docfile'))
            newdoc.save()
        form = DocumentForm()
        return redirect("index")
        # return render(request, 'index.html', {"form": form})
    

def files_view(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, "my_files.html", {"documents": documents})


def visualization_view(request, file_id):
    return redirect("files")


def delete_file(request, file_id):
    doc = Document.objects.get(id=file_id, user=request.user)
    if doc is not None:
        doc.docfile.delete()
        doc.delete()
        # doc.save()
    return redirect("files")