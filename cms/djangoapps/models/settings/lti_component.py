from django.db import models
from django.contrib.auth.models import User

class LTIComponent(models.Model):
    """
    Keeps track of key and secrets for LTI components
    """
    user = models.ForeignKey(User, db_index=True)
    course_id = models.TextField()
    module_id = models.TextField()
    key = models.TextField()
    secret = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, db_index=True)

    class Meta:
        db_table = 'courseware_lticomponent'

    def __unicode__(self):
        return "[LTIComponent] %s %s: %s = %s" % (self.course_id, self.module_id, self.key, self.secret)