from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.views import APIView

# Create your views here.

class BlogViewSet2(APIView):
    
    def get(self, request  , child_id):
        if child_id :
            child = Child.objects.get(id= child_id)
            blogs = Blog.objects.filter(content_age__lte = child.age , content_gender = child.gender)
            if not blogs:
                Response({'data':'blogs does not exists for your age/gender'} , status=status)

            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)
        return Response({'status':'child_id does not exist'})

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    @action(detail=False, methods=['get'])
    def personalized_feed(self, request, pk=None):
        parent_id = request.query_params.get('parent_id')
        parent = Parent.objects.get(id=parent_id)
        child = parent.children.first()  

        blogs = Blog.objects.filter(content_age__lt=child.age)
        if child.gender:
            blogs = blogs.filter(content_gender=child.gender)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)



        