from django.contrib.gis import forms


class RawAdminForm(forms.ModelForm):
    mpoly = forms.MultiPolygonField(
        widget=forms.OpenLayersWidget(
            attrs={
                "display_raw": True,
                # "supports_3d": True,
                "map_width": 1200,
                "map_height": 700,
            }
        )
    )
