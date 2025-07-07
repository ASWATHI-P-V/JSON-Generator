from django.db import models
from django.core.validators import URLValidator
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
        from django.core.exceptions import ValidationError
        
        # Validate HEX colors if present
        if self.json_data:
            theme = self.json_data.get('theme', {})
            primary_color = theme.get('primaryColor', '')
            secondary_color = theme.get('secondaryColor', '')
            
            hex_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
            
            if primary_color and not hex_pattern.match(primary_color):
                raise ValidationError('Primary color must be a valid HEX color')
            
            if secondary_color and not hex_pattern.match(secondary_color):
                raise ValidationError('Secondary color must be a valid HEX color')
            
            # Validate URLs
            assets = self.json_data.get('assets', {})
            urls_to_validate = [
                assets.get('logoUrl', ''),
                assets.get('faviconUrl', ''),
                self.json_data.get('meta', {}).get('siteUrl', ''),
            ]
            
            url_validator = URLValidator()
            for url in urls_to_validate:
                if url:
                    try:
                        url_validator(url)
                    except:
                        raise ValidationError(f'Invalid URL: {url}')
