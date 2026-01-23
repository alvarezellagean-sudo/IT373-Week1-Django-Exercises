from django.test import TestCase
from .models import Announcement

class AnnouncementModelTest(TestCase):

    def setUp(self):
        Announcement.objects.create(title="Test Announcement", content="This is a test announcement.")

    def test_announcement_content(self):
        announcement = Announcement.objects.get(id=1)
        expected_object_name = f'{announcement.title}'
        self.assertEqual(expected_object_name, 'Test Announcement')