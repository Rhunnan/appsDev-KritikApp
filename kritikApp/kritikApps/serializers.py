from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('custom_id','name',)


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Establishment
        fields = ('custom_id','path_image','name','location','category','description','address','ai_script')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ('custom_id','review_comment','star_rating','image_path', 'user', 'establishment')