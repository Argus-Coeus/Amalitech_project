from django.test import SimpleTestCase
from django.urls import reverse,resolve
from api.views import PostDetail,PostList,CreateList,UserDetail,UserList,CustomResetPasswordConfirmView

class TestUrls(SimpleTestCase):

    def test_create_url_is_resolved(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func.view_class,CreateList)

