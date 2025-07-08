# from django.db import models
# from django.core.validators import URLValidator
# import re
# from django.core.exceptions import ValidationError # Import specifically for clean method

# class ProjectSpec(models.Model):
#     project_name = models.CharField(max_length=200)
#     description = models.TextField()
#     json_data = models.JSONField() # This stores the complex JSON structure
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"{self.project_name} - {self.created_at.strftime('%Y-%m-%d')}"

#     def clean(self):
#         """
#         Custom model-level validation for the ProjectSpec instance.
        
#         Note: With Django REST Framework serializers, much of this validation
#         is handled *before* the model's clean method is called (during serializer.is_valid()).
#         However, this `clean` method provides a safeguard for direct model saves
#         (e.g., from Django Admin, shell scripts, or other parts of your Django app
#         that don't go through the DRF serializers).
#         """
#         # Validate HEX colors if present in json_data
#         if self.json_data:
#             theme = self.json_data.get('theme', {})
#             primary_color = theme.get('primaryColor', '')
#             secondary_color = theme.get('secondaryColor', '')
            
#             hex_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
            
#             if primary_color and not hex_pattern.match(primary_color):
#                 raise ValidationError({'json_data': 'Primary color in theme must be a valid HEX color.'})
            
#             if secondary_color and not hex_pattern.match(secondary_color):
#                 raise ValidationError({'json_data': 'Secondary color in theme must be a valid HEX color.'})
            
#             # Validate URLs within json_data
#             urls_to_validate = []

#             # Assets URLs
#             assets = self.json_data.get('assets', {})
#             if assets.get('logoUrl'):
#                 urls_to_validate.append(assets['logoUrl'])
#             if assets.get('faviconUrl'):
#                 urls_to_validate.append(assets['faviconUrl'])
            
#             # Meta siteUrl
#             meta = self.json_data.get('meta', {})
#             if meta.get('siteUrl'):
#                 urls_to_validate.append(meta['siteUrl'])

#             # Add more URLs from json_data if needed (e.g., from sections, social links, etc.)
#             # This would require more extensive parsing of the json_data structure.
#             # Example (if you want to add from SEO openGraph):
#             seo = self.json_data.get('seo', {})
#             if seo.get('openGraph', {}).get('image'):
#                 urls_to_validate.append(seo['openGraph']['image'])
#             if seo.get('openGraph', {}).get('url'):
#                 urls_to_validate.append(seo['openGraph']['url'])
#             if seo.get('twitterCard', {}).get('image'):
#                 urls_to_validate.append(seo['twitterCard']['image'])


#             url_validator = URLValidator()
#             for url in urls_to_validate:
#                 if url: # Only validate if the URL string is not empty
#                     try:
#                         url_validator(url)
#                     except Exception: # Catch any validation error from URLValidator
#                         # Provide a more specific error message if possible
#                         raise ValidationError({'json_data': f'Invalid URL found in JSON data: {url}'})

#         # Important: Call the super method to ensure any parent class clean logic runs
#         super().clean()







# from django.db import models
# from django.core.validators import URLValidator
# import re

# class ProjectSpec(models.Model):
#     project_name = models.CharField(max_length=200)
#     description = models.TextField()
#     json_data = models.JSONField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"{self.project_name} - {self.created_at.strftime('%Y-%m-%d')}"

#     def clean(self):
#         from django.core.exceptions import ValidationError
        
#         # Validate HEX colors if present
#         if self.json_data:
#             theme = self.json_data.get('theme', {})
#             primary_color = theme.get('primaryColor', '')
#             secondary_color = theme.get('secondaryColor', '')
            
#             hex_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
            
#             if primary_color and not hex_pattern.match(primary_color):
#                 raise ValidationError('Primary color must be a valid HEX color')
            
#             if secondary_color and not hex_pattern.match(secondary_color):
#                 raise ValidationError('Secondary color must be a valid HEX color')
            
#             # Validate URLs
#             assets = self.json_data.get('assets', {})
#             urls_to_validate = [
#                 assets.get('logoUrl', ''),
#                 assets.get('faviconUrl', ''),
#                 self.json_data.get('meta', {}).get('siteUrl', ''),
#             ]
            
#             url_validator = URLValidator()
#             for url in urls_to_validate:
#                 if url:
#                     try:
#                         url_validator(url)
#                     except:
#                         raise ValidationError(f'Invalid URL: {url}')

from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import re

class ProjectSpec(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    json_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.project_name} - {self.created_at.strftime('%Y-%m-%d')}"

    def clean(self):
        # Validate HEX colors if present within the 'theme' object
        if self.json_data:
            theme = self.json_data.get('theme', {})
            primary_color = theme.get('primaryColor', '')
            secondary_color = theme.get('secondaryColor', '')
            
            hex_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
            
            if primary_color and not hex_pattern.match(primary_color):
                raise ValidationError({'theme': {'primaryColor': 'Primary color must be a valid HEX color'}})
            
            if secondary_color and not hex_pattern.match(secondary_color):
                raise ValidationError({'theme': {'secondaryColor': 'Secondary color must be a valid HEX color'}})
            
            # Validate URLs
            urls_to_validate = []

            # Top-level siteUrl
            site_url = self.json_data.get('siteUrl', '')
            if site_url:
                urls_to_validate.append(('siteUrl', site_url))

            # Assets URLs
            logo_url = self.json_data.get('logoUrl', '')
            if logo_url:
                urls_to_validate.append(('logoUrl', logo_url))

            favicon_url = self.json_data.get('faviconUrl', '')
            if favicon_url:
                urls_to_validate.append(('faviconUrl', favicon_url))
            
            # OpenGraph Image URL
            og_image_url = self.json_data.get('openGraphTags', {}).get('ogImageUrl', '')
            if og_image_url:
                urls_to_validate.append(('openGraphTags.ogImageUrl', og_image_url))

            # OpenGraph URL
            og_url = self.json_data.get('openGraphTags', {}).get('ogUrl', '')
            if og_url:
                urls_to_validate.append(('openGraphTags.ogUrl', og_url))

            # Twitter Image URL
            twitter_image_url = self.json_data.get('twitterCardTags', {}).get('image', '')
            if twitter_image_url:
                urls_to_validate.append(('twitterCardTags.image', twitter_image_url))


            url_validator = URLValidator()
            for field_path, url in urls_to_validate:
                try:
                    url_validator(url)
                except ValidationError:
                    raise ValidationError({field_path: f'Invalid URL: {url}'})