from rest_framework import serializers

from soccer.models import Club, Player, Country


class CountrySerializer (serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class PlayerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'year_of_birth', 'scorrer_points']


class ClubSerializer (serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name','founding_date','points','active','country','players']


