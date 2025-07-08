# from rest_framework import serializers
# from .models import ProjectSpec
# import re
# from django.core.validators import URLValidator
# from django.core.exceptions import ValidationError as DjangoValidationError

# # --- Nested Serializers for Complex List Fields (Used in both Input and Output) ---

# # For Header Navigation Links
# class NavigationLinkSerializer(serializers.Serializer):
#     label = serializers.CharField(required=True, allow_blank=False) # Make required
#     link = serializers.CharField(required=True, allow_blank=False) # Or URLField if they are always full URLs

# # For Header CTA Button
# class CtaButtonSerializer(serializers.Serializer):
#     text = serializers.CharField(required=True, allow_blank=False)
#     link = serializers.CharField(required=True, allow_blank=False) # Or URLField

# # For Footer Columns
# class FooterColumnLinkSerializer(serializers.Serializer):
#     label = serializers.CharField(required=True, allow_blank=False)
#     link = serializers.CharField(required=True, allow_blank=False) # Or URLField

# class FooterColumnSerializer(serializers.Serializer):
#     title = serializers.CharField(required=True, allow_blank=False)
#     links = FooterColumnLinkSerializer(many=True, required=False, default=list)

# # For Footer Social Links
# class SocialLinkSerializer(serializers.Serializer):
#     platform = serializers.CharField(required=True, allow_blank=False)
#     url = serializers.URLField(required=True, allow_blank=False)

# # For Page Sections (Base) - This helps define common fields
# class BasePageSectionSerializer(serializers.Serializer):
#     type = serializers.CharField(required=True, allow_blank=False) # e.g., "Hero", "ServicesOverview"

# # Specific Page Section Serializers
# class HeroSectionSerializer(BasePageSectionSerializer):
#     headline = serializers.CharField(required=False, allow_blank=True)
#     subheadline = serializers.CharField(required=False, allow_blank=True)
#     ctaText = serializers.CharField(source='cta_text', required=False, allow_blank=True)
#     backgroundImage = serializers.URLField(source='background_image', required=False, allow_blank=True)

# class ServicesOverviewItemSerializer(serializers.Serializer):
#     title = serializers.CharField(required=False, allow_blank=True)
#     description = serializers.CharField(required=False, allow_blank=True)
#     icon = serializers.CharField(required=False, allow_blank=True)

# class ServicesOverviewSectionSerializer(BasePageSectionSerializer):
#     title = serializers.CharField(required=False, allow_blank=True)
#     items = ServicesOverviewItemSerializer(many=True, required=False, default=list)

# class TestimonialItemSerializer(serializers.Serializer):
#     name = serializers.CharField(required=False, allow_blank=True)
#     company = serializers.CharField(required=False, allow_blank=True)
#     quote = serializers.CharField(required=False, allow_blank=True)

# class TestimonialsSectionSerializer(BasePageSectionSerializer):
#     title = serializers.CharField(required=False, allow_blank=True)
#     testimonials = TestimonialItemSerializer(many=True, required=False, default=list)

# class CtaSectionSerializer(BasePageSectionSerializer):
#     text = serializers.CharField(required=False, allow_blank=True)
#     buttonText = serializers.CharField(source='button_text', required=False, allow_blank=True)
#     buttonLink = serializers.CharField(source='button_link', required=False, allow_blank=True)

# class TeamMemberSerializer(serializers.Serializer):
#     name = serializers.CharField(required=False, allow_blank=True)
#     role = serializers.CharField(required=False, allow_blank=True)
#     photo = serializers.CharField(required=False, allow_blank=True)
#     bio = serializers.CharField(required=False, allow_blank=True)

# class TeamIntroSectionSerializer(BasePageSectionSerializer):
#     title = serializers.CharField(required=False, allow_blank=True)
#     description = serializers.CharField(required=False, allow_blank=True)
#     teamMembers = TeamMemberSerializer(source='team_members', many=True, required=False, default=list)

# class MissionVisionSectionSerializer(BasePageSectionSerializer):
#     mission = serializers.CharField(required=False, allow_blank=True)
#     vision = serializers.CharField(required=False, allow_blank=True)

# class ServiceListItemSerializer(serializers.Serializer):
#     title = serializers.CharField(required=False, allow_blank=True)
#     description = serializers.CharField(required=False, allow_blank=True)
#     features = serializers.ListField(child=serializers.CharField(), required=False, default=list)

# class ServiceListSectionSerializer(BasePageSectionSerializer):
#     items = ServiceListItemSerializer(many=True, required=False, default=list)

# class ContactFormFieldSerializer(serializers.Serializer):
#     label = serializers.CharField(required=False, allow_blank=True)
#     type = serializers.CharField(required=False, allow_blank=True)
#     required = serializers.BooleanField(required=False, default=False)

# class ContactFormSectionSerializer(BasePageSectionSerializer):
#     title = serializers.CharField(required=False, allow_blank=True)
#     fields = ContactFormFieldSerializer(many=True, required=False, default=list)
#     submitButtonText = serializers.CharField(source='submit_button_text', required=False, allow_blank=True)

# class ContactInfoSectionSerializer(BasePageSectionSerializer):
#     address = serializers.CharField(required=False, allow_blank=True)
#     phone = serializers.CharField(required=False, allow_blank=True)
#     email = serializers.CharField(required=False, allow_blank=True)
#     mapEmbedUrl = serializers.URLField(source='map_embed_url', required=False, allow_blank=True)

# # Main Page Serializer (for output, reading from json_data)
# class PageSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     url = serializers.CharField()
#     sections = serializers.ListField(child=serializers.DictField(), required=False, default=list)


# # --- Output Serializer (ProjectSpecSerializer) ---
# class ProjectSpecSerializer(serializers.ModelSerializer):
#     projectName = serializers.CharField(source='json_data.project.name', read_only=True)
#     description = serializers.CharField(source='json_data.project.description', read_only=True)
#     theme = serializers.SerializerMethodField()
#     frontendFrameworks = serializers.ListField(source='json_data.technology.frontend', read_only=True)
#     # backendFrameworks = serializers.ListField(source='json_data.technology.backend', read_only=True)
#     # database = serializers.ListField(source='json_data.technology.database', read_only=True)
#     # hostingProvider = serializers.CharField(source='json_data.technology.hosting', read_only=True)
#     logoUrl = serializers.URLField(source='json_data.assets.logoUrl', read_only=True)
#     faviconUrl = serializers.URLField(source='json_data.assets.faviconUrl', read_only=True)
#     siteUrl = serializers.URLField(source='json_data.meta.siteUrl', read_only=True)
#     author = serializers.CharField(source='json_data.meta.author', read_only=True)
#     language = serializers.CharField(source='json_data.meta.language', read_only=True)
#     charset = serializers.CharField(source='json_data.meta.charset', read_only=True)
#     viewport = serializers.CharField(source='json_data.meta.viewport', read_only=True)
#     robots = serializers.CharField(source='json_data.meta.robots', read_only=True)
#     metaTitle = serializers.CharField(source='json_data.meta.title', read_only=True)
#     metaDescription = serializers.CharField(source='json_data.meta.description', read_only=True)
#     metaKeywords = serializers.ListField(source='json_data.meta.keywords', read_only=True)
#     seo = serializers.SerializerMethodField()
#     ogTitle = serializers.CharField(source='json_data.meta.openGraph.title', read_only=True)
#     ogDescription = serializers.CharField(source='json_data.meta.openGraph.description', read_only=True)
#     ogImageUrl = serializers.URLField(source='json_data.meta.openGraph.image', read_only=True)
#     ogUrl = serializers.URLField(source='json_data.meta.openGraph.url', read_only=True)
#     ogType = serializers.CharField(source='json_data.meta.openGraph.type', read_only=True)
#     twitterCardType = serializers.CharField(source='json_data.meta.twitterCard.card', read_only=True)
#     twitterSite = serializers.CharField(source='json_data.meta.twitterCard.site', read_only=True)
#     twitterTitle = serializers.CharField(source='json_data.meta.twitterCard.title', read_only=True)
#     twitterDescription = serializers.CharField(source='json_data.meta.twitterCard.description', read_only=True)
#     twitterImage = serializers.URLField(source='json_data.meta.twitterCard.image', read_only=True)
#     globalModules = serializers.SerializerMethodField()
#     pages = serializers.SerializerMethodField()

