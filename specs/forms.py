from django import forms
from .models import ProjectSpec

class ProjectSpecForm(forms.Form):
    # Project Info
    project_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    
    # Technology Stack
    frontend_frameworks = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'React, Vue, Angular (comma-separated)'}),
        help_text='Comma-separated list of frontend frameworks'
    )
    # backend_frameworks = forms.CharField(
    #     required=False,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Django, Express, Spring (comma-separated)'}),
    #     help_text='Comma-separated list of backend frameworks'
    # )
    # database = forms.CharField(
    #     required=False,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PostgreSQL, MySQL, MongoDB (comma-separated)'}),
    #     help_text='Comma-separated list of databases'
    # )
    # hosting_provider = forms.CharField(
    #     required=False,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AWS, Heroku, Vercel'})
    # )
    
    # Assets
    logo_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    favicon_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    
    # Theme
    primary_color = forms.RegexField(
        regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
        required=False,
        initial='#000000',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
        error_messages={'invalid': 'Enter a valid HEX color (e.g., #FF0000)'}
    )
    secondary_color = forms.RegexField(
        regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
        required=False,
        initial='#ffffff',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
        error_messages={'invalid': 'Enter a valid HEX color (e.g., #FF0000)'}
    )
    font_family = forms.CharField(
        required=False,
        initial='Arial, sans-serif',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    style_description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2})
    )
    
    # Meta/SEO
    site_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    meta_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    meta_description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    meta_keywords = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'keyword1, keyword2, keyword3'}),
        help_text='Comma-separated list of keywords'
    )
    author = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    language = forms.CharField(
        required=False,
        initial='en',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    charset = forms.CharField(
        required=False,
        initial='UTF-8',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    viewport = forms.CharField(
        required=False,
        initial='width=device-width, initial-scale=1.0',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    robots = forms.CharField(
        required=False,
        initial='index, follow',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    # OpenGraph
    og_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    og_description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    og_image_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    og_url = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    og_type = forms.CharField(
        required=False,
        initial='website',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    # Twitter Card
    twitter_card_type = forms.CharField(
        required=False,
        initial='summary',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    twitter_site = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    twitter_image = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    
    # SEO Section
    site_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    site_description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    seo_keywords = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'seo1, seo2, seo3'}),
        help_text='Comma-separated list of SEO keywords'
    )
    meta_content = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    seo_meta_keywords = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'meta1, meta2, meta3'}),
        help_text='Comma-separated list of meta keywords'
    )
    
    # Global Modules
    header_logo = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    navigation_links = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home, About, Services, Contact'}),
        help_text='Comma-separated list of navigation links'
    )
    cta_button = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    footer_columns = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Column 1, Column 2, Column 3'}),
        help_text='Comma-separated list of footer columns'
    )
    social_links = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebook, Twitter, Instagram'}),
        help_text='Comma-separated list of social links'
    )
    copyright_text = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_frontend_frameworks(self):
        data = self.cleaned_data['frontend_frameworks']
        return [item.strip() for item in data.split(',') if item.strip()] if data else []

    def clean_backend_frameworks(self):
        data = self.cleaned_data['backend_frameworks']
        return [item.strip() for item in data.split(',') if item.strip()] if data else []

    def clean_database(self):
        data = self.cleaned_data['database']
        return [item.strip() for item in data.split(',') if item.strip()] if data else []

    def clean_meta_keywords(self):
        data = self.cleaned_data['meta_keywords']
        return [item.strip() for item in data.split(',') if item.strip()] if data else []

    def clean_seo_keywords(self):
        data = self.cleaned_data['seo_keywords']
        return [item.strip() for item in data.split(',') if item.strip()] if data else []

    def clean_seo_meta_keywords(self):
        data = self.cleaned_data['seo_meta_keywords']
        return [item.strip() for item in data.split(',') if item.strip()] if data else []

    def clean_navigation_links(self):
        data = self.cleaned_data['navigation_links']
        return [item.strip() for item in data.split(',') if item.strip()] if data else []

    def clean_footer_columns(self):
        data = self.cleaned_data['footer_columns']
        return [item.strip() for item in data.split(',') if item.strip()] if data else []

    def clean_social_links(self):
        data = self.cleaned_data['social_links']
        return [item.strip() for item in data.split(',') if item.strip()] if data else []