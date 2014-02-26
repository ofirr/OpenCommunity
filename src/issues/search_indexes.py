import datetime
from haystack import indexes
from issues.models import Issue, IssueComment, Proposal
from haystack.fields import IntegerField


class IssueIndex(indexes.ModelSearchIndex, indexes.Indexable):
    community = IntegerField(model_attr='community_id')
    class Meta:
        model = Issue
        fields = ['title', 'abstract']

    # Note that regular ``SearchIndex`` methods apply.
    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return Issue.objects.all()


class ProposalIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Proposal
        fields = ['title', 'content']

    # Note that regular ``SearchIndex`` methods apply.
#    def index_queryset(self, using=None):
#        "Used when the entire index for model is updated."
#        return Proposal.objects.all()
