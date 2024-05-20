from django.db import models

class counseling_schedule(models.Model):
    counselingID = models.CharField(primary_key=True, max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    teachers = [
        ('teacher 1','Teacher 1'),
        ('teacher 2','Teacher 2'),
        ('teacher 3','Teacher 3'),
        ('teacher 4','Teacher 4'),
    ]
    counselor_teacher = models.CharField(max_length=255, choices=teachers)
    scheduled_datetime = models.DateTimeField()
    status = models.BooleanField(default=False)

class IndividualProfileBasicInfo(models.Model):

    studentPhoto = models.FileField(upload_to='media/studentPhoto')
    familyName = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    middleName = models.CharField(max_length=255)
    nickName = models.CharField(max_length=255)
    courseyearsection = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    studentId = models.IntegerField()
    dateFilled = models.DateField()

    studentTypeChoices = [
        ('newStudent','New Student'),
        ('returnee','Returnee'),
        ('shifter','Shifter'),
        ('transferee','Transferee'),
        ('alspasses','ALS Passer'),
        ('foreignstudent','Foreign Student'),
    ]

    studentType = models.CharField(max_length=30, choices=studentTypeChoices)

    #Only need if student is new student

    curriculumtypeChoices = [
        ('oldsecondary','Old Secondary Curriculum Graduate'),
        ('seniorhigh','Senior High School Graduate'),
    ]

    curriculumtype = models.CharField(max_length=50, choices=curriculumtypeChoices, default='')

    track = models.CharField(max_length=255, default='') #Will only be used if curriculumtype is senior high

    age = models.IntegerField()
    religion = models.CharField(max_length=255)
    height = models.DecimalField(max_digits=10,decimal_places=2)
    weight = models.DecimalField(max_digits=10,decimal_places=2)
    birthOrderAmongSiblings = models.CharField(max_length=10)

    sexChoices = [
        ('male','Male'),
        ('female','Female'),
    ]
    sex = models.CharField(max_length=7, choices=sexChoices)

    sexualOrientationChoices = [
        ('heterosexual','Heterosexual'),
        ('gay','Gay'),
        ('lesbian','Lesbian'),
        ('others','Others'),
    ]

    sexualOrientation = models.CharField(max_length=15, choices=sexualOrientationChoices)

    civilStatus = models.CharField(max_length=255)
    citizenship = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    placeOfBirth = models.CharField(max_length=255)
    currentAddress = models.CharField(max_length=255)
    permanentAddress = models.CharField(max_length=255)
    landlineNo = models.CharField(max_length=255)
    mobileNo = models.CharField(max_length=255)
    email = models.EmailField()
    languagesDialectsSpokenAtHome = models.CharField(max_length=255)
    languagesDialectsMostFluentIn = models.CharField(max_length=255)

    livingWithChoices = [
        ('parents','Parents'),
        ('fatheronly','Father Only'),
        ('motheronly','Mother Only'),
        ('spouse', 'Spouse'),
        ('relative', 'Relative'),
        ('employer', 'Employer'),
        ('others','Others'),
    ]

    livingWith = models.CharField(max_length=15, choices=livingWithChoices)
    
    livingWithRelative = models.CharField(max_length=255,default='')# Will be used if living with relative is true
    livingWithOthers = models.CharField(max_length=255,default='') # Will be used if living with others is true

    placeOfLivingChoices = [
        ('dormitory','Dormitory'),
        ('boardinghouse','Boarding House'),
        ('ownhouse', 'Own House'),
        ('others',' Others')
    ]
    placeOfLiving = models.CharField(max_length=20, choices=placeOfLivingChoices)
    placeOfLivingOthers = models.CharField(max_length=255,default='') #Will be used if place of living is other

    fatherName = models.CharField(max_length=255)
    motherName = models.CharField(max_length=255)
    fatherDateOfBirth = models.DateField()
    motherDateOfBirth = models.DateField()
    fatherAddress = models.CharField(max_length=255)
    motherAddress = models.CharField(max_length=255)
    fatherLandline = models.CharField(max_length=255)
    motherLandLine = models.CharField(max_length=255)
    fatherMobilePhone = models.CharField(max_length=255)
    motherMobilePhone = models.CharField(max_length=255)

    educationLevelChoices = [
        ('elementarylevel','Elementary Level'),
        ('elementarygraduate','Elementary Graduate'),
        ('highschoollevel','High School Level'),
        ('highschoolgraduate','High School Graduate'),
        ('collegelevel','College Level'),
        ('collegegraduate','College Graduate'),
        ('postgraduate', 'Post Graduate'),
    ]

    fatherEducationLevel = models.CharField(max_length=30, choices=educationLevelChoices)
    motherEducationLevel = models.CharField(max_length=30, choices=educationLevelChoices)

    fatherCTU = models.BooleanField()
    motherCTU = models.BooleanField()
    sourceOfIncomeChoices = [
        ('onlyfatherworks','Only father works'),
        ('onlymotherworks','Only mother works'),
        ('bothparentswork','Both parents work'),
        ('siblingswork', 'Sibling(s) work'),
        ('familyownedbusiness', 'Family owned business'),
        ('relatives','Relative(s)'),
    ]
    sourceOfIncome = models.CharField(max_length=30, choices=sourceOfIncomeChoices)
    sourceOfIncomeFamilyBusiness = models.CharField(max_length=255,default='') #Will be used if family business is picked
    sourceOfIncomeRelative = models.CharField(max_length=255,default='') #Will be used if relative is picked

    parentsOccupationChoices = [
        ('agriculture','Agriculture, Food and Natural Resources'),
        ('architecture', 'Architecture, Design and Construction'),
        ('businessmanagement','Business Management, Marketing and Sales'),
        ('clerical','Clerical and Customer Service'),
        ('education','Education and Training'),
        ('health', 'Health'),
        ('law', 'Law, Public Safety Corrections and Security'),
        ('manufacturing','Manufacturing'),
        ('science','Science, Technology, Engineering'),
        ('maintenance','Maintenance and Services'),
        ('transportation','Transportation, Distribution and Logistics'),
        ('unemployed','Unemployed'),
        ('others', 'Others'),
    ]

    fatherOccupation = models.CharField(max_length=255, choices=parentsOccupationChoices)
    fatherOtherOccupation = models.CharField(max_length=255, default='')

    motherOccupation = models.CharField(max_length=255, choices=parentsOccupationChoices)
    motherOtherOccupation = models.CharField(max_length=255,default='')

    familyEarningInaMonthChoices = [
        ('below1000','below P 1,000'),
        ('1000-5000','P 1,000 - P 5,000'),
        ('11000-15000','P 11,000 - P 15,000'),
        ('16000-20000','P 16,000 - P 20,000'),
        ('21000-25000','P 21,000 - P 25,000'),
        ('26000-30000','P 26,000 - P 30,000'),
        ('31000-40000','P 31,000 - P 40,000'),
        ('41000andabove','P 41,000 and above'),
    ]

    familyEarningInaMonth = models.CharField(max_length=30, choices=familyEarningInaMonthChoices)
    
    parentStatusChoices = [
        ('together&married','Living together and legally married'),
        ('together&notmarried','Living together and not legally married'),
        ('marriedbutseparate','Legally married but living separetely'),
        ('mohterofw','Mother is OFW'),
        ('fatherofw','Father is OFW'),
        ('fatherwanother','Father w/ Another Partner'),
        ('motherwanother','Mother w/ Another Partner'),
    ]

    parentStatus = models.CharField(max_length=50, choices=parentStatusChoices)

    siblingsName = models.JSONField()
    siblingsAge = models.JSONField()
    siblingsSchoolWork = models.JSONField()
    
    #Contact persons

    personInCaseofEmergency = models.CharField(max_length=255)
    personInCaseofEmergencyRelationship = models.CharField(max_length=255)
    personInCaseofEmergencyAddress = models.CharField(max_length=255)
    personInCaseofEmergencyLandline = models.CharField(max_length=255)
    personInCaseofEmergencyMobileNo = models.CharField(max_length=255)

    # Healh Data

    disabilies = models.CharField(max_length=255)
    allergies = models.CharField(max_length=255)

    bloodTypeChoices = [
        ('O-','O negative'),
        ('O+','O positive'),
        ('A-','A negative'),
        ('A+','A positive'),
        ('B-','B negative'),
        ('B+','B possitive'),
        ('AB-','AB negative'),
        ('AB+','AB positive'),
        ('unknown','Unknown')
    ]
    bloodType = models.CharField(max_length=10, choices=bloodTypeChoices)

    #Education Background

    elementaryName = models.CharField(max_length=255)
    elementaryType = models.BooleanField()
    elementaryAwardsRecieved = models.CharField(max_length=255)
    elementaryYearGraduated = models.IntegerField()

    seniorHighSchoolName = models.CharField(max_length=255)
    seniorHighSchoolType = models.BooleanField()
    seniorHighSchoolAwardsRecieved = models.CharField(max_length=255)
    seniorHighSchoolYearGraduated = models.IntegerField()

    collegeName = models.CharField(max_length=255)
    collegeAwardsRecieved = models.CharField(max_length=255)
    collegeYearGraduated = models.IntegerField()


    schoolLeaver = models.BooleanField()
    schoolLeaverWhy = models.CharField(max_length=255) #If school leaver is yes
    lastEducationAttainment = models.CharField(max_length=255)

    finaciallySupportingChoices = [
        ('parents','Parents'),
        ('spouse','Spouse'),
        ('relatives','Relatives'),
        ('selfsupporting','Self-supporting'),
        ('scholarship','Scholarship'),
    ]

    finaciallySupporting = models.CharField(max_length=20, choices=finaciallySupportingChoices)

    typeOfScholarshipChoices = [
        ('private',' Scholarship by private institution'),
        ('government','Government Scholarship'),
        ('organizations',' Scholarships granted by organizations within CTU'),
    ]

    typeOfScholarship = models.CharField(max_length=100,  choices=typeOfScholarshipChoices, default='')
    specifyScholarship = models.CharField(max_length=255, default='')
    
    # Membership in organizations

    nameOfOrganization = models.JSONField()
    inOutSchool = models.JSONField()
    positionTitle = models.JSONField()
    inclusiveYears = models.JSONField()
    
    # Unique Features

    specialSkill = models.CharField(max_length=255)
    goals = models.CharField(max_length=255)
    presentConcerns = models.CharField(max_length=255)

    # Students 

    describeYouBest = models.JSONField()
    describeYouBestOther = models.CharField(max_length=255, default='')

    # School/Career-related

    decisionForTheCourseChoices = [
        ('self','Self'),
        ('parents','Parent(s)'),
        ('brothersister','Brother/Sister'),
        ('sponsorsscholarship','Sponsors/Scholarship'),
        ('relatives','Relatives'),
        ('friends','Friends'),
    ]

    decisionForTheCourse = models.CharField(max_length=40, choices=decisionForTheCourseChoices)
    specifyTheDecision = models.CharField(max_length=255)
    doYouPlanToWork = models.BooleanField()
    specifyIfNo = models.CharField(max_length=255)
    possibleFactors = models.CharField(max_length=255)

class TestArray(models.Model):
    myarray = models.JSONField()

class FileUploadTest(models.Model):
    file = models.FileField()