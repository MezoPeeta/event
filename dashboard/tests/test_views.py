from django.test import TestCase , LiveServerTestCase
from django.shortcuts import reverse
from utils.selenium_test import TestUtils
from time import sleep
from dashboard.models import Design
from selenium.webdriver.common.by import By
from products.models import Products
from base.models import Videos, Contact 
from dashboard.views import InboxDetailView, ContactForm


class TestViews(TestCase,TestUtils):
    
    def setUp(self):
        self.login_admin()


   
    def test_us(self):
        self.user.profile.committee = "IT"
        self.user.profile.save()
        url = reverse('Dashboard')
        request = self.client.get(url) 
        #print(request.status_code)   
        self.assertEqual(request.status_code, 302)


    def test_reverse(self):
        self.user.profile.committee = "HR"
        self.user.profile.save()

        Contact.objects.create(id=1,name='Contact1',email='marwanmoatassem@gmail.com',subject='7amam',message='nam')
        url = reverse("Inbox_Detail", kwargs={"pk": 1})
    
        request = self.client.post(url,data={"reply":"Hello WOrld"}) 

        self.assertEqual(request.status_code,302)

    def test_get_context_data(self, **kwargs):
        self.user.profile.committee = "HR"
        self.user.profile.save()
        Contact.objects.create(id=1,name='Contact1',email='marwanmoatassem@gmail.com',subject='7amam',message='nam')
        url = reverse("Inbox_Detail", kwargs={"pk": 1})
        request = self.client.get(url)
        response = self.client.get(url)
        self.assertEqual(response.context["form"], ContactForm)
    def test_form_invalid(self):
        self.user.profile.committee = "HR"
        self.user.profile.save()
        
        url = reverse("Inbox_Detail", kwargs={"pk": 1})
        form = ContactForm(data={"name":"marwan","email":"marawnmoatassem@gm@@ail.com","subject":"marwan","message":"marwan","reply":"MSG"})
        self.assertTrue(form.is_valid())
        form = ContactForm(data={"name":"marwan","email":"marawnmoatassem@gm@@ail.com","subject":"marwan","message":"marwan"})
        self.assertFalse(form.is_valid())

        self.assertTrue(form.is_valid())

        self.assertFalse(form.is_valid())

    def test_InboxDelete(self):
        self.user.profile.committee = "HR"
        self.user.profile.save()
        Contact.objects.create(id=1,name='Test',email='test@gmail.com',subject='Test_Subject',message='Test_Message',reply='Test_Reply')
        url = reverse("Inbox_Delete", kwargs={"pk": 1})
        request = self.client.get(url)
        print("url:", request.status_code)
        # print("Status Code " , request.status_code)
        self.assertTemplateUsed("dashboard/HR/inbox.html")
        
    def test_change_background_color(self):
        self.user.profile.committee = "Design"
        self.user.profile.save()
        request = self.client.post
        font_btn = request.POST.get("font_btn")
        color = request.POST.get("color")
        

    # def test_VideoUpdateViewfunc(self):
    #     self.user.profile.committee = "Design"
    #     self.user.profile.save()
    #     self.video = Videos.objects.create(id=1,user=self.user,name='TestVideo')
        
    #     url = reverse('UpdateVideo', kwargs={'pk':self.video.id})
    #     self.client.post(url, data={'name': 'updated','urlID': '3cLgYSIGaJ8'})

class TestDesignDashboard(LiveServerTestCase,TestUtils):
    
    def setUp(self):
        self.selenium_admin_login()
    
    
    def test_design(self):
        self.user.profile.committee = "Design"
        self.user.profile.save()
        url = reverse("Dashboard")
        self.browser.get(self.live_server_url + url)
        color = Design.objects.filter(id=1).first().color
        element = self.browser.find_element(By.ID,'values').text
        values = element.split('\n')
        hex_color = values[0].split(' ')[1]
        self.assertEqual(color,hex_color)

    
    def test_products(self):
        self.user.profile.committee = "Logistics"
        self.user.profile.save()
        url = reverse('dataframes')
        product = Products.objects.create(id=1,user=self.user,price=10)
        print('Product',product)
        self.browser.get(self.live_server_url + url)
        name = Products.objects.filter(id=1).first().name
        id = Products.objects.filter(id=1).first().id
        price = Products.objects.filter(id=1).first().price
        element_id = self.browser.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr/td[1]').text
        element_name = self.browser.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr/td[2]').text
        element_price = self.browser.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr/td[5]').text
        self.assertEqual(element_name,name)
        self.assertEqual(id,int(element_id))
        self.assertEqual(element_price,str(price))
        self.assertTemplateUsed('dashboard/dataframes.html')
    
    
    def test_exporttocsv(self):
        url = reverse('dataCSV')
        request = self.client.post(url)
        self.assertEqual(request.status_code,200)
        self.assertEqual(request['content-type'],"text/csv")
        self.assertEqual(request['Content-Disposition'],"attachment; filename=dataframe.csv")
        request = self.client.get(url)
        self.assertEqual(request.status_code,404)
    
    
    def test_get_context_data(self):
        url = reverse('datacharts')
        response = self.client.get(url)
        self.assertQuerysetEqual(response.context['pt'],Products.objects.all())
        self.assertIsNotNone(response.context['form'])

    # def test_create_report_view(self):
    #     image = "data:image/png;base64,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"
    #     url = reverse('datacharts')
    #     request = self.client.post(url,{
    #         "image":image
    #     },)
    #     request['x-requested-with'] = "XMLHttpRequest"

    def test_change_background_color(self):
        self.user.profile.committee = "Design"
        self.user.profile.save()
        request = self.client.post
        font_btn = request.POST.get("font_btn")
        color = request.POST.get("color")
        url = reverse('Dashboard')
    
        



        




        





# How to test if element is found with selenium??
# 1 - self.browser.get(self.live_server_url + reverse(url)) -> Bt2ol le selenium ro7 lel url kza
# 2 - Get element from self.browser.find_element(By., element) by --> id, xpath, class_names
# 3 - Check element by self.assertEqual aww self.assertTrue()



# Self.client.post 
# https://stackoverflow.com/questions/49192882/writing-a-test-for-a-django-view-get-context-data-method