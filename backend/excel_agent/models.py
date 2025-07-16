from django.db import models

# Excel_agent model
class ExcelTask(models.Model):
    # Fields
    instruction = models.TextField(verbose_name='Instrucción')
    input_file = models.FileField(upload_to='input_excels/', verbose_name='Archivo de entrada')
    output_file = models.FileField(upload_to='output_excels/', null=True, blank=True, verbose_name='Archivo de salida')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    def __str__(self):
        return f'{self.pk} - {self.created_at}'
    
    class Meta:
        verbose_name = 'Documento Excel'
        verbose_name_plural = 'Documentos Excel'