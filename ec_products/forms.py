from django import forms
from .widgets import CustomClearableFileInput
from .models import EC_Product, EC_Category


class EC_ProductForm(forms.ModelForm):

    class Meta:
        model = EC_Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ec_categories = EC_Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in ec_categories]

        self.fields['ec_category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'