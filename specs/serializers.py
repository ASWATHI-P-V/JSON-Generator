from rest_framework import serializers
from .models import ProjectSpec
import re
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError as DjangoValidationError

class ProjectSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSpec
        fields = ['id', 'project_name', 'description', 'json_data', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_json_data(self, value):
        """Validate the JSON data structure"""
        errors = []
        
        # Check required top-level fields
        required_fields = ['project', 'technology', 'assets', 'theme', 'meta', 'seo', 'pages', 'globalModules']
        for field in required_fields:
            if field not in value:
                errors.append(f'Missing required field: {field}')
        
        # Validate HEX colors
        if 'theme' in value:
            theme = value['theme']
            hex_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
            
            for color_field in ['primaryColor', 'secondaryColor']:
                if color_field in theme and theme[color_field]:
                    if not hex_pattern.match(theme[color_field]):
                        errors.append(f'Invalid HEX color for {color_field}: {theme[color_field]}')
        
        # Validate URLs
        url_validator = URLValidator()
        urls_to_check = []
        
        if 'assets' in value:
            assets = value['assets']
            for url_field in ['logoUrl', 'faviconUrl']:
                if url_field in assets and assets[url_field]:
                    urls_to_check.append((url_field, assets[url_field]))
        
        if 'meta' in value and 'siteUrl' in value['meta'] and value['meta']['siteUrl']:
            urls_to_check.append(('siteUrl', value['meta']['siteUrl']))
        
        for field_name, url in urls_to_check:
            try:
                url_validator(url)
            except DjangoValidationError:
                errors.append(f'Invalid URL for {field_name}: {url}')
        
        if errors:
            raise serializers.ValidationError(errors)
        
        return value

class ProjectSpecCreateSerializer(serializers.Serializer):
    """Serializer for creating project specs from form data"""
    
    # Project Info
    project_name = serializers.CharField(max_length=200)
    description = serializers.CharField()
    
    # Technology Stack
    frontend_frameworks = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    backend_frameworks = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    database = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    hosting_provider = serializers.CharField(required=False, default='')
    
    # Assets
    logo_url = serializers.URLField(required=False, default='')
    favicon_url = serializers.URLField(required=False, default='')
    
    # Theme
    primary_color = serializers.RegexField(
        regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
        required=False,
        default='#000000'
    )
    secondary_color = serializers.RegexField(
        regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
        required=False,
        default='#ffffff'
    )
    font_family = serializers.CharField(required=False, default='Arial, sans-serif')
    style_description = serializers.CharField(required=False, default='')
    
    # Meta/SEO
    site_url = serializers.URLField(required=False, default='')
    meta_title = serializers.CharField(required=False, default='')
    meta_description = serializers.CharField(required=False, default='')
    meta_keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    author = serializers.CharField(required=False, default='')
    language = serializers.CharField(required=False, default='en')
    charset = serializers.CharField(required=False, default='UTF-8')
    viewport = serializers.CharField(required=False, default='width=device-width, initial-scale=1.0')
    robots = serializers.CharField(required=False, default='index, follow')
    
    # OpenGraph
    og_title = serializers.CharField(required=False, default='')
    og_description = serializers.CharField(required=False, default='')
    og_image_url = serializers.URLField(required=False, default='')
    og_url = serializers.URLField(required=False, default='')
    og_type = serializers.CharField(required=False, default='website')
    
    # Twitter Card
    twitter_card_type = serializers.CharField(required=False, default='summary')
    twitter_site = serializers.CharField(required=False, default='')
    twitter_title = serializers.CharField(required=False, default='')
    twitter_description = serializers.CharField(required=False, default='')
    twitter_image = serializers.URLField(required=False, default='')
    
    # SEO Section
    site_title = serializers.CharField(required=False, default='')
    site_description = serializers.CharField(required=False, default='')
    seo_keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    meta_content = serializers.CharField(required=False, default='')
    seo_meta_keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    
    # Pages (simplified - can be extended)
    pages = serializers.ListField(required=False, default=list)
    
    # Global Modules
    header_logo = serializers.CharField(required=False, default='')
    navigation_links = serializers.ListField(required=False, default=list)
    cta_button = serializers.CharField(required=False, default='')
    footer_columns = serializers.ListField(required=False, default=list)
    social_links = serializers.ListField(required=False, default=list)
    copyright_text = serializers.CharField(required=False, default='')

    def create(self, validated_data):
        """Convert form data to JSON spec and create ProjectSpec"""
        json_data = self._build_json_structure(validated_data)
        
        project_spec = ProjectSpec.objects.create(
            project_name=validated_data['project_name'],
            description=validated_data['description'],
            json_data=json_data
        )
        
        return project_spec

    def _build_json_structure(self, data):
        """Build the JSON structure from form data"""
        return {
            "project": {
                "name": data['project_name'],
                "description": data['description']
            },
            "technology": {
                "frontend": data['frontend_frameworks'],
                "backend": data['backend_frameworks'],
                "database": data['database'],
                "hosting": data['hosting_provider']
            },
            "assets": {
                "logoUrl": data['logo_url'],
                "faviconUrl": data['favicon_url']
            },
            "theme": {
                "primaryColor": data['primary_color'],
                "secondaryColor": data['secondary_color'],
                "fontFamily": data['font_family'],
                "styleDescription": data['style_description']
            },
            "meta": {
                "siteUrl": data['site_url'],
                "title": data['meta_title'],
                "description": data['meta_description'],
                "keywords": data['meta_keywords'],
                "author": data['author'],
                "language": data['language'],
                "charset": data['charset'],
                "viewport": data['viewport'],
                "robots": data['robots'],
                "openGraph": {
                    "title": data['og_title'],
                    "description": data['og_description'],
                    "image": data['og_image_url'],
                    "url": data['og_url'],
                    "type": data['og_type']
                },
                "twitterCard": {
                    "card": data['twitter_card_type'],
                    "site": data['twitter_site'],
                    "title": data['twitter_title'],
                    "description": data['twitter_description'],
                    "image": data['twitter_image']
                }
            },
            "seo": {
                "siteTitle": data['site_title'],
                "siteDescription": data['site_description'],
                "keywords": data['seo_keywords'],
                "metaContent": data['meta_content'],
                "metaKeywords": data['seo_meta_keywords'],
                "metaTags": []
            },
            "pages": data['pages'],
            "globalModules": {
                "header": {
                    "logo": data['header_logo'],
                    "navigationLinks": data['navigation_links'],
                    "ctaButton": data['cta_button']
                },
                "footer": {
                    "columns": data['footer_columns'],
                    "socialLinks": data['social_links'],
                    "copyrightText": data['copyright_text']
                }
            }
        }
