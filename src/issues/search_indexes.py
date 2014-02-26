import datetime
from haystack import indexes
from issues.models import Issue, IssueComment, Proposal


class IssueIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Issue
        fields = ['title', 'abstract']

    # Note that regular ``SearchIndex`` methods apply.
    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return Issue.objects.all()

#class IssueCommentIndex(indexes.ModelSearchIndex, indexes.Indexable):
#    class Meta:
#        model = IssueComment
#        fields = ['content']
#
#    # Note that regular ``SearchIndex`` methods apply.
#    def index_queryset(self, using=None):
#        "Used when the entire index for model is updated."
#        return IssueComment.objects.all()

class ProposalIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Proposal
        fields = ['title', 'content']

    # Note that regular ``SearchIndex`` methods apply.
#    def index_queryset(self, using=None):
#        "Used when the entire index for model is updated."
#        return Proposal.objects.all()
