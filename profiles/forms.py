# profiles/forms.py
from django import forms
from django_countries import countries
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ---- hard-materialise the country choices --------------------
        country_field = self.fields["default_country"]

        # build a regular (value, label) list – add the blank option first
        concrete_choices = (("", "---------"),) + tuple(countries)

        # assign it to both the field *and* its widget
        country_field.choices = concrete_choices
        country_field.widget.choices = concrete_choices
        # ----------------------------------------------------------------

        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
        }

        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for name, field in self.fields.items():
            if name != "default_country":
                ph = placeholders.get(name, "")
                if field.required:
                    ph += " *"
                field.widget.attrs["placeholder"] = ph
            field.widget.attrs["class"] = (
                "border-black rounded-0 profile-form-input"
            )
            field.label = False
