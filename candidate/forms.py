from django import forms
from candidate.models import CandidateProfiles


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfiles
        exclude = ("user",)
        widgets = {
            "profile_pic": forms.FileInput(attrs={
                "class": "form-control rounded-pill single-input"
            }),
            "resume": forms.FileInput(attrs={
                "class": "form-control rounded-pill single-input",
            }),
            "qualification": forms.TextInput(attrs={
                "class": "form-control rounded-pill single-input",
                "placeholder": "Qualification",
            }),
            "skills": forms.TextInput(attrs={
                "class": "form-control rounded-pill single-input",
                "placeholder": "Skills",
            }),
            "experience": forms.NumberInput(attrs={
                "class": "form-control rounded-pill single-input",
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        experience = cleaned_data.get("experience")
        if experience > 10:
            self.add_error(experience, error="Experience must be less than 10")
        return cleaned_data


class CandidateProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill single-input",
        "placeholder": "First Name",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill single-input",
        "placeholder": "Last Name",
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill single-input",
        "placeholder": "Phone number",
    }))

    class Meta:
        model = CandidateProfiles
        fields = [
            "first_name",
            "last_name",
            "phone",
            "profile_pic",
            "resume",
            "qualification",
            "skills",
            "experience"
        ]

        widgets = {
            "qualification": forms.TextInput(attrs={
                "class": "form-control rounded-pill single-input",
                "placeholder": "Phone number",
            }),
            "skills": forms.TextInput(attrs={
                "class": "form-control rounded-pill single-input",
                "placeholder": "Phone number",
            }),
            "experience": forms.NumberInput(attrs={
                "class": "form-control rounded-pill single-input",
                "placeholder": "Phone number",
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        experience_date = cleaned_data.get("experience")
        if experience_date > 10:
            self.add_error("experience", "Experience must be less than 10")
        return cleaned_data