#     class Meta:
#         model = ProjectSpec
#         fields = [
#             'id', 'projectName', 'description', 'theme','frontendFrameworks',
#             # 'backendFrameworks', 'database', 'hostingProvider',
#             'logoUrl', 'faviconUrl',
#             'siteUrl', 'author', 'language', 'charset', 'viewport', 'robots',
#             'metaTitle', 'metaDescription', 'metaKeywords', 'seo',
#             'ogTitle', 'ogDescription', 'ogImageUrl', 'ogUrl', 'ogType',
#             'twitterCardType', 'twitterSite', 'twitterTitle', 'twitterDescription', 'twitterImage',
#             'globalModules', 'pages'
#         ]
#         read_only_fields = fields

#     def get_theme(self, obj):
#         theme_data = obj.json_data.get('theme', {})
#         return {
#             "primaryColor": theme_data.get('primaryColor', '#000000'),
#             "secondaryColor": theme_data.get('secondaryColor', '#ffffff'),
#             "fontFamily": theme_data.get('fontFamily', 'Arial, sans-serif'),
#             "style": theme_data.get('styleDescription', '') # Mapped 'styleDescription' to 'style'
#         }
    
#     def get_seo(self, obj):
#         seo_data = obj.json_data.get('seo', {})
#         return {
#             "siteTitle": seo_data.get('siteTitle', ''),
#             "siteDescription": seo_data.get('siteDescription', ''),
#             "keywords": seo_data.get('keywords', []),
#         }

#     def get_globalModules(self, obj):
#         # Initialize header_data and footer_data as empty dictionaries
#         # This is where the change happens: iterate through globalModules list
#         header_data = {}
#         footer_data = {}
        
#         # obj.json_data.get('globalModules', []) will safely return an empty list if not found
#         for module in obj.json_data.get('globalModules', []):
#             if module.get('type') == 'Header':
#                 header_data = module
#             elif module.get('type') == 'Footer':
#                 footer_data = module

#         global_modules_list = []

#         if header_data:
#             # Now header_data is the dictionary for the Header module
#             global_modules_list.append({
#                 "type": "Header",
#                 "logo": header_data.get('logo', ''),
#                 # Ensure navigationLinks itself is a list before passing to NavigationLinkSerializer
#                 "navigation": NavigationLinkSerializer(header_data.get('navigationLinks', []), many=True).data,
#                 "ctaButton": CtaButtonSerializer(header_data.get('ctaButton', {})).data
#             })
        
#         if footer_data:
#             # Now footer_data is the dictionary for the Footer module
#             global_modules_list.append({
#                 "type": "Footer",
#                 "columns": FooterColumnSerializer(footer_data.get('columns', []), many=True).data,
#                 "socialLinks": SocialLinkSerializer(footer_data.get('socialLinks', []), many=True).data,
#                 "copyright": footer_data.get('copyrightText', '') # 'copyrightText' in JSON data, output as 'copyright'
#             })
        
#         return global_modules_list

#     def get_pages(self, obj):
#         pages_data = obj.json_data.get('pages', [])
#         serialized_pages = []
#         for page in pages_data:
#             page_obj = {
#                 "name": page.get('name', ''),
#                 "url": page.get('url', ''),
#                 "sections": []
#             }
#             sections_data = page.get('sections', [])
#             for section in sections_data:
#                 section_type = section.get('type')
#                 if section_type == "Hero":
#                     page_obj['sections'].append(HeroSectionSerializer(section).data)
#                 elif section_type == "ServicesOverview":
#                     page_obj['sections'].append(ServicesOverviewSectionSerializer(section).data)
#                 elif section_type == "Testimonials":
#                     page_obj['sections'].append(TestimonialsSectionSerializer(section).data)
#                 elif section_type == "CTA":
#                     page_obj['sections'].append(CtaSectionSerializer(section).data)
#                 elif section_type == "TeamIntro":
#                     page_obj['sections'].append(TeamIntroSectionSerializer(section).data)
#                 elif section_type == "MissionVision":
#                     page_obj['sections'].append(MissionVisionSectionSerializer(section).data)
#                 elif section_type == "ServiceList":
#                     page_obj['sections'].append(ServiceListSectionSerializer(section).data)
#                 elif section_type == "ContactForm":
#                     page_obj['sections'].append(ContactFormSectionSerializer(section).data)
#                 elif section_type == "ContactInfo":
#                     page_obj['sections'].append(ContactInfoSectionSerializer(section).data)
#                 else:
#                     page_obj['sections'].append(section) 
#             serialized_pages.append(page_obj)
#         return serialized_pages


# # --- Input Serializer (ProjectSpecCreateSerializer) ---
# class ThemeInputSerializer(serializers.Serializer):
#     primaryColor = serializers.RegexField(source='primary_color', regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', required=False, allow_blank=True, default='#000000')
#     secondaryColor = serializers.RegexField(source='secondary_color', regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', required=False, allow_blank=True, default='#ffffff')
#     fontFamily = serializers.CharField(source='font_family', required=False, allow_blank=True, default='Arial, sans-serif')
#     style = serializers.CharField(required=False, allow_blank=True, default='')

# class SeoInputSerializer(serializers.Serializer):
#     siteTitle = serializers.CharField(source='site_title', required=False, allow_blank=True, default='')
#     siteDescription = serializers.CharField(source='site_description', required=False, allow_blank=True, default='')
#     keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)

# class OgInputSerializer(serializers.Serializer):
#     title = serializers.CharField(required=False, allow_blank=True, default='')
#     description = serializers.CharField(required=False, allow_blank=True, default='')
#     image = serializers.URLField(required=False, allow_blank=True, default='')
#     url = serializers.URLField(required=False, allow_blank=True, default='')
#     type = serializers.CharField(required=False, allow_blank=True, default='website')

# class TwitterCardInputSerializer(serializers.Serializer):
#     card = serializers.CharField(required=False, allow_blank=True, default='summary')
#     site = serializers.CharField(required=False, allow_blank=True, default='')
#     title = serializers.CharField(required=False, allow_blank=True, default='')
#     description = serializers.CharField(required=False, allow_blank=True, default='')
#     image = serializers.URLField(required=False, allow_blank=True, default='')

