from django.test import TestCase
from .models import Task
# Create your tests here.
class TestTask(TestCase):
    def setUp(self):
        Task.objects.create(title="ab dadan be golha", done=False)
        Task.objects.create(title="ghaza dadan be gorbe ha", done=True)

    def test_task_str(self):
        task = Task.objects.get(done=False)
        self.assertEqual(task.__str__(), "ab dadan be golha")
        task = Task.objects.get(done=True)
        self.assertEqual(task.__str__(), "ghaza dadan be gorbe ha")
