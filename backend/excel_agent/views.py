from django.shortcuts import render
# Import requirement
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .excel_processor import process_excel_with_instruction
import os

class ExcelAgentView(APIView):
    parser_classes = [MultiPartParser]
    
    def post(self, request):
        file = request.FILES.get('file')
        instruction = request.data.get('instruction')
        
        if not file or not instruction:
            return Response({"error": "Falta archivo o instruction"}, status=400)
        
        # Saves the file temporarily
        file_path = f"media/{file.name}"
        with open(file_path, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)
                
        try:
            modified_path = process_excel_with_instruction(file_path, instruction)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
        # Returns the file
        with open(modified_path, 'rb') as f:
            response = Response(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(modified_path)}"'
            return response