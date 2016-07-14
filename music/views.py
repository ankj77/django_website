from .models import Album,Song
from django.views import  generic
from django.core.urlresolvers import reverse_lazy
from  django.views.generic.edit import  UpdateView,DeleteView,CreateView

class IndexView( generic.ListView ) :
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

    # def get_queryset(self):

class AlbumCreate(CreateView) :
    model = Album
    fields = ['artist','genre','album_title','album_logo']

class AlbumUpdate(UpdateView) :
    model = Album
    fields = ['artist','genre','album_title','album_logo']

class AlbumDelete(DeleteView) :
    model = Album
    success_url = reverse_lazy( 'music:index' )


# from  django.shortcuts import  render , get_object_or_404
# def index (request) :
#     all_albums = Album.objects.all()
#     context = {'albums' : all_albums}
#     return render(request,'music/index.html',context)
#
#
#
# def detail(request,album_id):
#     album =  get_object_or_404(Album,pk = album_id)
#     context = {'album': album}
#     return render(request,'music/detail.html',context)

# def favorite(request,album_id) :
#     album = get_object_or_404(Album, pk=album_id)
#
#     try:
#         song = album.song_set.get(pk = request.POST['song'])
#     except (KeyError , Song.DoesNotExist ):
#         context = {'album': album , 'error_message':"You didn't correct song",}
#         return render(request,'music/detail.html',context)
#
#     song.is_favorite  = True
#     song.save()
#     context = {'album': album,}
#     return render(request, 'music/detail.html', context)


