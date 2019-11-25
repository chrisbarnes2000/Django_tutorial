from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from polls.models import Question, Choice
from .serializers import QuestionSerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # def get(self, request):
    #     questions = Question.objects.all()[:20]
    #     data = QuestionSerializer(questions, many=True).data
    #     return Response(data)

class QuestionDetail(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # def get(self, request, pk):
    #     question = get_object_or_404(Question, pk=pk)
    #     data = QuestionSerializer(question).data
    #     return Response(data)
