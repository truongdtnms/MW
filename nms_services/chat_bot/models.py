from django.db import models
import datetime
class Events(models.Model):
    sender_id = models.CharField(max_length=255)
    type_name = models.CharField(max_length=255)
    timestamp = models.FloatField(blank=True, null=True)
    intent_name = models.CharField(max_length=255, blank=True, null=True)
    action_name = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.sender_id

    def getTimeStamp(self):
        return datetime.datetime.fromtimestamp(self.timestamp)
        # pass



    class Meta:
        managed = False
        db_table = 'events'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

class Textuser(models.Model):
    text_user = models.CharField(primary_key=True, max_length=1000)
    timestamp = models.FloatField(blank=True, null=True)
    entity = models.CharField(max_length=10000, blank=True, null=True)
    intent = models.CharField(max_length=10000, blank=True, null=True)

    def intent_dict(self):
        import json
        return json.loads(self.intent)
    class Meta:
        managed = False
        db_table = 'TextUser'

class Intent(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __init__(self, name):
        self.name = name
    class Meta:
        managed = False
        db_table = 'intent'

class Nlu(models.Model):
    intent_name = models.ForeignKey(Intent, on_delete=models.CASCADE)
    example = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'nlu'