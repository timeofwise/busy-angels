from django.shortcuts import render
import csv, io
from django.shortcuts import render
from django.contrib import messages
from rich.models import Asset

# Create your views here.

def AssetUpload(request):
    # declaring template
    template = "testcsv/asset_upload.html"
    data = Asset.objects.all()

    prompt = {
        'order': 'Order of the CSV should be date, p1~6, and f1~6',
        'assets': data
    }

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('cp949')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Asset.objects.update_or_create(
            #date=column[0],
            present_value_1=int(column[1]),
            present_value_2=int(column[2]),
            present_value_3=int(column[3]),
            present_value_4=int(column[4]),
            present_value_5=int(column[5]),
            present_value_6=int(column[6]),
            future_value_1=int(column[7]),
            future_value_2=int(column[8]),
            future_value_3=int(column[9]),
            future_value_4=int(column[10]),
            future_value_5=int(column[11]),
            future_value_6=int(column[12]),
        )
    context = {}
    return render(request, template, context)