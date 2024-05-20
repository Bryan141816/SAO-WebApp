import json
from django.shortcuts import render, redirect
from SAO_WebApp.forms import CounselingSchedulerForm, IndividualProfileForm, FileUpload
from .models import TestArray
class testing:
  name = "Testing rani"
  course = "Bachelor of Science major in sleeping."
  date = "Jan 1 2025"
  type = "Test"
  

def home(request):
	return render(request, 'main.html',{})
def counseling_app(request):
	form = CounselingSchedulerForm()
	context = {'form': form}
	return render(request, 'counseling_app.html',context)
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

