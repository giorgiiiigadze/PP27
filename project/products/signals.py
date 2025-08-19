# pre-save - 
# post-save - 
from .models import Product, ProductLog
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender = Product)
def log_product_creation(sender, instance, created, **kwargs):
    if created:
        ProductLog.objects.create(
            product = instance,
            message = f'product {instance.name} was created '
        )

