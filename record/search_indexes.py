from .models import Person
from haystack import indexes


class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Person

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
