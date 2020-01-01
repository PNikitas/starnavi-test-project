from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # A post can only be changed by the admin or the author
    url = serializers.HyperlinkedIdentityField(
        view_name='post-update',
        lookup_field='pk',
    )

    class Meta:
        model = Post
        fields = ('id', 
                  'url', 
                  'author',
                  'title',
                  'desctiption',
                  'date',
                  'like',
        )