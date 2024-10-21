from django.shortcuts import render, get_object_or_404
import pdb

# Create your views here.
def pallet_detail(request, serial_number):
    print("Pallet detail view called") 
    pdb.set_trace()
    pallet = get_object_or_404(IncomingPallet, serial_number = serial_number)
    batteries = pallet.batteries.all()
    battery_count = batteries.count()
    return render(request, 'templates/pallet_details.html', {'pallet': pallet, 'batteries': batteries,
                                                   'battery_count':battery_count})