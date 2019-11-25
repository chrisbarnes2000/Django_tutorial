from django.urls import path

from .views import QuestionList, QuestionDetail

urlpatterns = [
    path("polls/", QuestionList.as_view(), name="poll_list")
    # path("polls/<int:pk>/", QuestionDetail.as_view(), name="polls_detail")
]