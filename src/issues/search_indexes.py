import datetime
from haystack import indexes
from isues.models import Issue, Proposal


class IssueIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Issue
        fields = ['title', 'abstract']
    #IssueComment

    # Note that regular ``SearchIndex`` methods apply.
    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return Issue.objects.all()


class ProposalIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Proposal
        fields = ['title', 'content']

    # Note that regular ``SearchIndex`` methods apply.
    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return Issue.objects.all()