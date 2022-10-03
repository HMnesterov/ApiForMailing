from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_post_date
from .models import Mailing


@receiver(signal=post_save, sender=Mailing)
def mailing_was_saved(sender, instance, created,  *args, **kwargs):
    text = instance.message_id.text
    if created:

        for user in instance.message_id.client_id.all():

            send_post_date.apply_async([text, user.pk, instance.pk])