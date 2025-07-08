# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.views.generic import CreateView, ListView
# from .models import ProjectSpec
# from .serializers import ProjectSpecSerializer, ProjectSpecCreateSerializer
# from .forms import ProjectSpecForm # Assuming you still use this for web views
# import json
# from . import utils # Assuming utils.py provides api_response
# from django.http import JsonResponse, HttpResponse, Http404

# # API Views
# class ProjectSpecListCreateAPIView(generics.ListCreateAPIView):
#     queryset = ProjectSpec.objects.all()
    
#     def get_serializer_class(self):
#         """
#         Dynamically chooses the serializer based on the request method.
#         - POST requests will use ProjectSpecCreateSerializer (for input and validation).
#         - GET requests will use ProjectSpecSerializer (for output).
#         This is correctly implemented for the new serializer structure.
#         """
#         if self.request.method == 'POST':
#             return ProjectSpecCreateSerializer
#         return ProjectSpecSerializer
    
#     def list(self, request, *args, **kwargs):
#         """
#         Handles listing of ProjectSpecs.
#         Uses ProjectSpecSerializer for output, which correctly maps json_data fields.
#         """
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return utils.api_response(True, "Project specs fetched successfully.", serializer.data)
        
#         serializer = self.get_serializer(queryset, many=True)
#         return utils.api_response(True, "Project specs fetched successfully.", serializer.data)

    
#     def create(self, request, *args, **kwargs):
#         """
#         Handles creation of ProjectSpecs.
#         - Uses ProjectSpecCreateSerializer for data input and all defined validations.
#         - If serializer.is_valid() passes, it means all field-level and the custom
#           `validate` method logic (including globalModules validation) have passed.
#         - It then saves the project_spec and returns the newly created object
#           serialized with ProjectSpecSerializer for consistency in output.
#         This method remains correct and handles validation automatically.
#         """
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             project_spec = serializer.save()
#             # Respond with the ProjectSpecSerializer to show the structured output
#             response_serializer = ProjectSpecSerializer(project_spec)
#             return utils.api_response(
#                 True, 
#                 "Project spec created successfully.", 
#                 response_serializer.data, 
#                 status_code=status.HTTP_201_CREATED
#             )
#         # If serializer.is_valid() is False, serializer.errors will contain
#         # all validation messages, including those from the custom `validate` method.
#         return utils.api_response(False, "Invalid request data.", serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

# class ProjectSpecRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = ProjectSpec.objects.all()
#     serializer_class = ProjectSpecSerializer # Uses ProjectSpecSerializer for output
    
#     def retrieve(self, request, *args, **kwargs):
#         """
#         Handles retrieval of a single ProjectSpec.
#         Uses ProjectSpecSerializer for output.
#         """
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return utils.api_response(True, "Project spec retrieved successfully.", serializer.data)


# @api_view(['GET'])
# def download_json(request, pk):
#     """
#     Download JSON spec as file.
#     This view directly fetches the `json_data` from the model, so it doesn't
#     directly interact with the serializers for validation/structure, but rather
#     serves the already stored data.
#     """
#     try:
#         project_spec = get_object_or_404(ProjectSpec, pk=pk)
#     except Http404:
#         return utils.api_response(
#             False, 
#             "Project spec not found.", 
#             None, 
#             status_code=status.HTTP_404_NOT_FOUND
#         )
    
#     response = HttpResponse(
#         json.dumps(project_spec.json_data, indent=2),
#         content_type='application/json'
#     )
#     response['Content-Disposition'] = f'attachment; filename="{project_spec.project_name}_spec.json"'
#     return response

# # Web Views (assuming these are for a traditional Django template-based frontend)
# def spec_create_view(request):
#     """
#     Web form for creating specs.
#     This view uses a Django Form (ProjectSpecForm) and then maps its cleaned_data
#     to the ProjectSpecCreateSerializer. This mapping is where the new serializer
#     structure shines, as it expects flattened data.
#     All validations defined in ProjectSpecCreateSerializer will apply here too.
#     """
#     if request.method == 'POST':
#         form = ProjectSpecForm(request.POST)
#         if form.is_valid():
#             # Convert form data to JSON using the serializer
#             # The form.cleaned_data should align with the expected input of ProjectSpecCreateSerializer
#             serializer = ProjectSpecCreateSerializer(data=form.cleaned_data)
#             if serializer.is_valid():
#                 project_spec = serializer.save()
#                 return JsonResponse({
#                     'success': True,
#                     'id': project_spec.id,
#                     'json_data': project_spec.json_data # Returns the full JSON data
#                 })
#             else:
#                 # Serializer validation errors (including custom ones)
#                 return JsonResponse({
#                     'success': False,
#                     'errors': serializer.errors
#                 }, status=400)
#         else:
#             # Django Form validation errors
#             return JsonResponse({
#                 'success': False,
#                 'errors': form.errors
#             }, status=400)
#     else:
#         form = ProjectSpecForm()
    
#     return render(request, 'specs/create.html', {'form': form})

# def spec_list_view(request):
#     """List all specs"""
#     specs = ProjectSpec.objects.all()
#     return render(request, 'specs/list.html', {'specs': specs})

