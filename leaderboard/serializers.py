from rest_framework import serializers
from .models import Leaderboard

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ('id', 'username', 'score', 'created_at')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the 'id' field optional for creating a new leaderboard
        if 'request' in self.context and self.context['request'].method == 'POST':
            self.fields['id'].required = False