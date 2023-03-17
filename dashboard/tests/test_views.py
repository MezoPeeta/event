# from django.test import TestCase, RequestFactory
# from django.shortcuts import reverse 
# from utils.selenium_test import TestUtils
# from base.models import Videos
# from dashboard.views import VideoUpdateView

# class TestingUpdateVideo(TestCase,TestUtils):
#     def setUp(self):
#         self.login_admin()
#         self.video = Videos.objects.create(user = self.user, urlID="id", name="name")
#         self.user.profile.committee = "PR"
#         self.user.profile.save()

#         self.form_data = {"name":"new name", "urlID":"new id"}

#         self.url = reverse('UpdateVideo', kwargs={"pk":self.video.pk})
        
#     def test_video_update_view(self):
        
#         request = self.client.post(self.url, self.form_data )     
#         self.assertEqual(request.status_code, 302)
#     def test_test_func(self):
#         request = RequestFactory().get(self.url)
#         view = VideoUpdateView()
#         view.setup(request)
#         # response = VideoUpdateView.as_view()(request, kwargs={'pk':self.video.pk})
#         view.test_func()
#         # self.assertTrue(view.test_func())
    
