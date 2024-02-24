from django.db import models
	

class Employee(models.Model):
    """_summary_
       Modelo correspondiente a la tabla employee
    """
    first_name = models.CharField(max_length=50, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    document_type = models.CharField(
        max_length=20, verbose_name='Tipo de Documento')
    document_number = models.CharField(
        max_length=20, verbose_name='Numero de Documento')
    birthdate = models.DateField(verbose_name='Fecha de Nacimiento')
    phone_number = models.CharField(
        max_length=20, verbose_name='Numero de Telefono')
    address = models.CharField(max_length=50, verbose_name='Dirección')
    martial_status = models.CharField(
        max_length=20, verbose_name='Estado Civil')
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Salario')
    job = models.CharField(max_length=50, verbose_name='Cargo')
    department = models.CharField(max_length=50, verbose_name='Departamento')
    city = models.CharField(max_length=50, verbose_name='Ciudad')
    country = models.CharField(max_length=50, verbose_name='Pais')
    date_hired = models.DateField(
        auto_now_add=True, verbose_name='Fecha de Contratación')

    class Meta:
        """_summary_
           Clase Meta para definir el nombre de la tabla
        """
        db_table = 'employee'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """_summary_
           Método para retornar el nombre completo del empleado
        """
        return f'{self.first_name} {self.last_name}'