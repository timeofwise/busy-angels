import csv, io, django, os
from django.shortcuts import render
from django.contrib import messages
from rich.models import *
import pandas as pd
from django.urls import reverse
from django.http import HttpResponseRedirect
import logging
from .forms import EventsForm

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
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Asset.objects.update_or_create(
            """
                date=column[0],
                pv1=int(column[1]),
                pv2=int(column[2]),
                pv3=int(column[3]),
                pv4=int(column[4]),
                pv5=int(column[5]),
                pv6=int(column[6]),
                fv1=int(column[7]),
                fv2=int(column[8]),
                fv3=int(column[9]),
                fv4=int(column[10]),
                fv5=int(column[11]),
                fv6=int(column[12]),
                """
            )
        context = {}
        return render(request, template, context)

def ReadCSV(request):
    df = pd.read_csv('assets.csv', sep=',')

    row_iter = df.iterrows()
    objs = [
        Asset(
        """
            date=row['date'],
            pv1=row['pv1'],
            pv2=row['pv2'],
            pv3=row['pv3'],
            pv4=row['pv4'],
            pv5=row['pv5'],
            pv6=row['pv6'],
            fv1=row['fv1'],
            fv2=row['fv2'],
            fv3=row['fv3'],
            fv4=row['fv4'],
            fv5=row['fv5'],
            fv6=row['fv6'],
            """
        )

        for index, row in row_iter
    ]

    Asset.objects.bulk_create(objs)

    return render(request, 'testcsv/read.html')


def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "testcsv/asset_upload.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("upload_csv"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("upload_csv"))

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        #loop over the lines and save them in db. If error , store as string and then display
        for line in lines:
            fields = line.split(",")
            data_dict = {}
            data_dict["date"] = fields[0]
            data_dict["pv1"] = fields[1]
            data_dict["pv2"] = fields[2]
            data_dict["pv3"] = fields[3]
            data_dict["pv4"] = fields[4]
            data_dict["pv5"] = fields[5]
            data_dict["pv6"] = fields[6]
            data_dict["pv7"] = fields[7]
            data_dict["pv8"] = fields[8]
            data_dict["pv9"] = fields[9]
            data_dict["pv10"] = fields[10]
            data_dict["fv1"] = fields[11]
            data_dict["fv2"] = fields[12]
            data_dict["fv3"] = fields[13]
            data_dict["fv4"] = fields[14]
            data_dict["fv5"] = fields[15]
            data_dict["fv6"] = fields[16]
            data_dict["fv7"] = fields[17]
            data_dict["fv8"] = fields[18]
            data_dict["fv9"] = fields[19]
            data_dict["fv10"] = fields[20]
            try:
                form = EventsForm(data_dict)
                if form.is_valid():
                    form.save()
                else:
                    logging.getLogger("error_logger").error(form.errors.as_json())
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))
                pass

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        messages.error(request,"Unable to upload file. "+repr(e))

    return HttpResponseRedirect(reverse("upload_csv"))