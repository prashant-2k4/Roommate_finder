from django.db import models
from django.conf import settings

class Room(models.Model):
    ROOM_CATEGORIES = [
        ("Single", "Single Room"),
        ("Double", "Double Room"),
        ("Shared", "Shared Room"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="room_images/", blank=True, null=True)  # Optional
    capacity = models.IntegerField(default=1)  # New field: Max occupants
    category = models.CharField(max_length=10, choices=ROOM_CATEGORIES, default="Single")  # Room type
    is_available = models.BooleanField(default=True)  # New field: Availability status
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.location} ({self.category})"
