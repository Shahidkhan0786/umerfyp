from rest_framework import serializers
from .models import orders

class ordersSerializer(serializers.Serializer):
    # client = serializers.ForeignKey(MyProfile , on_delete=models.CASCADE)
    service = serializers.CharField(max_length=100 )
    package = serializers.CharField(max_length=200)
    run_time=serializers.CharField(max_length=100)
    finish_date = serializers.DateField()
    time= serializers.DateTimeField()
    status=serializers.CharField(max_length=200)
    user_name = serializers.ReadOnlyField()

    class Meta:
        model = orders