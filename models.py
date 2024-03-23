from django.db import models


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255)
    location_description = models.TextField()

    def __str__(self):
        return self.location_name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name


class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    asset_tag = models.CharField(max_length=255)
    equipment_name = models.CharField(max_length=255)
    equipment_description = models.TextField()
    equipment_type = models.CharField(max_length=255)
    equipment_availability = models.BooleanField(default=True)
    return_date = models.DateField(null=True, blank=True)
    equipment_status = models.CharField(max_length=255)

    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='equipment')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='equipment')

    def __str__(self):
        return self.equipment_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=255)
    user_role = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reservation_status = models.CharField(max_length=255)


class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alert_date = models.DateTimeField()
    alert_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
