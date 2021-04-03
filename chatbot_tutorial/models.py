from django.db import models
from django.contrib.auth.models import User
from chatbot_tutorial._threading_local import local

def set_current_user(user):
    _thread_locals.user = user


def get_current_user():
    return getattr(_thread_locals, 'user', None)


class DateTimeBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.CharField(max_length=100, default="", editable=False)
    updated_by = models.CharField(max_length=100, default="", editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        try:
            if get_current_user():
                if self.created_by == "":
                    self.created_by = get_current_user().username
                self.updated_by = get_current_user().username
        except Exception as e:
            print("error")
        super(DateTimeBase, self).save(*args, **kwargs)

class AllCalls(DateTimeBase):

    user = models.ForeignKey(User, null=True, blank=True)
    entered_val = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return u'%s'  %(self.entered_val)

class GetUser(DateTimeBase):
    
    user = models.ForeignKey(User, null=True, blank=True, default=None)
    date = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return u'%s'  %(self.user)


