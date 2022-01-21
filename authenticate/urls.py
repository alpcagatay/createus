from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),
    path('user_profile/', views.user_profile, name="user_profile"),
    path('add_user_story/', views.add_user_story, name="add_user_story"),
    path('my_user_stories/', views.my_user_stories, name="my_user_stories"),
    path('userstory_csv/', views.userstory_csv, name="userstory_csv"),
    path('list_userstories/', views.list_userstories, name="list_userstories"),
    path('add_category/', views.add_category, name="add_category"),
    #path('like_us/<userstory_id>', views.like_us, name="like_us"),
    #path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('delete_userstory/<userstory_id>', views.delete_userstory, name="delete_userstory"),
    path('update_userstory/<userstory_id>', views.update_userstory, name="update_userstory"),
    path('badges/', views.badges, name="badges"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('search_results', views.search_results, name="search_results"),
    path('show_userstory/<userstory_id>', views.show_userstory, name="show_userstory"),

]
