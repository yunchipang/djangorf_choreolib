from django.db import models

STYLE_CHOICES = (
    ("hip-hop", "Hip-Hop"),
    ("locking", "Locking"),
    ("popping", "Popping"),
    ("house", "House"),
    ("breaking", "Breaking"),
    ("jazz", "Jazz"),
    ("afro", "Afro"),
    ("dancehall", "Dancehall"),
    ("heels", "Heels"),
    ("comtemporary", "Comtemporary")
)

class Choreography(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    choreographer = models.CharField(max_length=30)
    music_title = models.CharField(max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, max_length=30)
    video_url = models.URLField()

    class Meta:
        ordering = ["created"]