# # For Global Modules Input (Header/Footer structure) - These are defined at top
# class HeaderModuleInputSerializer(serializers.Serializer):
#     type = serializers.CharField(required=True, allow_blank=False)
#     logo = serializers.CharField(required=False, allow_blank=True, default='')
#     navigation = NavigationLinkSerializer(many=True, required=False, default=list)
#     ctaButton = CtaButtonSerializer(required=False, default={})

# class FooterModuleInputSerializer(serializers.Serializer):
#     type = serializers.CharField(required=True, allow_blank=False)
#     columns = FooterColumnSerializer(many=True, required=False, default=list)
#     socialLinks = SocialLinkSerializer(many=True, required=False, default=list)
#     copyright = serializers.CharField(required=False, allow_blank=True, default='')

# # For Pages Input - This now accepts a list where each item is a PageInputSerializer
# class PageInputSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, allow_blank=False)
#     url = serializers.CharField(required=True, allow_blank=False)
#     # This `sections` field is still a bit flexible for input;
#     # more rigorous validation could involve a polymorphic serializer
#     # or manual validation in `validate_pages` or `validate` method.
#     sections = serializers.ListField(child=serializers.DictField(), required=False, default=list)


# class ProjectSpecCreateSerializer(serializers.Serializer):
#     """Serializer for creating project specs directly from structured API input"""
#     id = serializers.IntegerField(read_only=True)  # Read-only field for ID
#     projectName = serializers.CharField(source='project_name', max_length=200, required=True, allow_blank=False)
#     description = serializers.CharField(required=False, allow_blank=True, default='')
    
#     theme = ThemeInputSerializer(required=True) # Theme object is required
    
#     frontendFrameworks = serializers.ListField(source='frontend_frameworks', child=serializers.CharField(), required=False, default=list)
#     # backendFrameworks = serializers.ListField(source='backend_frameworks', child=serializers.CharField(), required=False, default=list)
#     # database = serializers.ListField(child=serializers.CharField(), required=False, default=list)
#     # hostingProvider = serializers.CharField(source='hosting_provider', required=False, allow_blank=True, default='')
    
#     logoUrl = serializers.URLField(source='logo_url', required=False, allow_blank=True, default='')
#     faviconUrl = serializers.URLField(source='favicon_url', required=False, allow_blank=True, default='')
    
#     siteUrl = serializers.URLField(source='site_url', required=False, allow_blank=True, default='')
#     author = serializers.CharField(required=False, allow_blank=True, default='')
#     language = serializers.CharField(required=False, allow_blank=True, default='en')
#     charset = serializers.CharField(required=False, allow_blank=True, default='UTF-8')
#     viewport = serializers.CharField(required=False, allow_blank=True, default='width=device-width, initial-scale=1.0')
#     robots = serializers.CharField(required=False, allow_blank=True, default='index, follow')
    
#     metaTitle = serializers.CharField(source='meta_title', required=False, allow_blank=True, default='')
#     metaDescription = serializers.CharField(source='meta_description', required=False, allow_blank=True, default='')
#     metaKeywords = serializers.ListField(source='meta_keywords', child=serializers.CharField(), required=False, default=list)
    
#     ogTitle = serializers.CharField(source='og_title', required=False, allow_blank=True, default='')
#     ogDescription = serializers.CharField(source='og_description', required=False, allow_blank=True, default='')
#     ogImageUrl = serializers.URLField(source='og_image_url', required=False, allow_blank=True, default='')
#     ogUrl = serializers.URLField(source='og_url', required=False, allow_blank=True, default='')
#     ogType = serializers.CharField(source='og_type', required=False, allow_blank=True, default='website')
    
#     twitterCardType = serializers.CharField(source='twitter_card_type', required=False, allow_blank=True, default='summary')
#     twitterSite = serializers.CharField(source='twitter_site', required=False, allow_blank=True, default='')
#     twitterTitle = serializers.CharField(source='twitter_title', required=False, allow_blank=True, default='')
#     twitterDescription = serializers.CharField(source='twitter_description', required=False, allow_blank=True, default='')
#     twitterImage = serializers.URLField(source='twitter_image', required=False, allow_blank=True, default='')
    
#     siteTitle = serializers.CharField(source='seo_site_title', required=False, allow_blank=True, default='')
#     siteDescription = serializers.CharField(source='seo_site_description', required=False, allow_blank=True, default='')
#     seoKeywords = serializers.ListField(source='seo_keywords_flat', child=serializers.CharField(), required=False, default=list)
#     metaContent = serializers.CharField(source='meta_content', required=False, allow_blank=True, default='')
    
#     # Global Modules: Now explicitly accepts two types, Header and Footer.
#     # This list must contain dicts conforming to either HeaderModuleInputSerializer or FooterModuleInputSerializer.
#     # We use a custom validate method for this.
#     globalModules = serializers.ListField(child=serializers.DictField(), required=False, default=list)
    
#     pages = PageInputSerializer(many=True, required=False, default=list)

#     def create(self, validated_data):
#         json_data = self._build_json_structure(validated_data)
        
#         project_spec = ProjectSpec.objects.create(
#             project_name=validated_data['project_name'],
#             description=validated_data['description'],
#             json_data=json_data
#         )
#         return project_spec

#     def _build_json_structure(self, data):
#         def get_val(key, default=''):
#             return data.get(key, default)

#         # globalModules has already been validated and transformed by the validate method.
#         # So, we can directly use its structure as it is already a list of validated dicts.
#         processed_global_modules = []
#         for gm_item in get_val('globalModules', []):
#             if gm_item.get('type') == 'Header':
#                 # gm_item is already the validated dictionary.
#                 # 'navigation' will be present as a list of dicts.
#                 processed_global_modules.append({
#                     "type": "Header",
#                     "logo": gm_item.get('logo', ''),
#                     "navigationLinks": gm_item.get('navigation', []), # This is correct, 'navigation' is the key in validated_data
#                     "ctaButton": gm_item.get('ctaButton', {})
#                 })
#             elif gm_item.get('type') == 'Footer':
#                 # gm_item is already the validated dictionary.
#                 processed_global_modules.append({
#                     "type": "Footer",
#                     "columns": gm_item.get('columns', []),
#                     "socialLinks": gm_item.get('socialLinks', []),
#                     "copyrightText": gm_item.get('copyright', '')
#                 })
        
#         # Pages reconstruction
#         # Similar to globalModules, if PageInputSerializer handled complex nested sections,
#         # its validated_data would be the source. But here, PageInputSerializer is basic,
#         # and sections are raw DictFields in input, so it's fine as is.
#         processed_pages = PageInputSerializer(get_val('pages', []), many=True).data

