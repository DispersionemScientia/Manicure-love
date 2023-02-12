from django.urls import path, include
from .views import home, record_occupied, cansel_record, RecordView, RecordAddView, ShowRecordView, DeleteRecordView


app_name = 'records'
urlpatterns = [
    path('', home, name='home'),
    path('records/', RecordView.as_view(), name='records'),
    path('records/record_add', RecordAddView.as_view(), name='record_add'),
    path('records/show_record/<int:pk>/', ShowRecordView.as_view(), name='show_record'),
    path('records/record_occupied/<int:record_pk>/', record_occupied, name='record_occupied'),
    path('records/delete_record/<int:pk>/', DeleteRecordView.as_view(), name='delete_record'),
    path('records/cansel_record/<int:record_pk>/', cansel_record, name='cansel_record'),

]
