from django.contrib.auth.mixins import UserPassesTestMixin

class DeleveryManPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_deleveryman