from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from .models import ProjectSpec
from .serializers import ProjectSpecSerializer, ProjectSpecCreateSerializer
from .forms import ProjectSpecForm
import json
from . import utils
from django.http import JsonResponse, HttpResponse, Http404

# API Views
class ProjectSpecListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProjectSpec.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectSpecCreateSerializer
        return ProjectSpecSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return utils.api_response(True, "Project specs fetched successfully.", serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return utils.api_response(True, "Project specs fetched successfully.", serializer.data)

    
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
        return utils.api_response(False, "Invalid request data.", serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)

class ProjectSpecRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ProjectSpec.objects.all()
    serializer_class = ProjectSpecSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return utils.api_response(True, "Project spec retrieved successfully.", serializer.data)


@api_view(['GET'])
def download_json(request, pk):
    """Download JSON spec as file"""
    try:
        project_spec = get_object_or_404(ProjectSpec, pk=pk)
    except Http404:
        # If get_object_or_404 raises Http404, we catch it here and return
        # our custom API response for "Not Found".
        # This explicitly uses utils.api_response for this specific case.
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
    response['Content-Disposition'] = f'attachment; filename="{project_spec.project_name}_spec.json"'
    return response

# Web Views
def spec_create_view(request):
    """Web form for creating specs"""
    if request.method == 'POST':
        form = ProjectSpecForm(request.POST)
        if form.is_valid():
            # Convert form data to JSON
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
    return JsonResponse(spec.json_data, json_dumps_params={'indent': 2})
