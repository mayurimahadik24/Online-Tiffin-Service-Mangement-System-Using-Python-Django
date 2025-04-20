from django.shortcuts import redirect, render

def match(request):
    page='match'
    if request.method == 'POST':
      login = request.POST.get('login')
    
        
    context = {'page': page}
    return render(request, 'homepage/login.html', context)

def notmatch(request):
    page='notmatch'
    context = {'page': page}
    return render(request, 'pincode_search/notmatch.html', context)


def pincode_search(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode')
        
        # List of valid pincodes
        valid_pincodes = ['402107', '400007', '402123']
        
        # Check if the entered pincode is in the list of valid pincodes
        if pincode in valid_pincodes:
            return render(request, 'pincode_search/match.html')
        else:
            return render(request, 'pincode_search/notmatch.html')
            
    else:
        return render(request, 'pincode_search/pincode_search.html')

def login(request):
    page='login'
    
    context = {'page': page}
    return render(request, 'homepage/login.html', context)




    

# Create your views here.
