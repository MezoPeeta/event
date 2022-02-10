from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('new/video', views.VideoCreateView.as_view(), name="CreateVideo"),
    path('update/video/<str:pk>', views.VideoUpdateView.as_view(), name="UpdateVideo"),
    path('delete/video/<str:pk>', views.VideoDeleteView.as_view(), name="DeleteVideo"),
    path('emails/', views.SubscribersListView.as_view(), name="Emails"),

    ## ER
    path('dataframes/', views.dataFrame, name="dataframes"),
    path('datacharts/', views.ProductChartView.as_view(), name="datacharts"),
    path('datacsv/', views.exportTOCSV, name="dataCSV"),
    path('save/', views.create_report_view, name="Create_Report"),
    path('reports/', views.ReportListView.as_view(), name="Reports"),
    path('reports/<pk>', views.ReportDetailView.as_view(), name="Reports_Detail"),
    path('pdf/<pk>', views.render_pdf_view, name="Reports_PDF"),
    ##HR
    path('inbox/', views.InboxListView.as_view(), name="Inbox"),
    path('inbox/<pk>', views.InboxDetailView.as_view(), name="Inbox_Detail"),
    path('inbox/delete/<pk>', views.inbox_Delete, name="Inbox_Delete"),

]