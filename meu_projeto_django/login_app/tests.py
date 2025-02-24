from django.test import TestCase
from django.urls import reverse
from login_app.models import CustomUser  # Importe o CustomUser

class LoginViewTests(TestCase):
    def setUp(self):
        # Crie um usuário de teste com um nome de usuário e e-mail únicos
        self.user = CustomUser.objects.create_user(
            username='testuser1',  # Nome de usuário único
            email='test1@example.com',  # E-mail único
            password='testpassword'
        )

    def test_login_view_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login_app/login.html')

    def test_login_with_valid_credentials(self):
        # Cria um usuário usando o modelo personalizado
        CustomUser.objects.create_user(username='testuser', password='testpass123')

        # Simula uma solicitação de login
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })

        # Verifica se a resposta é um redirecionamento
        self.assertEqual(response.status_code, 302)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'invaliduser',
            'password': 'wrongpassword',
        })
        self.assertContains(response, 'Por favor, entre com um usuário e senha corretos.')

    def test_redirect_to_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_app/register.html')

    def test_register_view_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'login_app/register.html')