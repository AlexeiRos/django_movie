from django import template
from movies.models import Category, Movie, Serial


register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count=5):
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies": movies}


@register.inclusion_tag('movies/tags/last_serial.html')
def get_last_serials(count=5):
    serials = Serial.objects.order_by("id")[:count]
    return {"last_serials": serials}
