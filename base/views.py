from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from .forms import DocumentForm
from .models import Document
from .visual_tools import generate_visualization_tree, get_active_file

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
    documents = Document.objects.filter(user=request.user).order_by('-time')
    return render(request, "my_files.html", {"documents": documents})


def visualization_view(request, file_id):
    file = Document.objects.get(id=file_id)
    open_file = get_active_file(file.docfile.path)
    on_checkboxes = request.GET.keys()




    on_checkboxes_out = list(map(int, list(on_checkboxes)))
    all_checkboxes_out = [x+1 for x in range(open_file.max_column)]
    on_checkboxes=set([x-1 for x in on_checkboxes_out])


    if len(set(on_checkboxes_out)) != 0:
        set_to_delete = reversed(list(set(list(range(open_file.max_column))) - set(on_checkboxes)))
        for i in set_to_delete:
            open_file.delete_cols(i+1, 1)
    else:
        on_checkboxes_out = [x+1 for x in range(open_file.max_column)]
        print(on_checkboxes_out)


    tree_node = generate_visualization_tree(open_file)
    return render(request, "visual.html", {"node": tree_node,
                                           "file_name": file.docfile.name,
                                           "user": request.user,
                                           "columns":all_checkboxes_out,
                                           "checked": on_checkboxes_out})


def delete_file(request, file_id):
    doc = Document.objects.get(id=file_id, user=request.user)
    if doc is not None:
        doc.docfile.delete()
        doc.delete()
        # doc.save()
    return redirect("files")