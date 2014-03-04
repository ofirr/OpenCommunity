from haystack import indexes
from meetings.models import Meeting, AgendaItem
from haystack.fields import IntegerField, BooleanField


class MeetingIndex(indexes.ModelSearchIndex, indexes.Indexable):
    community = IntegerField(model_attr='community_id')
    class Meta:
        model = Meeting
        fields = ['title', 'summary']

    # Note that regular ``SearchIndex`` methods apply.
    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return Meeting.objects.all()


class AgendaItemIndex(indexes.ModelSearchIndex, indexes.Indexable):
    community = IntegerField(model_attr='meeting__community_id')
    class Meta:
        model = AgendaItem
        fields = ['background']

    # Note that regular ``SearchIndex`` methods apply.
    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return AgendaItem.objects.all()