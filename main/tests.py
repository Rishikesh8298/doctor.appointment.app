from django.contrib.auth.models import User
from django.test import TestCase

from comment.models import Comment


# Create your tests here.

class MainTestCase(TestCase):
    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main/home.html')

    def setUp(self):
        self.credentials = {
            'username': 'user1',
            'password': 'password',
        }
        User.objects.create_user(**self.credentials)

    def test_registration_for_patient(self):
        response = self.client.post('/signup/', {
            'username': 'test1',
            'email': 'test2',
            'password': 'password1',
            'password confirmation': 'password1',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.get_by_natural_key(username='test1'))

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active, "Successfully Login")

    def test_login_templated_used(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'main/login.html')

    def test_comment_form(self):
        data = {
            'name': 'User1',
            'email': 'user1@gmail.com',
            'comment': 'This is a comment.',
        }
        comment = Comment(**data)
        comment.save()
        self.assertTrue(len(Comment.objects.filter(**data)) != 0)
