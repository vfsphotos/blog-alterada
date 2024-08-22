from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from publication.forms import PublicationForm
from publication.models import Publication


def list_view(request):
    publications = Publication.objects.all()
    return render(request, 'index.html', {'publications': publications})

@login_required
def create_view(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            publicatin = form.save(commit=False)
            publicatin.author = request.user
            publicatin.save()
            return redirect('publication-list')
    else:
        form = PublicationForm()
    return render(request, 'create_publication.html', {'form': form})

def detail_view(request, id):
    publication = Publication.objects.filter(id=id).first()
    return render(request, 'post.html', {'publication': publication})