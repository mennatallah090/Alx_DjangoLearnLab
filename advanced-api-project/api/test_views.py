from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        # Sample data
        self.book_data = {'title': 'Sample Book', 'author': 'Author Name', 'isbn': '1234567890'}
        self.book = Book.objects.create(**self.book_data)
        self.url_list = reverse('book-list')  # Assuming your book list view uses this name
        self.url_detail = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        response = self.client.post(self.url_list, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_get_book(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        updated_data = {'title': 'Updated Book', 'author': 'Updated Author', 'isbn': '0987654321'}
        response = self.client.put(self.url_detail, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, updated_data['title'])

    def test_delete_book(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books(self):
        # Add filter query params to your URL and test
        response = self.client.get(self.url_list, {'author': self.book_data['author']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Should return at least 1 book

    def test_search_books(self):
        # Search by title
        response = self.client.get(self.url_list, {'search': 'Sample'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_order_books(self):
        # Order by title
        response = self.client.get(self.url_list, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_unauthorized_access(self):
        # Logout and try to access the endpoints
        self.client.logout()
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
