from main.models import AbstractPerson, Employee, Passport, WorkProject, Membership, Client, VIPClient
from datetime import date

aika = Employee.objects.create(name="Aikanysh", birth_date = date(1988, 8, 25), work_position="backend_developer", experience = date(2011, 9,1))
tahir = Employee.objects.create(name="Tahir", birth_date = date(2000, 4, 20), work_position="video editor", experience=date(2020, 1, 1))
salavat = Employee.objects.create(name="Salavat", birth_date = date(2001, 6, 15), position="developer", experience=date(1999, 10, 15))

p1 = Passport.objects.create(employee=aika, inn="F12736464", id_card="PA737474")
p2 = Passport.objects.create(employee=tahir, inn="M83837373", id_card="PA733757")
p3 = Passport.objects.create(employee=salavat, inn="M47563894", id_card="PA583958")

p3 = Passport.objects.get(id=3)
p3.delete()

e3 = Employee.objects.get(id=3)
e3.delete()

codify = WorkProject.objects.create(project_name = "Codify")
codify.members.set([aika, tahir, salavat], through_defaults={'date_joined':date(2022, 4, 5)})

elya = Client.objects.create(name="Elmira", birth_date=date(1985, 1, 1), address = "Bishkek", phone_number = 564738395)
dolat = Client.objects.create(name="Dolatbek", birth_date=date(2002, 5, 5), address = "Bishkek", phone_number = 34757583)
kamila = Client.objects.create(name="Kamila", birth_date=date(1995, 10, 11), address = "Osh", phone_number = 8574638383)

daniyar = VIPClient.objects.create(name="Daniyar", birth_date=date(1992, 8, 9), address = "Bishkek", phone_number = 84847575, vip_status_start=date(2018, 1, 1), donation_amount=1000)

all_employees = Employee.objects.all()
print(all_employees)
employees_with_passports = all_employees.filter(Passport__inn__isnull = False, Passport__card_id__isnull = False )
print(employees_with_passports)
all_work_projects = WorkProject.objects.all()
print(all_work_projects)
target_employee = WorkProject.objects.get(Employee.name == "Aikanysh")
print(target_employee)

