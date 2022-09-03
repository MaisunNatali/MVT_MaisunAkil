from django import forms

class FamiliarFormulario(forms.Form):

    nombre=forms.CharField(max_length=50)
    fecha_nacimiento=forms.DateField()
    altura=forms.IntegerField()