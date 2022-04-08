from main.models import Employee, Passport

e = Employee.objects.first()
p = Passport(employee=e)
p.inn = 'dsadsadsa'

p.save()
