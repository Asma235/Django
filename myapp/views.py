# from django.http import HttpResponse, JsonResponse
# # Sample employee data with IDs
# employees = [
#     {
#         "id": 2532,
#         "name": "Asma",
#         "designation": "Software Engineer",
#         "department": "Engineering",
#         "salary": 75000,
#     },
#     {
#         "id": 2533,
#         "name": "Sumair",
#         "designation": "Devops Engineer",
#         "department": "Devops",
#         "salary": 80000,
#     },
   
# ]
# def employee(request):
#     return HttpResponse(employees)

# def get_employee_by_id(request, employee_id):
#     matching_employees = [emp for emp in employees if emp["id"] == int(employee_id)]

#     if matching_employees:
#         return JsonResponse(matching_employees[0])
#     else:
#         return HttpResponse("Employee not found", status=404)






from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # To disable CSRF protection for simplicity
import json

# Sample employee data with IDs
employees = [
    {
        "id": 2532,
        "name": "Asma",
        "designation": "Software Engineer",
        "department": "Engineering",
        "salary": 75000,
    },
    {
        "id": 2533,
        "name": "Sumair",
        "designation": "Devops Engineer",
        "department": "Devops",
        "salary": 80000,
    },
]

@csrf_exempt
def employee(request):
    if request.method == 'GET':
        return JsonResponse(employees, safe=False)
    elif request.method == 'POST':
        try:
            # Parse the JSON data from the POST request
            data = json.loads(request.body)
            
            # Generate a unique ID for the new employee
            new_id = max(employees, key=lambda emp: emp['id'])['id'] + 1
            
            # Add the new employee to the list
            new_employee = {
                "id": new_id,
                "name": data.get("name", ""),
                "designation": data.get("designation", ""),
                "department": data.get("department", ""),
                "salary": data.get("salary", 0),
            }
            employees.append(new_employee)
            
            return JsonResponse(new_employee, status=201)
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=400)

@csrf_exempt
def get_employee_by_id(request, employee_id):
    if request.method == 'GET':
        matching_employees = [emp for emp in employees if emp["id"] == int(employee_id)]

        if matching_employees:
            return JsonResponse(matching_employees[0])
        else:
            return HttpResponse("Employee not found", status=404)
    elif request.method == 'PUT':
        try:
            # Parse the JSON data from the PUT request
            data = json.loads(request.body)
            
            # Find the employee with the given ID and update their details
            for emp in employees:
                if emp['id'] == int(employee_id):
                    emp['name'] = data.get("name", emp['name'])
                    emp['designation'] = data.get("designation", emp['designation'])
                    emp['department'] = data.get("department", emp['department'])
                    emp['salary'] = data.get("salary", emp['salary'])
                    return JsonResponse(emp)
            
            return HttpResponse("Employee not found", status=404)
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=400)
    elif request.method == 'DELETE':
        # Find and remove the employee with the given ID
        for emp in employees:
            if emp['id'] == int(employee_id):
                employees.remove(emp)
                return HttpResponse(status=204)
        
        return HttpResponse("Employee not found", status=404)













