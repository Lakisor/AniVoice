from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.contrib.auth.models import User
from django.db import IntegrityError


class Anime(models.Model):
    title = models.CharField(max_length=350)
    pic_title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Tournament(models.Model):
    count_of_animes = models.IntegerField(default=16) # degree of 2 (>16)
    votes = models.IntegerField(default=0)
    name = models.CharField(max_length=150)
    author = models.ForeignKey(User, related_name="user_tour", on_delete=models.CASCADE)
    animes = models.ManyToManyField(Anime)
    def upvote(self, User):
        try:
            self.votes += 1
            self.save()
        except IntegrityError:
            return 'double_voting'
        return 'ok'

    def downvote(self, User):
        try:
            self.votes -= 1
            self.save()
        except IntegrityError:
            return 'double_voting'
        return 'ok'

    def __str__(self):
        return self.name
    
class UserVotes(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    tour = models.ForeignKey(Tournament, on_delete=CASCADE, related_name="post_votes")
    vote_type = models.CharField(max_length=50)

    class Meta:
        unique_together = ('user', 'tour', 'vote_type')

    def __str__(self):
        return str(self.user)+ ' - ' + str(self.tour)