from django.urls import path
from . import views
from products import views as product_views

urlpatterns = [
    path("dashboard/", views.dashboard, name="Dashboard"),
    path("new/video", views.VideoCreateView.as_view(), name="CreateVideo"),
    path("update/video/<str:pk>", views.VideoUpdateView.as_view(), name="UpdateVideo"),
    path("delete/video/<str:pk>", views.VideoDeleteView.as_view(), name="DeleteVideo"),
    path("emails/", views.SubscribersListView.as_view(), name="Emails"),
    path(
        "new/product/",
        product_views.ProductsCreateView.as_view(),
        name="CreateProducts",
    ),
    ## ER
    # path("dataframes/", views.data_frame, name="dataframes"),
    path("datacharts/", views.ProductChartView.as_view(), name="datacharts"),
    # path("datacsv/", views.export_to_csv, name="dataCSV"),
    path("save/", views.create_report_view, name="Create_Report"),
    path("reports/", views.ReportListView.as_view(), name="Reports"),
    path("reports/<pk>/", views.ReportDetailView.as_view(), name="Reports_Detail"),
    path("pdf/<pk>", views.render_pdf_view, name="Reports_PDF"),
    ##HR
    path("inbox/", views.InboxListView.as_view(), name="Inbox"),
    path("inbox/<pk>/", views.InboxDetailView.as_view(), name="Inbox_Detail"),
    path("inbox/delete/<pk>/", views.inbox_delete, name="Inbox_Delete"),
    ## Design
    path("change_bg_color/", views.change_background_color, name="ChangeBgColor"),
    # path('get_palette_color/', views.get_colors_palette, name="getPaletteColor"),
]
