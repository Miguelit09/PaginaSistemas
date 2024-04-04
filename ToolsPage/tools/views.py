from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .models import Tool
# Create your views here.

def library(request, tools=None, no_matches=False):
    if tools is None:
        tools = Tool.objects.all()
    
    return render(request, 'library.html', {
        'tools': tools,
        'no_matches': no_matches,
    })

def search_tools(request):
    search_language = request.GET['search_language']
    search_entry = request.GET['search_entry']
    results = Tool.objects.filter(**{f'{search_language}_name__icontains': search_entry})
    if (results.count()==0):
        no_matches = True
    else:
        no_matches = False
    return library(request, tools=results, no_matches=no_matches)

def get_tool(request, tool_id):
    tool = Tool.objects.get(id=tool_id)
    tool_data = {
        'english_name': tool.english_name,
        'english_description': tool.english_description,
        'spanish_name': tool.spanish_name,
        'spanish_description': tool.spanish_description,
        'tool_image': tool.tool_image
    }
    return JsonResponse(tool_data)

def create_database(request):
    # tool1 = Tool.objects.create(
    #     english_name = "Miller Fiber Optic Polishing Disc for LC connectors",
    #     english_description = "Aluminum disc for 1.25 mm ferrules. -- External diameter: 49.2 mm. -- Weight 43 gr",
    #     spanish_name = "Disco de pulido manual para conectores LC",
    #     spanish_description = "Disco de aluminio para ferrules de 1,25 mm. -- External diameter: 49.2 mm. -- Weight 43 gr",
    #     tool_image = 'image1.png'
    #     )
    # tool2 = Tool.objects.create(
    #     english_name = "2.5mm SC/FC/ST Universal Hand Polishing Disc",
    #     english_description = "Aluminum disc for 2.5 mm ferrules. -- Diam: Ext 49.2 -- mm: Weight 43 gr.",
    #     spanish_name = "Disco de pulido manual para conectores FCST-SC",
    #     spanish_description = "Disco de aluminio para ferrules de 2,5 mm. -- Diam: Ext 49,2 -- mm: Peso 43 gr.",
    #     tool_image = 'image2.png'
    #     )
    # tool3 = Tool.objects.create(
    #     english_name = "Swabs cleaning (Pack of 200)",
    #     english_description = "Made with particle-free material, diameter 2.5 mm.",
    #     spanish_name = "Bastoncillos de limpieza (Pack de 200)",
    #     spanish_description = "Elaborados con material libre de partículas diám 2,5 mm.",
    #     tool_image = 'image3.png'
    #     )
    # tool4 = Tool.objects.create(
    #     english_name = "Kim Wipes (Boxes of 280 units)",
    #     english_description = "Supplied in a dispenser box. Highly absorbent and with low particle emission.",
    #     spanish_name = "Toallitas Kim Wipes (Cajas de 280 u.)",
    #     spanish_description = "Suministradas en caja-dispensador. Muy absorbentes y con baja emisión de partículas.",
    #     tool_image = 'image4.png'
    #     )
    # tool5 = Tool.objects.create(
    #     english_name = "Optic Prep pre-impregnated wipes (Box of 50u.)",
    #     english_description = "Impregnated with cleaning solutioncompatible with mostplastic, metal and glass materials",
    #     spanish_name = "Toallitas pre impregnadas Optic Prep (Caja de 50u.)",
    #     spanish_description = "Impregnadas con solución limpiadora compatible con la mayoría de los materiales plásticos, metálicos y vidrios",
    #     tool_image = 'image5.png'
    #     )
    # tool6 = Tool.objects.create(
    #     english_name = "Automatic alcohol dispenser",
    #     english_description = "Very stable and manageable. Capacity 150 ml.",
    #     spanish_name = "Dispensador de alcohol automático",
    #     spanish_description = "Muy estable y manejable. Capacidad 150 ml.",
    #     tool_image = 'image6.png'
    #     )
    tool7 = Tool.objects.create(
        english_name = "MILLER alcohol dispenser",
        english_description = "Dimensions: 79 x 54 mm.Capacity: 118ml",
        spanish_name = "Dispensador MILLER de alcohol",
        spanish_description = "Dimensiones: 79 x 54 mm.Capacidad: 118 ml",
        tool_image = 'image7.png'
        )
    tool8 = Tool.objects.create(
        english_name = "CLETOP-S Cleaner for SC-FC-ST-DIN and D4",
        english_description = "Dimensions: 130 x 75 x 40 mm. (160 gr.) Approximate capacity: 400 applications.",
        spanish_name = "Limpiador CLETOP-S para SC-FC-ST-DIN y D4",
        spanish_description = "Dimensiones: 130 x 75 x 40 mm. (160 gr.) Capacidad aprox.: 400 aplic.",
        tool_image = 'image8.png'
        )
    tool9 = Tool.objects.create(
        english_name = "Replacement cartridge for CLETOP cleaner",
        english_description = "The Cletop-S 14110710 Replacement Reel is designed to be used with the CLETOP-S fiber ferrule cleaner",
        spanish_name = "Cartucho de recambio para limpiador CLETOP",
        spanish_description = "El carrete de repuesto Cletop-S 14110710 está diseñado para ser utilizado con el limpiador de virola de fibra CLETOP-S",
        tool_image = 'image9.png'
        )
    tool10 = Tool.objects.create(
        english_name = "Fiber Optic Polishing Kit",
        english_description = "Grains 0.3 um; 5um and 12 um",
        spanish_name = "Kit de pulido de fibra óptica",
        spanish_description = "Granos 0,3 um; 5um y 12 um",
        tool_image = 'image10-11.png'
        )
    tool11 = Tool.objects.create(
        english_name = "Diamond abrasive discs",
        english_description = "216 x 280mm sheets",
        spanish_name = "Discos de abrasivo diamante",
        spanish_description = "Pliegos de 216 x 280mm-",
        tool_image = 'image10-11.png'
        )
    tool12 = Tool.objects.create(
        english_name = "KMS tool for longitudinal roof cutting",
        english_description = "For longitudinal cutting and section of reinforced outer cable. (Up to 25 mm diameter).",
        spanish_name = "Herramienta KMS para corte longitudinal de cubierta",
        spanish_description = "Para corte longitudinal y sección de cable exterior armado. (Hasta 25 mm. diámetro).",
        tool_image = 'image12.png'
        )
    tool13 = Tool.objects.create(
        english_name = "Three carnations curved knife",
        english_description = "Curved blade electrician's knife.",
        spanish_name = "Navaja curva tres claveles",
        spanish_description = "Navaja de electricista de hoja curva.",
        tool_image = 'image13.png'
        )
    tool14 = Tool.objects.create(
        english_name = "MILLER adjustable peeler 0.65 to 2.6 mm.",
        english_description = "Length: 134mm. Weight 71 gr. With adjustment cam For preparing cables with diameters between 0.65 and 2.6 mm",
        spanish_name = "Peladora ajustable MILLER 0,65 a 2,6 mm.",
        spanish_description = "Longitud: 134 mm. Peso 71 gr. Con leva de ajuste Para preparación de cables de diámetros entre 0,65 y 2,6 mm",
        tool_image = 'image14.png'
        )
    tool15 = Tool.objects.create(
        english_name = "Circular tire peeler 4.5 to 25 mm.",
        english_description = "To remove insulation from cables. (Not PE) Adjustable depth up to 4.5 mm.",
        spanish_name = "Peladora circular de cubiertas 4,5 a 25 mm.",
        spanish_description = "Para eliminar el aislamiento de los cables. (No PE) Profundidad graduable hasta 4,5 mm.",
        tool_image = 'image15.png'
        )
    tool16 = Tool.objects.create(
        english_name = "Circular tire peeler 4.5 to 29 mm.",
        english_description = "Long. 138mm. Weight 100 gr. For stripping cables from 4.5 to 29 mm.",
        spanish_name = "Peladora circular de cubiertas 4,5 a 29 mm.",
        spanish_description = "Long. 138 mm. Peso 100 gr. Para el pelado de cables de 4,5 a 29 mm.",
        tool_image = 'image16.png'
        )
    tool17 = Tool.objects.create(
        english_name = "Clauss multi-mouth peeler (AWG 10 to 20)",
        english_description = "Multiple multi-mouth peeler for AWG 10 to AWG 20. (0.6 mm. to 2.6 mm.) Length 152 mm.",
        spanish_name = "Peladora Clauss multiboca (AWG 10 a 20)",
        spanish_description = "Peldora múltiple multiboca para AWG 10 a AWG 20. (0,6 mm. a 2,6 mm.) Longitud 152 mm.",
        tool_image = 'image17.png'
        )
    tool18 = Tool.objects.create(
        english_name = "Miller multiple peeler 0.6 to 2.6 mm",
        english_description = "Fine multi-mouth stripper for AWG 10 to AWG 22. (0.6 mm. to 2.6 mm.) Serrated tip Closing mechanism.",
        spanish_name = "Peladora múltiple Miller 0,6 a 2,6 mm.",
        spanish_description = "Peladora multiple multiboca para AWG 10 a AWG 22. (0,6 mm. a 2,6 mm.) Punta dentada Mecanismo de cierre.",
        tool_image = 'image18.png'
        )
    tool19 = Tool.objects.create(
        english_name = "Covered peeler from 4.8 to 8 mm.",
        english_description = "IDEAL stripping machine for stripping cables and tubes. Includes three straight blades and one circular blade",
        spanish_name = "Peladora cubierta de 4,8 a 8 mm.",
        spanish_description = "Peladora IDEAL para el desnudado de cables y tubos. Incluye tres cuchillas rectas y una circular.",
        tool_image = 'image19.png'
        )
    tool20 = Tool.objects.create(
        english_name = "Three carnation scissors with insulator",
        english_description = "Electrician's scissors, insulated, steel.",
        spanish_name = "Tijera tres claveles con aislante",
        spanish_description = "Tijeras de electricista, aisladas, de acero.",
        tool_image = 'image20.png'
        )
    tool21 = Tool.objects.create(
        english_name = "KLAUSS Kevlar Scissors 16 mm.",
        english_description = "Steel scissors, for Kevlar, with serrated blade, and recovery spring",
        spanish_name = "Tijeras para Kevlar KLAUSS 16 mm.",
        spanish_description = "Tijeras de acero , para Kevlar, con cuchilla dentada,y muelle de recuperación",
        tool_image = 'image21.png'
        )
    tool22 = Tool.objects.create(
        english_name = "MILLER Scissors for Kevlar",
        english_description = "Steel scissors, smooth blade, for cutting Kevlar. Length 140mm. Weight 80 gr.",
        spanish_name = "Tijeras MILLER para Kevlar",
        spanish_description = "Tijeras de acero, cuchilla lisa, para el corte de Kevlar. Longitud 140 mm. Peso 80 gr.",
        tool_image = 'image22.png'
        )
    tool23 = Tool.objects.create(
        english_name = "Tool for longitudinal intermediate and end cuts",
        english_description = "Tube diameter 3.0 to 3.3mm.",
        spanish_name = "Herramienta para cortes longitudinales intermedios y en extremos",
        spanish_description = "Diámetro del tubo 3,0 a 3,3 mm.",
        tool_image = 'image23.png'
        )
    tool24 = Tool.objects.create(
        english_name = "Jaw and pliers set for longitudinal cuts",
        english_description = "Includes pliers, support and heads for 1.8/2.2/2.5/3.0 and 3.3 mm.",
        spanish_name = "Juego de mordaza y tenaza para cortes longitudinales",
        spanish_description = "Incluye tenaza, soporte y cabezales para 1,8/2,2/2,5/3,0 y 3,3 mm.",
        tool_image = 'image24.png'
        )
    tool25 = Tool.objects.create(
        english_name = "MILLER triple peeler (250 and 900 um) (3 mm.)",
        english_description = "Metal peeling machine for 250 and 900 um coatings, and for 3 mm covers. Length 137mm. Weight 71 gr.",
        spanish_name = "Peladora triple MILLER (250 y 900 um) (3 mm.)",
        spanish_description = "Peladora metálica para revestimiento de 250 y 900 um, y para cubiertas de 3 mm. Longitud 137 mm. Peso 71 gr.",
        tool_image = 'image25.png'
        )
    tool26 = Tool.objects.create(
        english_name = "MILLER 900 and 250 um fiber peeling machine",
        english_description = "Metal peeling machine for 250 and 900 um coating. Length 137mm. Weight 71 gr.",
        spanish_name = "Peladora de fibra MILLER 900 y 250 um",
        spanish_description = "Peladora metálica para revestimiento de 250 y 900 um. Longitud 137 mm. Peso 71 gr.",
        tool_image = 'image26.png'
        )
    tool27 = Tool.objects.create(
        english_name = "MILLER fiber peeling machine for 250 um",
        english_description = "Peeler for standard 250 um coating and 3 mm covers. Length 165mm. Weight 119 gr.",
        spanish_name = "Peladora de fibra MILLER para 250 um",
        spanish_description = "Peladora para recubrimiento standard de 250 um y cubiertas de 3 mm. Longitud 165 mm. Peso 119 gr.",
        tool_image = 'image27.png'
        )
    tool28 = Tool.objects.create(
        english_name = "MILLER fiber stripper with 3 holes Cover 1.6 to 3 mm Buffer 600 to 900 um Acrylate 250 um",
        english_description = "Replaces the NONIK tool (discontinued). Available on request",
        spanish_name = "Peladora de fibra MILLER con 3 huecos • Cubierta 1,6 a 3 mm • Buffer 600 a 900 um • Acrilato 250 um",
        spanish_description = "Sustituye a la herramienta NONIK (descatalogada). Disponible bajo demanda",
        tool_image = 'image28.png'
        )
    tool29 = Tool.objects.create(
        english_name = "Fiber stripper > 140 um, red blade.",
        english_description = "Plastic peeler, axial action, with length limitation.",
        spanish_name = "Peladora de fibra > 140 um, cuchilla roja.",
        spanish_description = "Peladora plástica, de acción axial, con limitación de longitud.",
        tool_image = 'image29.png'
        )
    tool30 = Tool.objects.create(
        english_name = "Tungsten cutter for fiber scraps.",
        english_description = "With fixing clip.Length 112mm.Diam. 25mm tip",
        spanish_name = "Cortador de tungsteno para sobrantes de fibra.",
        spanish_description = "Con clip de fijación. Longitud 112 mm. Diam. Punta 25 mm",
        tool_image = 'image30.png'
        )
    return HttpResponse('Base de datos creada')