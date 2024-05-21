import csv
from datetime import datetime
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from SAO_WebApp.forms import CounselingSchedulerForm, IndividualProfileForm, FileUpload, UploadFileForm
from .models import TestArray, studentInfo, counseling_schedule
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.template.defaulttags import register

class testing:
  name = "Testing rani"
  course = "Bachelor of Science major in sleeping."
  date = "Jan 1 2025"
  type = "Test"
  

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            
            for row in reader:
                studentInfo.objects.create(
                    studID=row['studID'],
                    lrn=row['lrn'],
                    lastname=row['lastname'],
                    firstname=row['firstname'],
                    middlename=row['middlename'],
                    degree=row['degree'],
                    yearlvl=row['yearlvl'],
                    sex=row['sex'],
                    emailadd=row['emailadd'],
                    contact=row['contact']
                )
            
            messages.success(request, 'File uploaded and data imported successfully')
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def home(request):
	return render(request, 'main.html',{})
def counseling_app(request):
    if request.method == 'POST':
        form = CounselingSchedulerForm(request.POST)
        if form.is_valid():
            current_datetime = timezone.now()
            student_id = request.POST.get('student_id_val')
            
            # Get the studentInfo instance corresponding to the provided student ID
            student = get_object_or_404(studentInfo, studID=student_id)
            
            # Check for ongoing schedules
            ongoing_schedule = counseling_schedule.objects.filter(
                studentID=student, 
                scheduled_date__gte=current_datetime.date()
            ).first()
            
            if ongoing_schedule and not ongoing_schedule.status == 'declined':
                time = {
					'8-9': '8:00 AM - 9:00 AM',
					'9-10': '9:00 AM - 10:00 AM',
					'10-11': '10:00 AM-11:00 AM',
					'11-12': '11:00 AM -12:00 PM',
					'1-2':'1:00 PM - 2:00 PM',
					'2-3':'2:00 PM - 3:00 PM',
					'3-4':'3:00 PM - 4:00 PM',
					'4-5':'4:00 PM - 5:00 PM'
				}

                scheduled_date = ongoing_schedule.scheduled_date.strftime('%B %d, %Y')
                scheduled_time = time[f'{ongoing_schedule.scheduled_time}']
                messages.error(request, f'You still have an ongoing schedule on {scheduled_date} on {scheduled_time}.')
                return redirect('Counseling App With Scheduler')
            
            formatted_date = current_datetime.strftime('%Y-%m-%d')
            counseling = form.save(commit=False)
            counseling.dateRecieved = formatted_date
            counseling.studentID = student  # Assign the studentInfo instance
            counseling.save()
            
            messages.success(request, 'Your request has been successfully added. An email will be sent if it is accepted.')
            return redirect('Counseling App With Scheduler')
    else:
        form = CounselingSchedulerForm()
    
    context = {'form': form}
    return render(request, 'counseling_app.html', context)

def counseling_app_admin_view(request):
    meeting_requests = counseling_schedule.objects.select_related('studentID').order_by('-dateRecieved')

    time = {
        '8-9': '8:00 AM - 9:00 AM',
        '9-10': '9:00 AM - 10:00 AM',
        '10-11': '10:00 AM-11:00 AM',
        '11-12': '11:00 AM -12:00 PM',
        '1-2': '1:00 PM - 2:00 PM',
        '2-3': '2:00 PM - 3:00 PM',
        '3-4': '3:00 PM - 4:00 PM',
        '4-5': '4:00 PM - 5:00 PM'
    }

    context = {
        'meeting_requests': meeting_requests,
        'time': time,
    }
    return render(request, 'counseling_app_admin_view.html', context)
@register.filter
def get_formatted_time(dictionary, key):
    return dictionary.get(key)

def good_moral(request):
	value = testing
	return render(request, 'goodmoral.html',{'value': value})
def individualProfile(request):
	if request.method == 'POST':

		form = IndividualProfileForm(request.POST, request.FILES)
		if form.is_valid():
			siblings_name = request.POST.getlist('name[]')
			siblings_age = request.POST.getlist('age[]')
			siblings_placework = request.POST.getlist('placework[]')
			
			name_of_organization = request.POST.getlist('name_of_organization[]')
			in_out_school = request.POST.getlist('inoutSchool[]')
			position = request.POST.getlist('position[]')
			inclusive_years = request.POST.getlist('inclusiveyears[]')

			describeYouBest_values = [
				'Friendly', 'Self-Confident', 'Calm', 'Quick-Tempered', 'Feels Inferior',
				'Unhappy', 'Easily Bored', 'Talented', 'Withdrawn', 'Conscientious',
				'Talkative', 'Cheerful', 'Moody', 'Easily Exhausted', 'Lazy',
				'Sensitive', 'Poor health', 'Reserved', 'Quiet', 'Independent',
				'Depressed', 'Suspicious', 'Irritable', 'Stubborn', 'Thoughtful',
				'Lovable', 'Jealous', 'Shy', 'Sarcastic', 'Tactful',
				'Pessimistic', 'Submissive', 'Optimistic', 'Happy-go-lucky', 'Goal-oriented'
			]

			describeYouBest_checked = request.POST.getlist('describeYouBest[]')

			# Create a dictionary to store the state (checked or not) of each value
			describeYouBest_state = {value: value in describeYouBest_checked for value in describeYouBest_values}

			new_form = form.save(commit=False)
			new_form.siblingsName = siblings_name
			new_form.siblingsAge = siblings_age
			new_form.siblingsSchoolWork = siblings_placework

			# Assuming the other fields are also JSONFields
			new_form.nameOfOrganization = name_of_organization
			new_form.inOutSchool = in_out_school
			new_form.positionTitle = position
			new_form.inclusiveYears = inclusive_years
			new_form.describeYouBest = describeYouBest_state

			new_form.save()
			return redirect('Good Moral')
	else:
		form = IndividualProfileForm()
	context = {'form': form}
	return render(request, 'individual_profile.html',context)
def test(request):
	if request.method == 'POST':
		form = FileUpload(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('Test')
	else:
		form = FileUpload()
	return render(request, 'test.html',{'form':form})

def search_student_info(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number', '')
        try:
            student = studentInfo.objects.get(studID=id_number)
            response = {
				'student_id': student.studID,
				'name': f"{student.lastname}, {student.firstname}",
				'program_and_section': f"{student.degree} {student.yearlvl}",
				'contact_number': student.contact,
				'email': student.emailadd
        	}
            return JsonResponse(response)
        except studentInfo.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)

def check_date_time_validity(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        try:
            # Convert the selected date string to a Python datetime object
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            # Query the counseling_schedule model for entries with the same scheduled_date
            counseling_schedules = counseling_schedule.objects.filter(scheduled_date=selected_date)
            # You can now do something with the counseling_schedules queryset, like serialize it to JSON
            serialized_data = [{'scheduled_time': schedule.scheduled_time, 'status': schedule.status} for schedule in counseling_schedules]
            return JsonResponse({'counseling_schedules': serialized_data})
        except ValueError:
            # Handle invalid date format
            return JsonResponse({'error': 'Invalid date format'}, status=400)