from haystack import indexes
from issues.models import Issue, IssueComment, Proposal
from meetings.models import Meeting, AgendaItem
from haystack.fields import IntegerField, BooleanField


class IssueIndex(indexes.ModelSearchIndex, indexes.Indexable):
    community = IntegerField(model_attr='community_id')
    class Meta:
        model = Issue
        fields = ['title', 'abstract']

    # Note that regular ``SearchIndex`` methods apply.
    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return Issue.objects.all()


class IssueCommentIndex(indexes.ModelSearchIndex, indexes.Indexable):
    community = IntegerField(model_attr='issue__community_id')
    is_open = BooleanField(model_attr='is_open')
    class Meta:
        model = IssueComment
        fields = ['content']

    # Note that regular ``SearchIndex`` methods apply.
    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return IssueComment.objects.all()


class ProposalIndex(indexes.ModelSearchIndex, indexes.Indexable):
    community = IntegerField(model_attr='issue__community_id')
    is_open = BooleanField(model_attr='is_open')
    status = IntegerField(model_attr='status')
    class Meta:
        model = Proposal
        fields = ['title', 'content']

    # Note that regular ``SearchIndex`` methods apply.
    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return Proposal.objects.all()


class MeetingIndex(indexes.ModelSearchIndex, indexes.Indexable):
    community = IntegerField(model_attr='community_id')
    class Meta:
        model = Meeting
        fields = ['title', 'comments', 'summary']

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