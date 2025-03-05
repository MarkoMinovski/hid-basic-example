from django.shortcuts import redirect, render, loader, HttpResponse, get_object_or_404
from .models import VideoGame
from .forms import VideoGameForm

# Create your views here.


def home_page(request):
    return render(request, 'games_crud/home_page.html')


def about_us(request):
    return render(request, 'games_crud/about_us.html')


def all_games(request):
    template = loader.get_template('games_crud/games.html')

    context = {
        'games': VideoGame.objects.all().order_by('-listing_posted'),
        'form': VideoGameForm()
    }

    return HttpResponse(template.render(context, request))


def add_game(request):

    if request.method == 'POST':
        form = VideoGameForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('all_games_view')


def delete_game(request, game_id):
    game = get_object_or_404(VideoGame, pk=game_id)
    if request.method == 'POST':
        game.delete()

    return redirect('all_games_view')


def get_update_form(request, game_id):
    game = get_object_or_404(VideoGame, pk=game_id)
    form = VideoGameForm(instance=game)

    return render(request, 'games_crud/edit_form.html', {'form': form, 'game': game})


def update(request, game_id):
    game = get_object_or_404(VideoGame, pk=game_id)
    if request.method == 'POST':
        form = VideoGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()

    return redirect('all_games_view')