#         return {
#             "projectName": get_val('project_name'),
#             "description": get_val('description'),
#             "theme": {
#                 "primaryColor": get_val('theme').get('primary_color', '#000000'),
#                 "secondaryColor": get_val('theme').get('secondary_color', '#ffffff'),
#                 "fontFamily": get_val('theme').get('font_family', 'Arial, sans-serif'),
#                 "style": get_val('theme').get('style', '')
#             },
#             "frontendFrameworks": get_val('frontend_frameworks', []),
#             # "backendFrameworks": get_val('backend_frameworks', []),
#             # "database": get_val('database', []),
#             # "hostingProvider": get_val('hosting_provider', ''),
#             "logoUrl": get_val('logo_url'),
#             "faviconUrl": get_val('favicon_url'),
#             "styleDescription": get_val('theme').get('style', ''), # Map 'style' from theme input to 'styleDescription' in JSON data

#             "siteUrl": get_val('site_url'),
#             "author": get_val('author'),
#             "language": get_val('language'),
#             "charset": get_val('charset'),
#             "viewport": get_val('viewport'),
#             "robots": get_val('robots'),
#             "metaTitle": get_val('meta_title'),
#             "metaDescription": get_val('meta_description'),
#             "metaKeywords": get_val('meta_keywords', []),
            
#             "ogTitle": get_val('og_title'),
#             "ogDescription": get_val('og_description'),
#             "ogImageUrl": get_val('og_image_url'),
#             "ogUrl": get_val('og_url'),
#             "ogType": get_val('og_type'),
            
#             "twitterCardType": get_val('twitter_card_type'),
#             "twitterSite": get_val('twitter_site'),
#             "twitterTitle": get_val('twitter_title'),
#             "twitterDescription": get_val('twitter_description'),
#             "twitterImage": get_val('twitter_image'),
            
#             "siteTitle": get_val('seo_site_title'),
#             "siteDescription": get_val('seo_site_description'),
#             "seoKeywords": get_val('seo_keywords_flat', []),
#             "metaContent": get_val('meta_content'),
            
#             "seo": {
#                 "siteTitle": get_val('seo_site_title'),
#                 "siteDescription": get_val('seo_site_description'),
#                 "keywords": get_val('seo_keywords_flat', []),
#             },
            
#             "globalModules": processed_global_modules,
#             "pages": processed_pages
#         }

#     def validate(self, data):
#         """
#         Custom validation to ensure top-level structure and enforce rules
#         that span across multiple fields or nested objects.
#         This mimics the logic from your original validate_json_data.
#         """
#         errors = {}

#         # 1. Check required top-level logical groups
#         # These are implicitly covered by `required=True` on the serializer fields,
#         # but can be explicitly checked if you want a specific error message format
#         # or to ensure the _presence_ of the object even if empty.
        
#         # DRF's default required=True will catch if 'theme' is completely missing.
#         # However, we can add a check for its internal structure if needed,
#         # but ThemeInputSerializer should handle its own fields.
        
#         # 2. Validate HEX colors (already handled by RegexField in ThemeInputSerializer)
#         # This check is now robustly handled by `ThemeInputSerializer` itself:
#         # primaryColor = serializers.RegexField(regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', ...)
#         # So, no need to re-validate here.

#         # 3. Validate URLs (already handled by URLField in respective serializers)
#         # These are automatically validated by `serializers.URLField` in:
#         # ProjectSpecCreateSerializer: logoUrl, faviconUrl, siteUrl, ogImageUrl, ogUrl, twitterImage
#         # SocialLinkSerializer: url
#         # No need to re-validate manually here.

#         # 4. Custom validation for 'globalModules' list content
#         # Ensure that each item in globalModules list is either a Header or a Footer
#         # and validate its internal structure.
#         if 'globalModules' in data and data['globalModules']:
#             validated_global_modules = []
#             gm_errors = []
#             for i, gm_item in enumerate(data['globalModules']):
#                 item_type = gm_item.get('type')
#                 if item_type == 'Header':
#                     serializer = HeaderModuleInputSerializer(data=gm_item)
#                 elif item_type == 'Footer':
#                     serializer = FooterModuleInputSerializer(data=gm_item)
#                 else:
#                     gm_errors.append(f"Item {i}: 'type' must be 'Header' or 'Footer'.")
#                     continue # Skip to next item

#                 if serializer.is_valid():
#                     validated_global_modules.append(serializer.validated_data)
#                 else:
#                     gm_errors.append({f"Item {i} ({item_type})": serializer.errors})
            
#             if gm_errors:
#                 errors['globalModules'] = gm_errors
#             else:
#                 # If all are valid, replace the original data with the validated, structured data
#                 # This ensures _build_json_structure receives properly validated objects.
#                 data['globalModules'] = validated_global_modules

#         # 5. Validate 'pages' list content more deeply if needed
#         # PageInputSerializer provides basic validation (name, url).
#         # If you need to ensure specific section types or content within sections,
#         # you'd add more logic here. For example, ensuring 'Home' page always has a 'Hero' section.
#         # This requires iterating through each page and its sections:
#         # if 'pages' in data and data['pages']:
#         #     page_errors = []
#         #     for i, page_data in enumerate(data['pages']):
#         #         # Example: Ensure each page has sections (if required)
#         #         if not page_data.get('sections'):
#         #             page_errors.append(f"Page '{page_data.get('name', i)}': must contain sections.")
#         #         # Further validation of sections could go here, similar to globalModules
#         #     if page_errors:
#         #         errors['pages'] = page_errors

#         if errors:
#             raise serializers.ValidationError(errors)
        
#         return data
















# from rest_framework import serializers
# from .models import ProjectSpec
# import re
# from django.core.validators import URLValidator
# from django.core.exceptions import ValidationError as DjangoValidationError

# class ProjectSpecSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectSpec
#         fields = ['id', 'project_name', 'description', 'json_data', 'created_at', 'updated_at']
#         read_only_fields = ['id', 'created_at', 'updated_at']

#     def validate_json_data(self, value):
#         """Validate the JSON data structure"""
#         errors = []
        
#         # Check required top-level fields
#         required_fields = ['project', 'technology', 'assets', 'theme', 'meta', 'seo', 'pages', 'globalModules']
#         for field in required_fields:
#             if field not in value:
#                 errors.append(f'Missing required field: {field}')
        
#         # Validate HEX colors
#         if 'theme' in value:
#             theme = value['theme']
#             hex_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
            
#             for color_field in ['primaryColor', 'secondaryColor']:
#                 if color_field in theme and theme[color_field]:
#                     if not hex_pattern.match(theme[color_field]):
#                         errors.append(f'Invalid HEX color for {color_field}: {theme[color_field]}')
        
#         # Validate URLs
#         url_validator = URLValidator()
#         urls_to_check = []
        
#         if 'assets' in value:
#             assets = value['assets']
#             for url_field in ['logoUrl', 'faviconUrl']:
#                 if url_field in assets and assets[url_field]:
#                     urls_to_check.append((url_field, assets[url_field]))
        
#         if 'meta' in value and 'siteUrl' in value['meta'] and value['meta']['siteUrl']:
#             urls_to_check.append(('siteUrl', value['meta']['siteUrl']))
        
#         for field_name, url in urls_to_check:
#             try:
#                 url_validator(url)
#             except DjangoValidationError:
#                 errors.append(f'Invalid URL for {field_name}: {url}')
        
#         if errors:
#             raise serializers.ValidationError(errors)
        
#         return value

# class ProjectSpecCreateSerializer(serializers.Serializer):
#     """Serializer for creating project specs from form data"""
    
