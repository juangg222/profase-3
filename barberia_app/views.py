from django.shortcuts import render, redirect
from .forms import AgendaForm  # Importar el formulario personalizado para agendar citas

# Vista principal
def home(request):
    # Renderiza la página principal (home.html)
    return render(request, 'home.html')

# Vista de servicios
def servicios(request):
    # Renderiza la página de servicios (servicios.html)
    return render(request, 'servicios.html')

# Vista para agendar citas
def agenda(request):
    if request.method == 'POST':  # Si la solicitud es POST (se envió el formulario)
        form = AgendaForm(request.POST)  # Cargar los datos enviados al formulario
        if form.is_valid():  # Verifica si los datos son válidos
            form.save()  # Guarda los datos válidos en la base de datos
            return redirect('confirmacion')  # Redirige al usuario a la página de confirmación
    else:  # Si la solicitud es GET (se abre la página)
        form = AgendaForm()  # Crea un formulario vacío para mostrarlo al usuario
    
    # Renderiza el formulario en la plantilla agenda.html
    return render(request, 'agenda.html', {'form': form})

# Vista de confirmación
def confirmacion(request):
    # Muestra una página de confirmación tras enviar el formulario
    return render(request, 'confirmacion.html')


def servicios_view(request):
    return render(request, 'servicios.html')
