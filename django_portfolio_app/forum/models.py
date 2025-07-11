from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']  # Newest posts first

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    def clean(self):
        from django.core.exceptions import ValidationError
        # Check if parent comment exists and belongs to a different post
        if self.parent and self.parent.post != self.post:
            raise ValidationError("Parent comment must belong to the same post")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created_at']

class ReactionType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='reaction_icons/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Reaction Type'
        verbose_name_plural = 'Reaction Types'

class Reaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reactions')
    reaction_type = models.ForeignKey(ReactionType, on_delete=models.CASCADE, related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions', null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reactions', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'post'],
                condition=models.Q(comment__isnull=True),
                name='unique_post_reaction_per_user'
            ),
            models.UniqueConstraint(
                fields=['user', 'comment'],
                condition=models.Q(post__isnull=True),
                name='unique_comment_reaction_per_comment'
            ),
        ]

    def __str__(self):
        if self.post:
            return f"{self.user.username} reacted to post {self.post.title} with {self.reaction_type.name}"
        elif self.comment:
            return f"{self.user.username} reacted to comment on post {self.comment.post.title} with {self.reaction_type.name}"
        return f"{self.user.username} reacted with {self.reaction_type.name}"