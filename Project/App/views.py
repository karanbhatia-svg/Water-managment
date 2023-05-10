from django.shortcuts import render
import math
# Create your views here.
def form(request):

    return render(request, 'App/Frontpage.html')

def calculate(request):
    ratio = '0:0'
    if request.method == 'POST':
        category = request.POST.get('category')
        ratio = request.POST.get('ratio')
        guest = request.POST.get('guest', 0)

    # parse ratio string into two integers
    corporation_ratio, borewell_ratio = map(int, ratio.split(":"))
    # calculate allotted water based on category
    if category == "900":
        allotted_water = 900
    elif category == "1500":
        allotted_water = 1500

    additional_consumption = int(guest) * 10 * 30
    total_water = allotted_water + additional_consumption
    total_water = math.floor(total_water)
    borewell_water = allotted_water * borewell_ratio / (corporation_ratio + borewell_ratio)
    corporation_water = allotted_water * corporation_ratio / (corporation_ratio + borewell_ratio)
    # calculate water bill based on consumption and rates
    corporation_bill = corporation_water * 1
    borewell_bill = borewell_water * 1.5

    if additional_consumption <= 500:
        tanker_bill = additional_consumption * 2
    elif additional_consumption <= 1500:
        tanker_bill = 500 * 2 + (additional_consumption - 500) * 3
    elif additional_consumption <= 3000:
        tanker_bill = 500 * 2 + 1000 * 3 + (additional_consumption - 1500) * 5
    else:
        tanker_bill = 500 * 2 + 1000 * 3 + 1500 * 5 + (additional_consumption - 3000) * 8

    total_bill  = corporation_bill + borewell_bill + tanker_bill
    total_bill = math.floor(total_bill)
    context = {'total_bill': total_bill,'total_water':total_water,'corporation_bill':corporation_bill,'borewell_bill':borewell_bill,'guest':guest,'tanker_bill':tanker_bill,'corporation_ratio':corporation_ratio,
               'additional_consumption':allotted_water,'additional_consumption':additional_consumption,'borewell_ratio':borewell_ratio}
    return render (request, 'App/answers.html', context)