# def spec_detail_view(request, pk):
#     """View specific spec"""
#     spec = get_object_or_404(ProjectSpec, pk=pk)
#     # This directly returns the stored json_data, no serializer is used for output here.
#     return JsonResponse(spec.json_data, json_dumps_params={'indent': 2})






# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.views.generic import CreateView, ListView
# from .models import ProjectSpec
# from .serializers import ProjectSpecSerializer, ProjectSpecCreateSerializer
# from .forms import ProjectSpecForm
# import json
# from . import utils
# from django.http import JsonResponse, HttpResponse, Http404

# # API Views
# class ProjectSpecListCreateAPIView(generics.ListCreateAPIView):
#     queryset = ProjectSpec.objects.all()
    
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return ProjectSpecCreateSerializer
#         return ProjectSpecSerializer
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return utils.api_response(True, "Project spec not found.", serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return utils.api_response(True, "Project specs fetched successfully.", serializer.data)

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             project_spec = serializer.save()
#             response_serializer = ProjectSpecSerializer(project_spec)
#             return utils.api_response(
#                 True, 
#                 "Project spec created successfully.", 
#                 response_serializer.data, 
#                 status_code=status.HTTP_201_CREATED
#             )
#         return utils.api_response(False, "Invalid request data.", serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

# class ProjectSpecRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = ProjectSpec.objects.all()
#     serializer_class = ProjectSpecSerializer

#     def retrieve(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object() # This will raise Http404 if not found
#             serializer = self.get_serializer(instance)
#             return utils.api_response(True, "Project spec fetched successfully.", serializer.data)
#         except Http404:
#             return utils.api_response(False, "Project spec not found.", None, status_code=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def download_json(request, pk):
#     """Download JSON spec as file"""
#     try:
#         project_spec = get_object_or_404(ProjectSpec, pk=pk)
#     except Http404:
#         # If get_object_or_404 raises Http404, we catch it here and return
#         # our custom API response for "Not Found".
#         # This explicitly uses utils.api_response for this specific case.
#         return utils.api_response(
#             False, 
#             "Project spec not found.", 
#             None, 
#             status_code=status.HTTP_404_NOT_FOUND
#         )
    
#     response = HttpResponse(
#         json.dumps(project_spec.json_data, indent=2),
#         content_type='application/json'
#     )
#     response['Content-Disposition'] = f'attachment; filename="{project_spec.project_name}_spec.json"'
#     return response

# # Web Views
# def spec_create_view(request):
#     """Web form for creating specs"""
#     if request.method == 'POST':
#         form = ProjectSpecForm(request.POST)
#         if form.is_valid():
#             # Convert form data to JSON
#             serializer = ProjectSpecCreateSerializer(data=form.cleaned_data)
#             if serializer.is_valid():
#                 project_spec = serializer.save()
#                 return JsonResponse({
#                     'success': True,
#                     'id': project_spec.id,
#                     'json_data': project_spec.json_data
#                 })
#             else:
#                 return JsonResponse({
#                     'success': False,
#                     'errors': serializer.errors
#                 }, status=400)
#         else:
#             return JsonResponse({
#                 'success': False,
#                 'errors': form.errors
#             }, status=400)
#     else:
#         form = ProjectSpecForm()
    
#     return render(request, 'specs/create.html', {'form': form})

# def spec_list_view(request):
#     """List all specs"""
#     specs = ProjectSpec.objects.all()
#     return render(request, 'specs/list.html', {'specs': specs})

# def spec_detail_view(request, pk):
#     """View specific spec"""
#     spec = get_object_or_404(ProjectSpec, pk=pk)
#     return JsonResponse(spec.json_data, json_dumps_params={'indent': 2})


from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
import json
from rest_framework.exceptions import ErrorDetail

from .models import ProjectSpec
from .serializers import ProjectSpecSerializer, ProjectSpecCreateSerializer
# Assuming you have a forms.py, but for API/JSON generation, serializers are often preferred
# from .forms import ProjectSpecForm 

# utils.py - You need to ensure this file exists and contains the api_response function
# If you don't have this, you can define a simple version:
# def api_response(success, message, data=None, status_code=status.HTTP_200_OK):
#     return Response({'success': success, 'message': message, 'data': data}, status=status_code)
from . import utils 

# API Views
class ProjectSpecListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProjectSpec.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectSpecCreateSerializer
        return ProjectSpecSerializer

    # ... (list method remains the same)

    def _get_single_readable_error_message(self, errors_dict, parent_path=""):
        """
        Recursively extracts the first human-readable error message encountered.
        Returns a single string message or None if no errors are found.
        """
        for field, error_detail in errors_dict.items():
            # Adjust field name for readability (e.g., camelCase to space-separated)
            readable_field_name = field.replace('_', ' ').replace('.', ' ')
            
            if isinstance(error_detail, list):
                # This field has direct errors (e.g., 'projectName': ['This field is required.'])
                if error_detail: # Make sure the list is not empty
                    # If it's an ErrorDetail object, use its string representation
                    error_string = str(error_detail[0]) if isinstance(error_detail[0], ErrorDetail) else error_detail[0]
                    
                    # For top-level fields, display "Field Name: Error Message"
                    if not parent_path: # This means it's a top-level field
                        return f"{readable_field_name}: {error_string}"
                    else:
                        # For nested fields, display "Parent.Field Name: Error Message" or just "Field Name: Error Message"
                        # We'll stick to a simpler "Field Name: Error Message" for readability in the single message
                        return f"{readable_field_name}: {error_string}"
                        
            elif isinstance(error_detail, dict):
                # This field contains nested errors, recurse into it
                nested_message = self._get_single_readable_error_message(error_detail, parent_path=f"{parent_path}.{field}" if parent_path else field)
                if nested_message:
                    return nested_message # Return the first error found in nested structure

            # If neither list nor dict, or list is empty, continue to next field.
        return None # No errors found in this dictionary level

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            project_spec = serializer.save()
            response_serializer = ProjectSpecSerializer(project_spec)
            return utils.api_response(
                True,
                "Project spec created successfully.",
                response_serializer.data,
                status_code=status.HTTP_201_CREATED
            )
        else:
            print("\n--- Serializer Validation Errors ---")
            print(serializer.errors)
            print("--- End Serializer Errors ---\n")

            # Get the single, prioritized error message
            display_message = self._get_single_readable_error_message(serializer.errors)

            if not display_message:
                # Fallback if for some reason no specific error was extracted
                display_message = "Invalid request data. Please check the provided fields."
            else:
                # Capitalize the first letter of the generated message
                display_message = display_message[0].upper() + display_message[1:]

            return utils.api_response(
                False,
                display_message, # Use our generated single message
                None, # Explicitly set data to None
                status_code=status.HTTP_400_BAD_REQUEST
            )
class ProjectSpecRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ProjectSpec.objects.all()
    serializer_class = ProjectSpecSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object() # This will raise Http404 if not found
            serializer = self.get_serializer(instance)
            return utils.api_response(True, "Project spec fetched successfully.", serializer.data)
        except Http404:
            return utils.api_response(False, "Project spec not found.", None, status_code=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def download_json(request, pk):
    """Download JSON spec as file"""
    try:
        project_spec = get_object_or_404(ProjectSpec, pk=pk)
    except Http404:
        return utils.api_response(
            False, 
            "Project spec not found.", 
            None, 
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    response = HttpResponse(
        json.dumps(project_spec.json_data, indent=2),
        content_type='application/json'
    )
    # Ensure project_name is safe for filename
    filename_safe_name = project_spec.project_name.replace(" ", "_").replace("/", "_")
    response['Content-Disposition'] = f'attachment; filename="{filename_safe_name}_spec.json"'
    return response

# Web Views (You might re-evaluate if you still need ProjectSpecForm for web views or if you're going API-only)
# For the web views, you would typically use a Django Form for input.
# If ProjectSpecForm directly maps to the *final JSON structure*, it would be complex.
# If it maps to the flattened data that ProjectSpecCreateSerializer expects, it's feasible.
# Assuming 'ProjectSpecForm' is updated to reflect the new flattened fields for input.

def spec_create_view(request):
    """Web form for creating specs"""
    # This part assumes a Django Form (ProjectSpecForm) is used,
    # and its fields align with ProjectSpecCreateSerializer's input fields.
    # If you intend to use a single input method (e.g., REST API with a JS frontend),
    # these web views might become less relevant or need significant refactoring
    # to use serializers directly for rendering the form fields.
    
    # Placeholder: You'll need to define ProjectSpecForm in forms.py
    # and ensure it matches the fields in ProjectSpecCreateSerializer.
    # from .forms import ProjectSpecForm 
    
    # For simplicity, if you are focusing on the API, this web view part
    # might need a more detailed implementation or a front-end framework.
    # I'm keeping the existing logic structure but note the dependency on ProjectSpecForm.

    # Example of how you *might* render a form if you want to use the serializer's fields
    # as a basis for a form, but this is a complex topic for a full re-write of `forms.py`
    # and template rendering based on serializer fields.
    
    # A simplified example if ProjectSpecForm is indeed providing flat data
    from .forms import ProjectSpecForm # Make sure this form exists and is aligned

    if request.method == 'POST':
        form = ProjectSpecForm(request.POST)
        if form.is_valid():
            # Use the ProjectSpecCreateSerializer to build and save the JSON
            serializer = ProjectSpecCreateSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                project_spec = serializer.save()
                return JsonResponse({
                    'success': True,
                    'id': project_spec.id,
                    'json_data': project_spec.json_data
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': serializer.errors
                }, status=400)
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            }, status=400)
    else:
        form = ProjectSpecForm()
    
    return render(request, 'specs/create.html', {'form': form})

def spec_list_view(request):
    """List all specs"""
    specs = ProjectSpec.objects.all()
    return render(request, 'specs/list.html', {'specs': specs})

def spec_detail_view(request, pk):
    """View specific spec"""
    spec = get_object_or_404(ProjectSpec, pk=pk)
    # This returns the raw JSON data of the model instance
    return JsonResponse(spec.json_data, json_dumps_params={'indent': 2})