#     # Project Info
#     project_name = serializers.CharField(max_length=200)
#     description = serializers.CharField()
    
#     # Technology Stack
#     frontend_frameworks = serializers.ListField(child=serializers.CharField(), required=False, default=list)
#     # backend_frameworks = serializers.ListField(child=serializers.CharField(), required=False, default=list)
#     # database = serializers.ListField(child=serializers.CharField(), required=False, default=list)
#     # hosting_provider = serializers.CharField(required=False, default='')
    
#     # Assets
#     logo_url = serializers.URLField(required=False, default='')
#     favicon_url = serializers.URLField(required=False, default='')
    
#     # Theme
#     primary_color = serializers.RegexField(
#         regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
#         required=False,
#         default='#000000'
#     )
#     secondary_color = serializers.RegexField(
#         regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
#         required=False,
#         default='#ffffff'
#     )
#     font_family = serializers.CharField(required=False, default='Arial, sans-serif')
#     style_description = serializers.CharField(required=False, default='')
    
#     # Meta/SEO
#     site_url = serializers.URLField(required=False, default='')
#     meta_title = serializers.CharField(required=False, default='')
#     meta_description = serializers.CharField(required=False, default='')
#     meta_keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
#     author = serializers.CharField(required=False, default='')
#     language = serializers.CharField(required=False, default='en')
#     charset = serializers.CharField(required=False, default='UTF-8')
#     viewport = serializers.CharField(required=False, default='width=device-width, initial-scale=1.0')
#     robots = serializers.CharField(required=False, default='index, follow')
    
#     # OpenGraph
#     og_title = serializers.CharField(required=False, default='')
#     og_description = serializers.CharField(required=False, default='')
#     og_image_url = serializers.URLField(required=False, default='')
#     og_url = serializers.URLField(required=False, default='')
#     og_type = serializers.CharField(required=False, default='website')
    
#     # Twitter Card
#     twitter_card_type = serializers.CharField(required=False, default='summary')
#     twitter_site = serializers.CharField(required=False, default='')
#     twitter_title = serializers.CharField(required=False, default='')
#     twitter_description = serializers.CharField(required=False, default='')
#     twitter_image = serializers.URLField(required=False, default='')
    
#     # SEO Section
#     site_title = serializers.CharField(required=False, default='')
#     site_description = serializers.CharField(required=False, default='')
#     seo_keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
#     meta_content = serializers.CharField(required=False, default='')
#     seo_meta_keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    
#     # Pages (simplified - can be extended)
#     pages = serializers.ListField(required=False, default=list)
    
#     # Global Modules
#     header_logo = serializers.CharField(required=False, default='')
#     navigation_links = serializers.ListField(required=False, default=list)
#     cta_button = serializers.CharField(required=False, default='')
#     footer_columns = serializers.ListField(required=False, default=list)
#     social_links = serializers.ListField(required=False, default=list)
#     copyright_text = serializers.CharField(required=False, default='')

#     def create(self, validated_data):
#         """Convert form data to JSON spec and create ProjectSpec"""
#         json_data = self._build_json_structure(validated_data)
        
#         project_spec = ProjectSpec.objects.create(
#             project_name=validated_data['project_name'],
#             description=validated_data['description'],
#             json_data=json_data
#         )
        
#         return project_spec

#     def _build_json_structure(self, data):
#         """Build the JSON structure from form data"""
#         return {
#             "project": {
#                 "name": data['project_name'],
#                 "description": data['description']
#             },
#             "technology": {
#                 "frontend": data['frontend_frameworks'],
#                 # "backend": data['backend_frameworks'],
#                 # "database": data['database'],
#                 # "hosting": data['hosting_provider']
#             },
#             "assets": {
#                 "logoUrl": data['logo_url'],
#                 "faviconUrl": data['favicon_url']
#             },
#             "theme": {
#                 "primaryColor": data['primary_color'],
#                 "secondaryColor": data['secondary_color'],
#                 "fontFamily": data['font_family'],
#                 "styleDescription": data['style_description']
#             },
#             "meta": {
#                 "siteUrl": data['site_url'],
#                 "title": data['meta_title'],
#                 "description": data['meta_description'],
#                 "keywords": data['meta_keywords'],
#                 "author": data['author'],
#                 "language": data['language'],
#                 "charset": data['charset'],
#                 "viewport": data['viewport'],
#                 "robots": data['robots'],
#                 "openGraph": {
#                     "title": data['og_title'],
#                     "description": data['og_description'],
#                     "image": data['og_image_url'],
#                     "url": data['og_url'],
#                     "type": data['og_type']
#                 },
#                 "twitterCard": {
#                     "card": data['twitter_card_type'],
#                     "site": data['twitter_site'],
#                     "title": data['twitter_title'],
#                     "description": data['twitter_description'],
#                     "image": data['twitter_image']
#                 }
#             },
#             "seo": {
#                 "siteTitle": data['site_title'],
#                 "siteDescription": data['site_description'],
#                 "keywords": data['seo_keywords'],
#                 "metaContent": data['meta_content'],
#                 "metaKeywords": data['seo_meta_keywords'],
#                 "metaTags": []
#             },
#             "pages": data['pages'],
#             "globalModules": {
#                 "header": {
#                     "logo": data['header_logo'],
#                     "navigationLinks": data['navigation_links'],
#                     "ctaButton": data['cta_button']
#                 },
#                 "footer": {
#                     "columns": data['footer_columns'],
#                     "socialLinks": data['social_links'],
#                     "copyrightText": data['copyright_text']
#                 }
#             }
#         }

# from rest_framework import serializers
# from .models import ProjectSpec
# import re
# from django.core.validators import URLValidator
# from django.core.exceptions import ValidationError as DjangoValidationError

# class ProjectSpecSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectSpec
#         fields = ['id', 'project_name', 'description', 'json_data', 'created_at', 'updated_at']
#         read_only_fields = ['id', 'created_at', 'updated_at']

#     def validate_json_data(self, value):
#         """Validate the JSON data structure according to the latest schema."""
#         errors = {} # Use a dictionary to store errors by field path for better context
        
#         # Define required top-level fields based on the latest JSON structure
#         required_top_level_fields = [
#             'projectName', 'description', 'frontendFrameworks', 'logoUrl',
#             'faviconUrl', 'theme', 'siteUrl', 'metaTitle', 'metaDescription',
#             'metaKeywords', 'author', 'language', 'charset', 'viewport', 'robots',
#             'openGraphTags', 'twitterCardTags', 'seo', 'pages', 'globalModules'
#         ]

#         for field in required_top_level_fields:
#             if field not in value:
#                 errors[field] = 'Missing required field.'

#         # Validate Theme colors
#         if 'theme' in value and isinstance(value['theme'], dict):
#             theme = value['theme']
#             hex_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
            
#             if 'primaryColor' in theme and theme['primaryColor']:
#                 if not hex_pattern.match(theme['primaryColor']):
#                     errors.setdefault('theme', {})['primaryColor'] = f'Invalid HEX color: {theme["primaryColor"]}'
#             else:
#                 errors.setdefault('theme', {})['primaryColor'] = 'Missing primaryColor in theme.'

