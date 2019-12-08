from rest_framework import serializers

from .models import WinUpdate
from agents.models import Agent

class WinUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WinUpdate
        fields = "__all__"

class UpdateSerializer(serializers.ModelSerializer):
    winupdates = WinUpdateSerializer(many=True, read_only=True)

    class Meta:
        model = Agent
        fields = (
            "pk",
            "hostname",
            "winupdates",
        )

class ApprovedUpdateSerializer(serializers.ModelSerializer):
    winupdates = WinUpdateSerializer(read_only=True)
    agentid = serializers.ReadOnlyField(source='agent.pk')

    class Meta:
        model = WinUpdate
        fields = ("id", "kb", "guid", "agentid", "winupdates",)