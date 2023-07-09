from django.db import models


# Create your models here.
class Post(models.Model):
    """
        Represents a blog post.

        :param title: The title of the blog post.
        :type title: str
        :param body: The content/body of the blog post.
        :type body: str
        :param signature: The author's signature for the blog post.
        :type signature: str
        :param date: The date and time when the blog post was published.
        :type date: datetime.datetime
        """
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Douglas Holder")
    date = models.DateTimeField()

    def __str__(self):
        """
                Returns a string representation of the blog post.

                :return: The title of the blog post.
                :rtype: str
                """
        return self.title

