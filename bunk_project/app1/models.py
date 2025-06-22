from django.db import models

# Create your models here.
class BunkEntry(models.Model):
    totalDays = models.IntegerField()
    totalAttendanceNeeded = models.IntegerField()
    presentAttendance = models.IntegerField()
    daysGone = models.IntegerField()
    resultMessage = models.TextField(blank=True, null=True)  # Optional: store result

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"Bunk Entry ({self.created_at.strftime('%Y-%m-%d %H:%M')})"