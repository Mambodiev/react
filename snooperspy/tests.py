from django.test import TestCase
from django.contrib.auth.models import User
from snooperspy.models import Product, Category


class Test_Create_Product(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        test_product = Product.objects.create(category_id=1, title='Product Title', excerpt='Product Excerpt',
                                        content='Product Content', slug='Product-title', author_id=1, status='published')

    def test_snooperspy_content(self):
        product = Product.productobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{product.author}'
        excerpt = f'{product.excerpt}'
        title = f'{product.title}'
        content = f'{product.content}'
        status = f'{product.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'product Title')
        self.assertEqual(content, 'product Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(product), "Product Title")
        self.assertEqual(str(cat), "django")
