import csv
from datetime import datetime
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from SAO_WebApp.forms import CounselingSchedulerForm, IndividualProfileForm, FileUpload, UploadFileForm, ExitInterviewForm, OjtAssessmentForm
from .models import TestArray, studentInfo, counseling_schedule, exit_interview_db, OjtAssessment
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.template.defaulttags import register
from django.core.mail import send_mail
from django.http import HttpResponse

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
            
            if ongoing_schedule and not ongoing_schedule.status == 'Declined' and not ongoing_schedule.status == 'Expired':
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
				'program':student.degree,
                'year':student.yearlvl,
				'contact_number': student.contact,
				'email': student.emailadd
        	}
            return JsonResponse(response)
        except studentInfo.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
def search_ojt_assessment_request(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number', '')
        students = OjtAssessment.objects.filter(studentID__studID=id_number)
        if students.exists():
            response = []
            for student in students:
                response.append({
                    'date_received': student.dateRecieved,
                    'student_id': student.studentID.studID,
                    'name': f"{student.studentID.lastname}, {student.studentID.firstname}",
                    'schoolyear': student.schoolYear,
                    'status': student.status
                })
            return JsonResponse(response, safe=False)  # safe=False to allow serialization of non-dict objects
        else:
            return JsonResponse({'error': 'Student not found'}, status=404)    
def search_exit_interview_request(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number', '')
        students = exit_interview_db.objects.filter(studentID__studID=id_number)
        if students.exists():
            response = []
            for student in students:
                response.append({
                    'date_received': student.dateRecieved,
                    'student_id': student.studentID.studID,
                    'name': f"{student.studentID.lastname}, {student.studentID.firstname}",
                    'status': student.status
                })
            return JsonResponse(response, safe=False)  # safe=False to allow serialization of non-dict objects
        else:
            return JsonResponse({'error': 'Student not found'}, status=404)    
def get_ojt_assessment_data(request):
    if request.method == 'POST':
        recordID = request.POST.get('OjtRequestID','')
        try:
            student = OjtAssessment.objects.get(OjtRequestID=recordID)
            if student.studentID.middlename == 'NONE':
                middleInit = ''  # Set to empty string if text is 'NONE'
            else:
                middleInit = student.studentID.middlename[0]
            dateAccepted =student.dateAccepted
            formatted_dateAccepeted = dateAccepted.strftime("%B %d, %Y")
            response = {
				'name': f"{student.studentID.firstname.title()} {middleInit} {student.studentID.lastname.title()}",
                'schoolyear': student.schoolYear,
				'program':student.studentID.degree,
                'date_accepted':formatted_dateAccepeted,    
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
def check_date_time_validity_for_exit(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        try:
            # Convert the selected date string to a Python datetime object
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            # Query the counseling_schedule model for entries with the same scheduled_date
            counseling_schedules = exit_interview_db.objects.filter(scheduled_date=selected_date)
            # You can now do something with the counseling_schedules queryset, like serialize it to JSON
            serialized_data = [{'scheduled_time': schedule.scheduled_time, 'status': schedule.status} for schedule in counseling_schedules]
            return JsonResponse({'counseling_schedules': serialized_data})
        except ValueError:
            # Handle invalid date format
            return JsonResponse({'error': 'Invalid date format'}, status=400)

def exit_interview(request):
    if request.method == 'POST':
        form = ExitInterviewForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            fields = [
                'academically_too_challenging',
                'not_academically_challenging_enough',
                'does_not_offer_my_academic_major',
                'size_of_the_school',
                'location_of_the_school',
                'negative_social_campus_climate',
                'residence_hall_environment_not_positive',
                'social_environment_not_diverse_enough',
                'not_enough_campus_activities',
                'needed_more_academic_support',
                'financial',
                'medical_injury',
            ]
            values = []
            for field in fields:
                value = request.POST.get(field, '')
                if value == '':
                    values.append('')
                else:
                    values.append(value)
            student_id = request.POST.get('studentID')
            
            # Get the studentInfo instance corresponding to the provided student ID
            student = get_object_or_404(studentInfo, studID=student_id)

            ongoing_request = exit_interview_db.objects.filter(
                studentID=student,
                status = 'Pending' 
            ).first()
            
            if ongoing_request:
                messages.error(request, f'You still have an pending request.')
                return redirect('Exit Interview')
            
            current_date = timezone.localtime(timezone.now())
            date_number = current_date.strftime("%m%d%y")  # Format date as MMDDYY

            # Sum the digits of the student ID
            digit_sum = sum(int(digit) for digit in str(student_id))

            # Combine date number and digit sum into a preliminary final number
            preliminary_final_number = f"{date_number}{digit_sum}"

            # Calculate the number of zeros needed to make the length 10 digits
            total_length = 10
            number_of_zeros_needed = total_length - len(preliminary_final_number)

            # Insert zeros between date number and digit sum
            final_number = f"{date_number}{'0' * number_of_zeros_needed}{digit_sum}"
            
            new_form.date = timezone.now()
            new_form.contributedToDecision = values
            new_form.studentID = student
            new_form.dateRecieved = timezone.now()
            new_form.save()
            messages.success(request, 'Your request has been successfully added. An email will be sent if it is accepted.')
            return redirect('Exit Interview')
    else:
         form = ExitInterviewForm()
    return render(request, 'exit_interview.html',{'form': form})
def exit_interview_admin_view(request):
    exit_interview_request = exit_interview_db.objects.select_related('studentID').order_by('-dateRecieved')
    context = {'exit_interview_request': exit_interview_request,}
    return render(request, 'exit_interview_admin.html', context)
def update_exit_interview_status(request):
    if request.method == 'POST':
        requestID = request.POST.get('exitinterviewId', '')
        update_type = request.POST.get('type','')
        if update_type == 'accept':
            obj = get_object_or_404(exit_interview_db, exitinterviewId=requestID)
            obj.status = 'Accepted'
            message = f"Hello {obj.studentID.firstname.title()} {obj.studentID.lastname.title()} your Exit Interview request has been approved."
            email = obj.emailadd
            obj.save()
            send_mail(
                'Exit Interview Request',
                message,
                'notifytest391@gmail.com',  # From email
                [email],  # To email
                fail_silently=False,
            )
            obj.save()
    
            # Optionally, you can return a JSON response indicating success
            return JsonResponse({'message': 'Value updated successfully'})
        elif update_type == 'decline':
            obj = get_object_or_404(exit_interview_db, exitinterviewId=requestID)
            obj.status = 'Declined'
            message = f"Hello {obj.studentID.firstname.title()} {obj.studentID.lastname.title()} your Exit Interview request has been declined."
            email = obj.emailadd
            obj.save()
            send_mail(
                'Exit Interview Request',
                message,
                'notifytest391@gmail.com',  # From email
                [email],  # To email
                fail_silently=False,
            )
            obj.save()
    
            # Optionally, you can return a JSON response indicating success
            return JsonResponse({'message': 'Value updated successfully'})
def delete_exit_interview_status(request):
    if request.method == 'POST':
        requestID = request.POST.get('exitinterviewId', '')
        obj = get_object_or_404(exit_interview_db, exitinterviewId=requestID)
        obj.delete()
        return JsonResponse({'message': 'Value updated successfully'})  
def update_ojt_assessment(request):
    if request.method == 'POST':
        requestID = request.POST.get('OjtRequestID', '')
        update_type = request.POST.get('type','')
        if update_type == 'accept':
            obj = get_object_or_404(OjtAssessment, OjtRequestID=requestID)
            obj.status = 'Accepted'
            obj.dateAccepted = timezone.now()
            message = f"Hello {obj.studentID.firstname.title()} {obj.studentID.lastname.title()} your OJT Assessments/Psychological Issuance request has been approved."
            email = obj.emailadd
            obj.save()
            send_mail(
                'OJT Assessments/Psychological Issuance Request',
                message,
                'notifytest391@gmail.com',  # From email
                [email],  # To email
                fail_silently=False,
            )
    
            # Optionally, you can return a JSON response indicating success
            return JsonResponse({'message': 'Value updated successfully'})
        elif update_type == 'decline':
            obj = get_object_or_404(OjtAssessment, OjtRequestID=requestID)
            obj.status = 'Declined'
            obj.save()
            message = f"Hello {obj.studentID.firstname.title()} {obj.studentID.lastname.title()} your OJT Assessments/Psychological Issuance request has been declined."
            email = obj.emailadd
            send_mail(
                'OJT Assessments/Psychological Issuance Request',
                message,
                'notifytest391@gmail.com',  # From email
                [email],  # To email
                fail_silently=False,
            )
            # Optionally, you can return a JSON response indicating success
            return JsonResponse({'message': 'Value updated successfully'})       
def delete_ojt_assessment(request):
    if request.method == 'POST':
        requestID = request.POST.get('exitinterviewId', '')
        obj = get_object_or_404(OjtAssessment, OjtRequestID=requestID)
        obj.delete()
        return JsonResponse({'message': 'Value updated successfully'})  
def ojt_assessment(request):
    if request.method == 'POST':
        form = OjtAssessmentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            student_id = request.POST.get('student_id_val')
            student = get_object_or_404(studentInfo, studID=student_id)
            ongoing_request = OjtAssessment.objects.filter(
                studentID=student,
                status = 'Pending' 
            ).first()
            
            if ongoing_request:
                messages.error(request, f'You still have an pending request.')
                return redirect('OJT Assessment')

            new_form.studentID = student
            new_form.dateRecieved = timezone.now()
            new_form.save()
            messages.success(request, 'Your request has been successfully added. An email will be sent if it is accepted.')
            return redirect('OJT Assessment')
    else:
        form = OjtAssessmentForm()
    return render(request,'ojt_assessment.html',{'form': form})

def ojt_assessment_admin_view(request):
    ojt_assessment_request = OjtAssessment.objects.select_related('studentID').order_by('-dateRecieved')
    context = {'ojt_assessment_request': ojt_assessment_request,}
    return render(request, 'ojt_assessment_admin.html', context)
