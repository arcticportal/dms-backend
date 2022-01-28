from django.contrib.gis import forms


class RawAdminForm(forms.ModelForm):
    geometry = forms.MultiPolygonField(
        widget=forms.OpenLayersWidget(
            attrs={
                "display_raw": True,
                # "supports_3d": True,
                "map_width": 900,
                "map_height": 500,
            }
        )
    )
