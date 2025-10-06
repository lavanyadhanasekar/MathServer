# Ex.05 Design a Website for Server Side Processing
## Date:06.10.2025

## AIM:
 To design a website to calculate the Body Mass Index(BMI) in the server side.

## FORMULA:
BMI= w/h<sup>2</sup>
<br> BMI --> Body Mass Index 
<br> W --> Weight
<br> H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
myapp.html

<html> 
<head> 
<title>BMI</title> 
<style>
        body{
          background-color: green;
          border-top: 20;
        }
        .m{
          background-color:greenyellow;
          border-style: dotted;
          margin-top: 150px;
          margin-left: 500px;
          margin-right: 500px;
          
        }
            .main{
                font-size: 250%;
                text-align: center;
                background-color: greenyellow;
                 margin-left: 50px;
                  margin-right: 50px;
                  padding: 50px;
                  
                  
            }
            .a{
                font-size: 150%;
                text-align: center;
                background-color: goldenrod;
                 margin-left: 50px;
                  margin-right: 50px;
                
                 
            }
            form{
              text-align: center;
              background-color: yellow;
               margin-left: 50px;
             margin-right: 50px;
             padding: 50px;
            }
           
        </style>
</head> 

    <center>
    <h1>lavanya D(25016895)</h1>
<div class="edge"> 
<div class="box"> 
<h1>BMI</h1> 
<form method="POST">
{%csrf_token %}
<div class="formelt"> 
height:<input type="text" name="height" value="{{h}}"></input>(in m)<br/> 
</div> 
<div class="formelt"> 
weight:<input type="text" name="weight" value="{{w}}"></input>(in kg)<br/> 
</div> 
<div class="formelt"> 
<input type="submit" value="Calculate"></input><br/> 
</div> 
<div class="formelt"> 
BMI:<input type="text" name="BMI" value="{{BMI}}"></input>kg/m<sup>2</sup><br/> 
</div>
</form>
</div>
</div> 
</body>

views.py

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

urls.py
from django.contrib import admin 
from django.urls import path 
from myapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('BMI/',views.BMI,name="BMI"),
    path('',views.BMI,name="BMI")
]

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (48).png>)

## HOMEPAGE:
![alt text](<Screenshot (46).png>)

## RESULT:
The program for performing server side processing is completed successfully.
