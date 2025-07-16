from django.shortcuts import render
# Import requirement
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.http import FileResponse
from .serializer import ExcelTaskSerializer
from .utils import process_excel

# Create view class to process excel
class ProcessExcelView(APIView):
    permission_classes = [MultiPartParser]
    
    def post(self, request, *args, **kwargs):
        # Serializer
        serializer = ExcelTaskSerializer(data=request.data)
        
        # Validation serializer
        if serializer.is_valid():
            instruction = serializer.validated_data['instruction']
            file = serializer.validated_data['file']
            
            processed_file = process_excel(file, instruction)
            response = FileResponse(processed_file, as_attachment=True, filename='modified.xlsx')
            
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)