from django import forms


class PlayerRequest(forms.Forms):
    playerName = forms.CharField(label='Enter a Player Name')
