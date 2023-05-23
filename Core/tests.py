from django.test import TestCase
from django.contrib.auth.models import User
from .models import WebsiteSetting, UserProfile, MetaInfo

# Create your tests here.

class WebsiteSettingTestCase(TestCase):
    def setUp(self):
        self.setting = WebsiteSetting.objects.create(
            name='Setting 1',
            value='Value 1'
        )

    def test_setting_str_representation(self):
        self.assertEqual(str(self.setting), 'Setting 1')

    # Add more test cases for the WebsiteSetting model

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            bio='Test bio',
            profile_pic='profile_pics/test.jpg'
        )

    def test_profile_str_representation(self):
        self.assertEqual(str(self.profile), 'testuser')

    # Add more test cases for the UserProfile model

class MetaInfoTestCase(TestCase):
    def setUp(self):
        self.meta_info = MetaInfo.objects.create(
            page_name='Page 1',
            title='Title 1',
            description='Test description',
            keywords='keyword1, keyword2'
        )

    def test_meta_info_str_representation(self):
        self.assertEqual(str(self.meta_info), 'Page 1')

    # Add more test cases for the MetaInfo model