#             if 'secondaryColor' in theme and theme['secondaryColor']:
#                 if not hex_pattern.match(theme['secondaryColor']):
#                     errors.setdefault('theme', {})['secondaryColor'] = f'Invalid HEX color: {theme["secondaryColor"]}'
#             else:
#                 errors.setdefault('theme', {})['secondaryColor'] = 'Missing secondaryColor in theme.'

#             if 'fontFamily' not in theme:
#                  errors.setdefault('theme', {})['fontFamily'] = 'Missing fontFamily in theme.'
#             if 'style' not in theme:
#                  errors.setdefault('theme', {})['style'] = 'Missing style in theme.'
#         else:
#             errors['theme'] = 'Missing or invalid theme object.'
        
#         # Validate URLs
#         url_validator = URLValidator()
#         urls_to_check = {
#             'siteUrl': value.get('siteUrl'),
#             'logoUrl': value.get('logoUrl'),
#             'faviconUrl': value.get('faviconUrl'),
#             'openGraphTags.ogImageUrl': value.get('openGraphTags', {}).get('ogImageUrl'),
#             'openGraphTags.ogUrl': value.get('openGraphTags', {}).get('ogUrl'),
#             'twitterCardTags.image': value.get('twitterCardTags', {}).get('image')
#         }
        
#         for field_path, url in urls_to_check.items():
#             if url: # Only validate if URL is provided
#                 try:
#                     url_validator(url)
#                 except DjangoValidationError:
#                     errors[field_path] = f'Invalid URL: {url}'
#             elif field_path in ['siteUrl', 'logoUrl', 'faviconUrl', 'openGraphTags.ogImageUrl', 'openGraphTags.ogUrl', 'twitterCardTags.image']:
#                  # Mark as missing if required and not present
#                  if field_path == 'siteUrl': # assuming siteUrl is required
#                      errors[field_path] = 'Missing required URL.'
#                  # Other URLs like logoUrl, faviconUrl etc. may be optional based on your SRS interpretation
#                  # but for now, they are marked as required if explicitly in urls_to_check and not found

#         # Validate Lists (e.g., frontendFrameworks, metaKeywords, seo.keywords, seo.metaKeywords)
#         list_fields = {
#             'frontendFrameworks': value.get('frontendFrameworks'),
#             'metaKeywords': value.get('metaKeywords'),
#             'seo.keywords': value.get('seo', {}).get('keywords'),
#             'seo.metaKeywords': value.get('seo', {}).get('metaKeywords'),
#             'pages': value.get('pages'),
#             'globalModules': value.get('globalModules')
#         }
#         for field_path, data_list in list_fields.items():
#             if data_list is not None and not isinstance(data_list, list):
#                 errors[field_path] = 'Must be a list.'
#             # Add more specific validation for list contents if needed (e.g., pages structure)

#         # Validate nested SEO metaTags structure
#         if 'seo' in value and isinstance(value['seo'], dict):
#             seo_data = value['seo']
#             if 'metaTags' in seo_data:
#                 if not isinstance(seo_data['metaTags'], list):
#                     errors.setdefault('seo', {})['metaTags'] = 'metaTags must be a list.'
#                 else:
#                     for i, tag in enumerate(seo_data['metaTags']):
#                         if not isinstance(tag, dict) or 'name' not in tag or 'content' not in tag:
#                             errors.setdefault('seo', {})['metaTags'] = errors.setdefault('seo', {}).get('metaTags', []) + \
#                                 [f'Item {i}: Each metaTag must be an object with "name" and "content" fields.']

#         if errors:
#             # Flatten errors dictionary for DRF's ValidationError or keep nested
#             # For simplicity, returning a flat list of error messages for now
#             flattened_errors = []
#             for field, err_msg in errors.items():
#                 if isinstance(err_msg, dict):
#                     for sub_field, sub_err_msg in err_msg.items():
#                         flattened_errors.append(f'{field}.{sub_field}: {sub_err_msg}')
#                 elif isinstance(err_msg, list): # For lists of errors like metaTags
#                      flattened_errors.extend([f'{field}: {msg}' for msg in err_msg])
#                 else:
#                     flattened_errors.append(f'{field}: {err_msg}')
#             raise serializers.ValidationError(flattened_errors)
        
#         return value

# class ThemeSerializer(serializers.Serializer):
#     primaryColor = serializers.RegexField(regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', required=True)
#     secondaryColor = serializers.RegexField(regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', required=True)
#     fontFamily = serializers.CharField(required=True)
#     style = serializers.CharField(required=True, source='style_description') # Map 'style' in JSON to 'style_description' in data

# class OpenGraphTagsSerializer(serializers.Serializer):
#     ogTitle = serializers.CharField(required=False, allow_blank=True)
#     ogDescription = serializers.CharField(required=False, allow_blank=True)
#     ogImageUrl = serializers.URLField(required=False, allow_blank=True)
#     ogUrl = serializers.URLField(required=False, allow_blank=True)
#     ogType = serializers.CharField(required=False, allow_blank=True)

# class ProjectSpecCreateSerializer(serializers.Serializer):
#     """
#     Serializer for creating project specs from flattened form data.
#     This serializer takes flat input and constructs the nested JSON structure.
#     """
    
#     # Project Info
#     project_name = serializers.CharField(max_length=200) # Maps to projectName
#     description = serializers.CharField()
    
#     # Technology Stack
#     frontend_frameworks = serializers.ListField(child=serializers.CharField(), required=True) # Changed to required=True as per SRS

#     # Assets
#     logo_url = serializers.URLField(required=True) # Changed to required=True as per SRS
#     favicon_url = serializers.URLField(required=True) # Changed to required=True as per SRS
    
#     # Theme
#     primary_color = serializers.RegexField(regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', required=True) # Changed to required=True
#     secondary_color = serializers.RegexField(regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', required=True) # Changed to required=True
#     font_family = serializers.CharField(required=True) # Changed to required=True
#     style_description = serializers.CharField(required=True) # Changed to required=True
    
#     # Meta/SEO
#     site_url = serializers.URLField(required=True) # Changed to required=True
#     meta_title = serializers.CharField(required=False, allow_blank=True)
#     meta_description = serializers.CharField(required=False, allow_blank=True)
#     meta_keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
#     author = serializers.CharField(required=False, allow_blank=True)
#     language = serializers.CharField(required=False, default='en', max_length=10)
#     charset = serializers.CharField(required=False, default='UTF-8', max_length=20)
#     viewport = serializers.CharField(required=False, default='width=device-width, initial-scale=1.0', max_length=100)
#     robots = serializers.CharField(required=False, default='index, follow', max_length=50)
    
#     # OpenGraph Tags
#     og_title = serializers.CharField(required=False, allow_blank=True)
#     og_description = serializers.CharField(required=False, allow_blank=True)
#     og_image_url = serializers.URLField(required=False, allow_blank=True)
#     og_url = serializers.URLField(required=False, allow_blank=True)
#     og_type = serializers.CharField(required=False, allow_blank=True)
    
