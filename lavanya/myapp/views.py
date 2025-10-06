from django.shortcuts import render
def BMI(request): 
    context={} 
    context['BMI'] = "0" 
    context['h'] = "0" 
    context['w'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        h = request.POST.get('height','0')
        w = request.POST.get('weight','0')
        print('request=',request) 
        print('height=',h) 
        print('weight=',w) 
        BMI = int(w)/((int(h)/100)**2)
        context['BMI'] = BMI 
        context['h'] = l
        context['w'] = b 
        print('BMI=',BMI) 
    return render(request,'myapp/math.html',context)
