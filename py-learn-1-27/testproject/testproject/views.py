from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def home(request):
    data={
        'dataTitle':"Test P Home",
        'bodyData':"Hell o I am the body.\n What did you learn yesterday?\n",
        'courseList': ["PHP","Python","Javascript"],
        'numbers':[10,20,30,40,50],
        'student_details': [
            {'name':"ABC",'phone': 91458},
            {'name':"DEF",'phone': 17254},
        ]
    }
    return render(request,'home.html',data)

def aboutUS(request):
    
    return render(request,'about.html')

def contactUS(request):
    user = {}
    
    try:
        if request.method == "GET":
        # 3 ways to receive value from input field 
            name_value = request.GET['name']
            password_value = request.GET.get('password')
            roll_value = int(request.GET['roll'])

            user['name'] = name_value
            user['password'] = password_value
            user['roll'] = roll_value

            print(user,"User Dictionary",{'result_data':user})
            # return render(request,'contactus.html',{'result_data':user})  # render HTML page
            
            return HttpResponseRedirect(f'/about/?key1=one&key2=two')  # redirect to route '/about' page

        elif request.method == "POST":
            village_value = request.POST['village']
            country_value = request.POST['country']
            
            address = {
                'village_data': village_value,
                'country_data': country_value
            }
            
            return render(request,'contactus.html',{'result_post_data': address})
        else:
            return render(request,'contactus.html')

    except BaseException as err:
        print(str(err)," ->PRINTED ERROR<-")
        pass
    finally:
        # print("Finished block")
        pass

    return render(request,'contactus.html')
    
    

def Courses(para):
    return HttpResponse("Welcome to Courses Page")

def courseDetails(para,courseID):
    print(courseID)
    return HttpResponse(f'Showing the detail of pourse number: <h1> {courseID}</h1>')

def services(request):
    return render(request,'services.html')