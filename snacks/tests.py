from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.

class SanckTest(TestCase):
    def test_snack_list_status(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_list.html')



    def setUp(self):

        self.user=get_user_model().objects.create_user(
            username='ibrahimanaseer',
            email='ibrahim@test.com',
            password='test')

        self.snack=Snack.objects.create(
            title='cordon blue',
            description='bread with cheese ,chicken',
            purchaser=self.user 
        )


    def test_str_method(self):
        self.assertEqual(str(self.snack),'cordon blue')    

    def test_detail_view(self):
        url = reverse('snack_detail',args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')


    def test_create_view(self):

        data={
            'title':'snack',
            'description':'test',
            'purchaser':self.user.id

         }
        url = reverse('snack_create')
        response= self.client.post(path=url,data=data,follow=True)
        self.assertRedirects(response,reverse('snacks_list'))


    def test_update_view(self):

        data={
            'title':'burger',
            'description':'test',
            'purchaser':self.user.id

         }
        url = reverse('snack_update',args=[self.snack.id])
        response= self.client.post(path=url,data=data,follow=True)
        self.assertRedirects(response,reverse('snacks_list'))



    def test_delete_view(self):
        url = reverse('snack_delete',args=[self.snack.id])
        response= self.client.post(path=url)
         
        self.assertRedirects(response,reverse('snacks_list'))