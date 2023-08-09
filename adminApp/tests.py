from django.test import TestCase

from doctor.models import DoctorInfo
from doctor.models import User


# Create your tests here.
class UnitTestCase(TestCase):
    def setUp(self):
        self.admin = {
            "username": "admin",
            "password": "password"
        }
        User.objects.create_superuser(**self.admin)

    def test_add_doctor_template(self):
        response1 = self.client.post("/login/", self.admin, follow=True)
        response2 = self.client.get("/admin/add-doctor/")
        self.assertTemplateUsed(response2, "adminApp/add_doctor.html")
        self.assertTrue(response1.status_code == 200)

    def test_add_doctors(self):
        email = "morton.jon68@gmail.com"
        data = {
            "firstname": "Jon",
            "lastname": "Morton",
            "phone": "7886451236",
            "gender": "Male",
        }
        credential = {
            "username": email[:str(email).rindex("@")],
            "password": "password",
        }

        User.objects.create_user(**credential)
        doctor = DoctorInfo(userid=User.objects.get_by_natural_key(credential["username"]), **data)
        doctor.save()
        self.assertTrue(User.objects.get_by_natural_key(username=credential["username"]))
        self.assertTrue(DoctorInfo.objects.get(userid=User.objects.get_by_natural_key(credential["username"])))
