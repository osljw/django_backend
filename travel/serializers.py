from rest_framework import serializers
from .models import Travel, Order, Person


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

# class TravelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Travel
#         fields = [
#             'id',
#             'title',
#             'cover_image',
#             'description',
#             'cities',
#             'duration_days',
#             'start_date',
#             'end_date'
#         ]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Make the 'id' field optional for creating a new leaderboard
#         if 'request' in self.context and self.context['request'].method == 'POST':
#             self.fields['id'].required = False

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    persons = PersonSerializer(many=True, read_only=True)
    travel = TravelSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'