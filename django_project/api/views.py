from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import PostSerializer
from blog.models import Post


@api_view(['PUT'])
def update_post(request, id):
    post = Post.objects.get(id=id)
    post.liked = not post.liked
    post.save()
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)
