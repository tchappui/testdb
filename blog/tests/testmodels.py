from django.test import TestCase
from blog.models import Article

# models test
class BlogModelTest(TestCase):

    def create_article(self, title="only a test", content="yes, this is only a test"):
        return Article.objects.create(title=title, content=content)

    def test_article_creation(self):
        article = self.create_article()
        self.assertTrue(isinstance(article, Article))
        self.assertEqual(str(article), article.title)
        self.assertEqual(article.content, "yes, this is only a test")
