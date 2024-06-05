from django.db import models

class Complaint(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accept'
    REJECTED = 'reject'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]
    name = models.CharField(max_length=50)
    complaint_type = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)


class UserRegistration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
