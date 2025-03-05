
from django.urls import path

import games_crud.views

urlpatterns = [
    path('', games_crud.views.home_page, name='home_page_view'),
    path('about', games_crud.views.about_us, name='about_us_view'),
    path('games', games_crud.views.all_games, name='all_games_view'),

    path('create_game', games_crud.views.add_game, name='create_game_view'),
    path('delete_game/<game_id>', games_crud.views.delete_game, name='delete_game_view'),
    path('edit_form/<game_id>', games_crud.views.get_update_form, name='edit_form_view'),
    path('update_game/<game_id>', games_crud.views.update, name='update_game_view'),
]
