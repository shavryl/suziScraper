from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import BottomData, ExclusivesData
from django.views.generic import TemplateView


@csrf_exempt
@require_http_methods(['POST'])
def get_data(request):

    if request.method == 'POST':

        bottoms_data = BottomData.objects.all().values()
        exclusives_data = ExclusivesData.objects.all().values()
        data_list = list(bottoms_data)
        exclusives_list = list(exclusives_data)

        for obj in exclusives_list:
            data_list.append(obj)

        return JsonResponse(data_list, safe=False)


class HomeView(TemplateView):
    template_name = 'index.html'
