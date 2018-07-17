from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from toys.models import Toy
from toys.serializers import ToySerializer

toy_release_date = timezone.make_aware(
    datetime.now(), timezone.get_current_timezone())
toy1 = Toy(name='Snoopy talking action figure', description='Snoopy speaks five languages',
           release_date=toy_release_date, toy_category='Action figures', was_included_in_home=False)
toy1.save()
toy2 = Toy(name='Hawaiian Barbie', description='Barbie loves Hawaii',
           release_date=toy_release_date, toy_category='Dolls', was_included_in_home=True)
toy2.save()
