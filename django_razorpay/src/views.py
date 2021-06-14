from django.shortcuts import render
from .forms import CoralForm
from .models import Corals
import razorpay
def payment(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact_no=request.POST.get('contact_no')
        address_1=request.POST.get('address_1')
        address_2=request.POST.get('address_2')
        pincode=request.POST.get('pincode')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        package=request.POST.get('package')
        if package=='1':
            type="Single Coral"
            set="For Individual"
            amount=600000
        elif package=='2':
            type="Single Coral"
            set="For Group of 2"
            amount=300000
        elif package=='3':
            type="Single Coral"
            set="For Group of 3"
            amount=200000
        elif package=='4':
            type="Single Coral"
            set="For Group of 4"
            amount=150000
        elif package=='5':
            type="Coral Tile"
            set="For Individual"
            amount=2200000
        elif package=='6':
            type="Coral Tile"
            set="For Group of 2"
            amount=1100000
        elif package=='7':
            type="Coral Tile"
            set="For Group of 3"
            amount=750000
        elif package=='8':
            type="Coral Tile"
            set="For Group of 4"
            amount=600000
        elif package=='9':
            type="Coral Tile"
            set="For Group of 6"
            amount=400000
        elif package=='10':
            type="Coral Tile"
            set="For Group of 8"
            amount=300000
        elif package=='11':
            type="Coral Bed"
            set="For Individual"
            amount=24000000
        elif package=='12':
            type="Coral Bed"
            set="For Company"
            amount=25000000
        else:
            form=CoralForm()
        
        client=razorpay.Client(auth=('rzp_test_hkacggmdlTcwlO', '3mBefpmZLch75OiXGsyfDDpF'))
        response_payment=client.order.create(
            dict(amount=amount, currency = 'INR')
        )
        order_id=response_payment['id']
        order_status=response_payment['status']
        form=CoralForm(request.POST)
        print(form.is_valid())
        if form.is_valid() and order_status=='created':
            corals = form.save(commit=False)
            corals.type=type
            corals.set=set
            corals.amount = amount
            corals.order_id=order_id
            corals.save()
            response_payment['name']=name
            return render (request, 'index.html', {'form': form, 'payment': response_payment})
        print(response_payment)

    form=CoralForm()
    return render(request, 'index.html', {'form': form})

def payment_status(request):
    response=request.POST
    print(response)
    return render(request, 'payment_status.html')
