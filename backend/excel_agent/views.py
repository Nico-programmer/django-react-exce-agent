from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .excel_processor import process_excel_with_instruction
import os

media_dir = 'media'
os.makedirs(media_dir, exist_ok=True)

class ExcelAgentView(APIView):
    parser_classes = [MultiPartParser]
    
    def get(self, request):
        return Response({"message": "Este endpoint solo acepta POST con un archivo y una instrucción"}, status=200)
    
    def post(self, request):
        file = request.FILES.get('file')
        instruction = request.data.get('instruction')
        
        if not file or not instruction:
            return Response({"error": "Falta archivo o instruction"}, status=400)
        
        # Guardar archivo temporalmente
        file_path = os.path.join(media_dir, file.name)
        with open(file_path, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)
        
        try:
            modified_path = process_excel_with_instruction(file_path, instruction)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
        # Retornar archivo resultante
        with open(modified_path, 'rb') as f:
            response = Response(
                f.read(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(modified_path)}"'
            return response