#     # Twitter Card Tags
#     twitter_card_type = serializers.CharField(required=False, allow_blank=True)
#     twitter_site = serializers.CharField(required=False, allow_blank=True)
#     twitter_title = serializers.CharField(required=False, allow_blank=True)
#     twitter_description = serializers.CharField(required=False, allow_blank=True)
#     twitter_image = serializers.URLField(required=False, allow_blank=True)
    
#     # SEO Section
#     site_title = serializers.CharField(required=True) # Changed to required=True
#     site_description = serializers.CharField(required=False, allow_blank=True)
#     seo_keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
#     meta_content = serializers.CharField(required=False, allow_blank=True)
#     seo_meta_keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
#     # metaTags will be handled as a nested field directly or constructed from separate inputs
#     # For now, assuming it's part of the raw 'pages' input or constructed separately.
#     # To properly support `metaTags` like `metaTags: [{ "name": "...", "content": "..." }]`
#     # you would need a nested serializer for that list, or parse it from a string input if applicable.
#     # For simplicity of this example, assuming it's either part of complex 'pages' or omitted from direct input here.
#     # If it's a direct input, define it like:
#     # meta_tags = serializers.ListField(
#     #    child=serializers.DictField(child=serializers.CharField()), required=False, default=list
#     # )
#     # Adding a simple version of meta_tags for demonstration.
#     meta_tags = serializers.ListField(
#         child=serializers.DictField(), required=False, default=list,
#         help_text="List of objects like {'name': 'tag_name', 'content': 'tag_content'}"
#     )


#     # Pages (This expects the full nested page structure as input)
#     # This field expects the entire 'pages' array structure directly as provided in the JSON example.
#     # In a real form, this might come from a textarea for JSON, or a complex dynamic form.
#     pages = serializers.JSONField(required=False, default=list) # Changed to JSONField to accept complex data

#     # Global Modules
#     # These also expect the full nested structure. If coming from a form,
#     # you would either flatten them or use nested serializers.
#     # For this example, assuming they come as full nested JSON or are constructed like pages.
#     # For simplicity, if these are form inputs, you would flatten their fields.
#     # e.g., header_logo, header_nav_link_1_label, header_nav_link_1_url, etc.
#     # As per the SRS, these are part of "Global Modules" -> "Header", "Footer"
#     # I'll keep the flattened input fields as per your original `ProjectSpecCreateSerializer`
#     # and map them into the nested structure.

#     header_logo = serializers.CharField(required=False, allow_blank=True)
#     navigation_links = serializers.ListField(child=serializers.CharField(), required=False, default=list) # Assuming simple list of strings like "Home", "About"
#     cta_button_text = serializers.CharField(required=False, allow_blank=True) # Changed from cta_button
#     cta_button_link = serializers.URLField(required=False, allow_blank=True) # Added for CTA button link

#     footer_columns_data = serializers.JSONField(required=False, default=list, 
#                                                 help_text="JSON list of footer column objects, e.g., [{'title': 'Company', 'links': [{'label': 'About', 'link': '/about'}]}]")
#     social_links_data = serializers.JSONField(required=False, default=list, 
#                                             help_text="JSON list of social link objects, e.g., [{'platform': 'Facebook', 'url': 'https://...'}]")
#     copyright_text = serializers.CharField(required=False, allow_blank=True)

#     def create(self, validated_data):
#         """Convert form data to JSON spec and create ProjectSpec"""
#         json_data = self._build_json_structure(validated_data)
        
#         project_spec = ProjectSpec.objects.create(
#             project_name=validated_data['project_name'], # This remains flat
#             description=validated_data['description'], # This remains flat
#             json_data=json_data
#         )
        
#         return project_spec

#     def _build_json_structure(self, data):
#         """Build the nested JSON structure from flattened validated data"""
#         return {
#             "projectName": data['project_name'],
#             "description": data['description'],
#             "frontendFrameworks": data['frontend_frameworks'],
#             # "backendFrameworks": data.get('backend_frameworks', []), # Removed as per "avoid"
#             # "database": data.get('database', []), # Removed as per "avoid"
#             # "hostingProvider": data.get('hosting_provider', ''), # Removed as per "avoid"
#             "logoUrl": data['logo_url'],
#             "faviconUrl": data['favicon_url'],
#             "theme": {
#                 "primaryColor": data['primary_color'],
#                 "secondaryColor": data['secondary_color'],
#                 "fontFamily": data['font_family'],
#                 "style": data['style_description'] # Renamed 'styleDescription' to 'style' as per latest JSON
#             },
#             "siteUrl": data['site_url'],
#             "metaTitle": data['meta_title'],
#             "metaDescription": data['meta_description'],
#             "metaKeywords": data['meta_keywords'],
#             "author": data['author'],
#             "language": data['language'],
#             "charset": data['charset'],
#             "viewport": data['viewport'],
#             "robots": data['robots'],
#             "openGraphTags": {
#                 "ogTitle": data['og_title'],
#                 "ogDescription": data['og_description'],
#                 "ogImageUrl": data['og_image_url'],
#                 "ogUrl": data['og_url'],
#                 "ogType": data['og_type']
#             },
#             "twitterCardTags": {
#                 "cardType": data['twitter_card_type'],
#                 "twitterSite": data['twitter_site'],
#                 "title": data['twitter_title'],
#                 "description": data['twitter_description'],
#                 "image": data['twitter_image']
#             },
#             "seo": {
#                 "siteTitle": data['site_title'],
#                 "siteDescription": data['site_description'],
#                 "keywords": data['seo_keywords'],
#                 "metaContent": data['meta_content'],
#                 "metaKeywords": data['seo_meta_keywords'],
#                 "metaTags": data['meta_tags'] # Assuming this is passed directly
#             },
#             "pages": data['pages'], # Assuming full JSON for pages is passed
#             "globalModules": {
#                 "header": {
#                     "logo": data['header_logo'],
#                     "navigation": [ {"label": link, "link": f"/{link.lower()}"} for link in data['navigation_links'] ], # Example: transform string list to obj list
#                     "ctaButton": {
#                         "text": data['cta_button_text'],
#                         "link": data['cta_button_link']
#                     }
#                 },
#                 "footer": {
#                     "columns": data['footer_columns_data'], # Assuming full JSON for footer columns
#                     "socialLinks": data['social_links_data'], # Assuming full JSON for social links
#                     "copyright": data['copyright_text']
#                 }
#             }
#         }



from rest_framework import serializers
from .models import ProjectSpec
import re
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError as DjangoValidationError

# --- Nested Serializers for Input Validation (and common output structure) ---

