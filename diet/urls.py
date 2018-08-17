from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^signin/$', views.signin, name='signin'),
]



# 웹사이트 화면   --- >   웹 서버 (채팅서버)    --- > dialogflow (질문, 답변)

# [인텐트] 운동법요청
#  (다리 운동법) entity1 알려줘 
#  (가슴 운동법) entity2 알려줘
# 