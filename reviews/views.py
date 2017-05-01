from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Movie, Genre, Actor, Rating

class IndexView(generic.ListView):
    template_name = 'reviews/index.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.order_by('movie_text')

class DetailView(generic.DetailView):
    model = Movie
    template_name = 'reviews/detail.html'

class ResultsView(generic.DetailView):
    model = Movie
    template_name = 'reviews/results.html'
    
def vote(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    try:
        selected_garbage = movie.garbage_set.get(pk=request.POST['garbage'])
    except (KeyError, Rating.DoesNotExist):
        return render(request, 'reviews/detail.html', {
            'movie': movie,
            'error_message': "You didn't select a rating.",
        })
    else:
        selected_garbage.votes += 1
        selected_garbage.save()
        return HttpResponseRedirect(reverse('reviews:results', args=(movie.id)))

