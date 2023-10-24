from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class TimeUserModel(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        db_index=True
        )
    
    class Meta:
        abstract = True
        ordering = ["created_at"]


class Post(TimeUserModel):
    title = models.CharField(_("title"), max_length=200)
    body = models.TextField(_("body"), max_length=5000)
    
    def __str__(self) -> str:
        return f"{self.title}"


class Comment(TimeUserModel):
    post = models.ForeignKey(
        Post,
        verbose_name=_("post"), 
        on_delete=models.CASCADE,
        related_name="comments",
    )
    body = models.TextField(_("body"), max_length=2500)

    def __str__(self) -> str:
        return f"{self.post} {_('by')} {self.user}"


class PostLike(TimeUserModel):
    post = models.ForeignKey(
        Post,
        verbose_name=_("post"), 
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self) -> str:
        return f"{self.post} {_('liked by')} {self.user}"


class CommentLike(TimeUserModel):
    comment = models.ForeignKey(
        Comment,
        verbose_name=_("comment"),
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self) -> str:
        return f"{self.comment} {_('liked by')} {self.user}"
