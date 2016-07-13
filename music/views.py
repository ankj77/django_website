from .models import Album,Song
from  django.shortcuts import  render , get_object_or_404
def index (request) :
    all_albums = Album.objects.all()
    context = {'albums' : all_albums}
    return render(request,'music/index.html',context)



def detail(request,album_id):
    album =  get_object_or_404(Album,pk = album_id)
    context = {'album': album}
    return render(request,'music/detail.html',context)

def favorite(request,album_id) :
    album = get_object_or_404(Album, pk=album_id)

    try:
        song = album.song_set.get(pk = request.POST['song'])
    except (KeyError , Song.DoesNotExist ):
        context = {'album': album , 'error_message':"You didn't correct song",}
        return render(request,'music/error.html',context)

    song.is_favorite  = True
    song.save()
    context = {'album': album,}
    return render(request, 'music/detail.html', context)
