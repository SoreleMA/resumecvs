from django.urls import path
from api.cv.views import (
    AdminCurriculumListView, 
    AdminCurriculumDetailView, 
    ClientCurriculumListView, 
    ClientCurriculumDetailView, 
    CompanyCurriculumListView,
    EducationListCreateAPIView,
    EducationDetailAPIView,
    ExperienceListCreateAPIView,
    ExperienceDetailAPIView
)

urlpatterns = [
    path('admin/curriculum/', AdminCurriculumListView.as_view(), name='admin-curriculum-list-create'),
    path('admin/curriculum/<int:id>/', AdminCurriculumDetailView.as_view(), name='admin-curriculum-detail'),
    path('client/curriculum/', ClientCurriculumListView.as_view(), name='client-curriculum-list-create'),
    path('client/curriculum/<int:id>/', ClientCurriculumDetailView.as_view(), name='client-curriculum-detail'),
    path('company/curriculum/', CompanyCurriculumListView.as_view(), name='company-curriculum-list'),
    path('education/', EducationListCreateAPIView.as_view(), name='education-list-create'),
    path('education/<int:pk>/', EducationDetailAPIView.as_view(), name='education-detail'),
    path('experience/', ExperienceListCreateAPIView.as_view(), name='experience-list-create'),
    path('experience/<int:pk>/', ExperienceDetailAPIView.as_view(), name='experience-detail'),
]