class ThemeSerializer(serializers.Serializer):
    primaryColor = serializers.RegexField(regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', required=True)
    secondaryColor = serializers.RegexField(regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', required=True)
    fontFamily = serializers.CharField(required=True)
    style = serializers.CharField(required=True) # Matches the 'style' key in your desired JSON output

class OpenGraphTagsSerializer(serializers.Serializer):
    ogTitle = serializers.CharField(required=False, allow_blank=True)
    ogDescription = serializers.CharField(required=False, allow_blank=True)
    ogImageUrl = serializers.URLField(required=False, allow_blank=True)
    ogUrl = serializers.URLField(required=False, allow_blank=True)
    ogType = serializers.CharField(required=False, allow_blank=True)

class TwitterCardTagsSerializer(serializers.Serializer):
    cardType = serializers.CharField(required=False, allow_blank=True)
    twitterSite = serializers.CharField(required=False, allow_blank=True)
    title = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    image = serializers.URLField(required=False, allow_blank=True)

class SeoMetaTagSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    content = serializers.CharField(required=True)

class SeoSerializer(serializers.Serializer):
    siteTitle = serializers.CharField(required=True)
    siteDescription = serializers.CharField(required=False, allow_blank=True)
    keywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    metaContent = serializers.CharField(required=False, allow_blank=True)
    metaKeywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    metaTags = SeoMetaTagSerializer(many=True, required=False, default=list) # Nested list of meta tags

# Nested serializers for Global Modules
class HeaderCtaButtonSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, allow_blank=True)
    link = serializers.URLField(required=True, allow_blank=True)

class HeaderNavigationLinkSerializer(serializers.Serializer):
    label = serializers.CharField(required=True)
    link = serializers.CharField(required=True) # Could be URLField if external links expected

class HeaderSerializer(serializers.Serializer):
    logo = serializers.CharField(required=False, allow_blank=True) # Or URLField if expecting valid URL
    navigation = HeaderNavigationLinkSerializer(many=True, required=False, default=list)
    ctaButton = HeaderCtaButtonSerializer(required=False)

class FooterColumnLinkSerializer(serializers.Serializer):
    label = serializers.CharField(required=True)
    link = serializers.CharField(required=True)

class FooterColumnSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    links = FooterColumnLinkSerializer(many=True, required=False, default=list)

class FooterSocialLinkSerializer(serializers.Serializer):
    platform = serializers.CharField(required=True)
    url = serializers.URLField(required=True)

class FooterSerializer(serializers.Serializer):
    columns = FooterColumnSerializer(many=True, required=False, default=list)
    socialLinks = FooterSocialLinkSerializer(many=True, required=False, default=list)
    copyright = serializers.CharField(required=False, allow_blank=True)

class GlobalModulesSerializer(serializers.Serializer):
    header = HeaderSerializer(required=False)
    footer = FooterSerializer(required=False)

# Pages can be highly dynamic. For robust validation, you'd define serializers for common 'section types'
# and use a custom validation in PageSerializer's validate_sections.
# For maximum flexibility (if sections can vary wildly), we'll keep `sections` as a list of generic dictionaries
# with a basic `type` check, but know this is a trade-off.
class PageSectionSerializer(serializers.Serializer):
    # This is a very generic section serializer to allow flexible content.
    # For stricter validation of section content, you'd make specific serializers
    # (e.g., HeroSectionSerializer, ServicesOverviewSerializer) and then in PageSerializer's
    # validate_sections, you'd check the 'type' field and deserialize with the correct sub-serializer.
    type = serializers.CharField(required=True)
    # Allows any other fields to pass through, as their structure isn't strictly defined here.
    # When deserializing, just return the raw dictionary, assuming it's valid JSON
    def to_representation(self, instance):
        # When serializing for output, just return the dictionary as is
        return instance

    def to_internal_value(self, data):
        # When deserializing (for input), ensure it's a dict and has 'type'
        if not isinstance(data, dict):
            raise serializers.ValidationError("Each section must be a dictionary.")
        if 'type' not in data:
            raise serializers.ValidationError("Each section must have a 'type' field.")
        return data # Pass through the raw dictionary for the rest of the fields

class PageSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    url = serializers.CharField(required=True) # Could be URLField if internal paths are always URLs
    sections = PageSectionSerializer(many=True, required=False, default=list) # Validate sections using a sub-serializer

# --- Main Serializers ---

class ProjectSpecCreateSerializer(serializers.Serializer):
    """
    Serializer for creating project specs.
    This serializer *directly accepts* the nested JSON structure.
    It maps camelCase JSON keys to snake_case for Python processing if needed,
    but primarily uses camelCase as its field names to match the expected JSON input.
    """
    projectName = serializers.CharField(max_length=200) # project_name for model
    description = serializers.CharField()
    frontendFrameworks = serializers.ListField(child=serializers.CharField(), required=True)
    logoUrl = serializers.URLField(required=True)
    faviconUrl = serializers.URLField(required=True)

    # Nested objects validated by their own serializers
    theme = ThemeSerializer(required=True)
    siteUrl = serializers.URLField(required=True)
    metaTitle = serializers.CharField(required=False, allow_blank=True)
    metaDescription = serializers.CharField(required=False, allow_blank=True)
    metaKeywords = serializers.ListField(child=serializers.CharField(), required=False, default=list)
    author = serializers.CharField(required=False, allow_blank=True)
    language = serializers.CharField(required=False, default='en', max_length=10)
    charset = serializers.CharField(required=False, default='UTF-8', max_length=20)
    viewport = serializers.CharField(required=False, default='width=device-width, initial-scale=1.0', max_length=100)
    robots = serializers.CharField(required=False, default='index, follow', max_length=50)

    openGraphTags = OpenGraphTagsSerializer(required=False)
    twitterCardTags = TwitterCardTagsSerializer(required=False)
    seo = SeoSerializer(required=False)
    pages = PageSerializer(many=True, required=False, default=list) # List of page objects
    globalModules = GlobalModulesSerializer(required=False)

    def create(self, validated_data):
        # The validated_data dictionary already contains the correctly structured nested data
        # because the nested serializers have done their job.
        # We need to extract the model fields (project_name, description) and
        # put the rest into json_data.

        # Pop out fields that directly map to ProjectSpec model fields
        project_name = validated_data.pop('projectName') # Mapped to project_name in model
        description = validated_data.pop('description') # Mapped to description in model

        # The remaining validated_data is precisely the `json_data` content
        json_data_content = validated_data

        project_spec = ProjectSpec.objects.create(
            project_name=project_name,
            description=description,
            json_data=json_data_content # Save the entire validated_data as json_data
        )
        return project_spec

    # No update method needed for this example, but you would add it if supporting PUT/PATCH

class ProjectSpecSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving and listing ProjectSpec instances.
    This exposes the `json_data` as its raw JSON content.
    If you want to validate `json_data` upon update (PUT/PATCH),
    you can use the `ProjectSpecCreateSerializer` internally for that.
    """
    # Assuming json_data directly stores the complex structure.
    # If you want specific camelCase fields for output, you would define them here
    # or use a SerializerMethodField to transform json_data.
    # For simplicity, json_data is exposed directly as the model's JSONField.

    class Meta:
        model = ProjectSpec
        fields = ['id', 'project_name', 'description', 'json_data', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_json_data(self, value):
        """
        This method is primarily useful if this serializer is also used for
        updating (PUT/PATCH) ProjectSpec instances where `json_data` is sent directly.
        It re-uses the ProjectSpecCreateSerializer to ensure the incoming `json_data`
        conforms to the expected nested structure.
        """
        try:
            # Attempt to deserialize using the create serializer to validate structure.
            # `partial=True` can be added if updates don't require all fields to be present.
            temp_serializer = ProjectSpecCreateSerializer(data=value)
            temp_serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            # Re-raise the validation error with a clearer context
            raise serializers.ValidationError({"json_data_content_error": e.detail})
        return value