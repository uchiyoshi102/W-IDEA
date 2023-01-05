from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Topic

# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username ="testuser", email="test@email.com", password="secret"
        )
        
        cls.post = Topic.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/topic/1/")
        
    def test_rul_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/topic/1/")
    
        self.assertEqual(response.status_code, 200)
        
    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "home.html")
        
    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"topic_pk": self.post.pk}))
        no_response = self.client.get("/topic/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "topic_detail.html")
        
        
    def test_post_createview(self):
        response = self.client.post(
            reverse("topic_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Topic.objects.last().title, "New title")
        self.assertEqual(Topic.objects.last().body, "New text")

    def test_post_updateview(self):
        response = self.client.post(
            reverse("topic_edit", args = "1"),
            {
                "title": "Update title",
                "body": "Update text",
            },
        )        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Topic.objects.last().title, "Update title")
        self.assertEqual(Topic.objects.last().body, "Update text")
        
    def test_post_deleteview(self):
        response = self.client.post(reverse("topic_delete", args = "1"))
        self.assertEqual(response.status_code, 302)
        