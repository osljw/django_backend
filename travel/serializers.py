from rest_framework import serializers
from .models import Travel

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = [
            'id',
            'title',
            'cover_image',
            'description',
            'cities',
            'duration',
            'start_date',
            'end_date'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the 'id' field optional for creating a new leaderboard
        if 'request' in self.context and self.context['request'].method == 'POST':
            self.fields['id'].required = False