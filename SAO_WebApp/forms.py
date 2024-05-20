from django import forms
from SAO_WebApp.models import counseling_schedule, IndividualProfileBasicInfo, FileUploadTest


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class CounselingSchedulerForm(forms.ModelForm):

    teachers = [
        ('teacher 1','Teacher 1'),
        ('teacher 2','Teacher 2'),
        ('teacher 3','Teacher 3'),
        ('teacher 4','Teacher 4'),
    ]
    counselor_teacher = forms.ChoiceField(choices=teachers) 
    scheduled_datetime = forms.DateTimeField(widget=DateTimeInput)   
    reason = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize:none;'}))
    def __init__(self, *args, **kwargs):
        super(CounselingSchedulerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
    class Meta:
        model = counseling_schedule
        fields = '__all__'

class IndividualProfileForm(forms.ModelForm):
    schoolTypeChoices = [
        (True,'Private'),
        (False,'Public'),
    ]
    yes_no =[
        (True,'Yes'),
        (False,'No'),
    ]
    elementaryType = forms.ChoiceField(choices=schoolTypeChoices, widget=forms.RadioSelect)
    seniorHighSchoolType = forms.ChoiceField(choices=schoolTypeChoices, widget=forms.RadioSelect)
    schoolLeaver = forms.ChoiceField(choices=yes_no, widget=forms.RadioSelect)
    fatherCTU = forms.ChoiceField(choices=yes_no, widget=forms.RadioSelect)
    motherCTU = forms.ChoiceField(choices=yes_no, widget=forms.RadioSelect)
    doYouPlanToWork =forms.ChoiceField(choices=yes_no, widget=forms.RadioSelect)

    class Meta:
        model = IndividualProfileBasicInfo
        exclude = ['siblingsName','siblingsAge','siblingsSchoolWork','nameOfOrganization','inOutSchool','positionTitle','inclusiveYears','describeYouBest']
        widgets ={
            'dateFilled': forms.DateInput(attrs={'type':'date'}),
            'dateOfBirth': forms.DateInput(attrs={'type':'date'}),
            'fatherDateOfBirth': forms.DateInput(attrs={'type':'date'}),
            'motherDateOfBirth': forms.DateInput(attrs={'type':'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['elementaryType'].widget.attrs.update({'class': 'side-way'})
        self.fields['seniorHighSchoolType'].widget.attrs.update({'class': 'side-way'})
        self.fields['schoolLeaver'].widget.attrs.update({'class': 'side-way'})
        self.fields['schoolLeaver'].widget.attrs.update({'class': 'side-way'})
        self.fields['fatherCTU'].widget.attrs.update({'class': 'side-way'})
        self.fields['motherCTU'].widget.attrs.update({'class': 'side-way'})
        self.fields['doYouPlanToWork'].widget.attrs.update({'class': 'side-way'})
        self.fields['sourceOfIncomeFamilyBusiness'].widget.attrs.update({'class': 'hidden'})
        self.fields['sourceOfIncomeRelative'].widget.attrs.update({'class': 'hidden'})
        self.fields['curriculumtype'].widget.attrs.update({'class': 'hidden'})

        self.fields['track'].required = False
        self.fields['livingWithRelative'].required = False
        self.fields['livingWithOthers'].required = False
        self.fields['placeOfLivingOthers'].required = False
        self.fields['sourceOfIncomeFamilyBusiness'].required = False
        self.fields['sourceOfIncomeRelative'].required = False
        self.fields['fatherOtherOccupation'].required = False
        self.fields['motherOtherOccupation'].required = False
        self.fields['typeOfScholarship'].required = False
        self.fields['specifyScholarship'].required = False
        self.fields['schoolLeaverWhy'].required = False
        self.fields['specifyIfNo'].required = False
        self.fields['middleName'].required = False
        self.fields['nickName'].required = False
        self.fields['landlineNo'].required = False
        self.fields['fatherLandline'].required = False
        self.fields['motherLandLine'].required = False
        self.fields['personInCaseofEmergency'].required = False
        self.fields['disabilies'].required = False
        self.fields['allergies'].required = False
        self.fields['collegeName'].required = False
        self.fields['collegeAwardsRecieved'].required = False
        self.fields['collegeYearGraduated'].required = False
        self.fields['lastEducationAttainment'].required = False
        self.fields['specifyTheDecision'].required = False
        self.fields['describeYouBestOther'].required = False


class FileUpload(forms.ModelForm):
    class Meta:
        model = FileUploadTest
        fields = '__all__'
        widgets = {
            'file': forms.FileInput(attrs={'accept':'image/*'}),
        }