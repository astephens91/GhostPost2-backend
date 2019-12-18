from rest_framework.serializers import HyperlinkedModelSerializer
from GhostProject.models import Post


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['is_boast',
                  'content',
                  'author',
                  'up_votes',
                  'down_vote',
                  'post_date',
                  'net_votes']