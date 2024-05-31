$(document).ready(function(){
    $('#consent_container').addClass('active');

    $("#agreeCheck").change((event)=>{
        if($('#agreeCheck').is(':checked')){
            $('#proceedBtn').prop('disabled', false);
            $('#proceedBtn').removeClass('disabled');
        }
        else{
            $('#proceedBtn').prop('disabled', true);
            $('#proceedBtn').addClass('disabled');
        }
    });

    $(document).on('click','#proceedBtn' ,function(event){
        event.preventDefault();
        $('#consent_container').removeClass('active');
    });



    $("#addanother").on("click", function(event){
        event.preventDefault();
        let newRow = $(".sibllingsrowTemplate").clone(true);
        newRow.removeClass("sibllingsrowTemplate");
        newRow.find('input').each(function() { // Clear the input values
            $(this).val("");
        });
        $("#siblings").append(newRow);
    });
    $("#addOrganization").on("click", function(event){
        event.preventDefault();
        let newRow = $(".orgRowTemplate").clone(true);
        newRow.removeClass("orgRowTemplate");
        newRow.find('input').each(function() {
            if ($(this).is(':radio') || $(this).is(':checkbox')) {
                $(this).prop('checked', false);
            } else {
                $(this).val("");
            }
        });
        $("#organizationTable").append(newRow);
    });
    $("#id_sourceOfIncome").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "familyownedbusiness"){
            $("#id_sourceOfIncomeFamilyBusiness").removeClass("hidden")  
            $("#sourceIncome").removeClass("fullLenght")       

            $("#id_sourceOfIncomeRelative").addClass("hidden")
            $("#optionalBox").addClass("visible")
        }
        else if(selectedValue == "relatives"){
            $("#id_sourceOfIncomeFamilyBusiness").addClass("hidden")  
            $("#sourceIncome").removeClass("fullLenght")          
            $("#id_sourceOfIncomeRelative").removeClass("hidden")
            $("#optionalBox").addClass("visible")
        }
        else{
            $("#id_sourceOfIncomeFamilyBusiness").addClass("hidden")
            $("#sourceIncome").addClass("fullLenght")   
            $("#id_sourceOfIncomeRelative").addClass("hidden")
            $("#optionalBox").removeClass("visible")
        }
    })
    $("#id_studentType").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "newStudent"){
            $("#id_curriculumtype").removeClass("hidden")         
            $("#studentbox").addClass("visible")
        }
        else{
            $("#id_curriculumtype").addClass("hidden")
            $("#studentbox").removeClass("visible")
        }
    })
    $("#id_curriculumtype").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "seniorhigh"){      
            $("#trackbox").addClass("visible")
        }
        else{
            $("#trackbox").removeClass("visible")
        }
    })
    $("#id_livingWith").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue=="relative"){
            $("#livingBox").removeClass("fullLength")
            $("#livingBox").addClass("halfLength")
            $("#livingOthers").addClass("hidden")
            $("#relativeBox").removeClass("hidden")
        }
        else if(selectedValue=="others"){
            $("#livingBox").removeClass("fullLength")
            $("#livingBox").addClass("halfLength")
            $("#relativeBox").addClass("hidden")
            $("#livingOthers").removeClass("hidden")
        }
        else{
            $("#livingBox").removeClass("halfLength")
            $("#livingBox").addClass("fullLength")
            $("#relativeBox").addClass("hidden")
            $("#livingOthers").addClass("hidden")
        }
    })
    
    $("#id_placeOfLiving").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "others"){
            $("#specifyPlace").removeClass("hidden")
            $("#specifyPlace").addClass("visible")
                  
        }
        else{
            $("#specifyPlace").removeClass("visible")
            $("#specifyPlace").addClass("hidden")
        }
    })
    
    $("#id_fatherOccupation").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "others"){
            
            $("#fatherOcupation").removeClass("fullLength")
            $("#fatherOcupation").addClass("halfLength")
            $("#fatherOcupationOther").removeClass("hidden")
        }
        else{
            $("#fatherOcupation").addClass("fullLength")
            $("#fatherOcupation").removeClass("halfLength")
            $("#fatherOcupationOther").addClass("hidden")
        }
    })
    $("#id_motherOccupation").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "others"){
            
            $("#motherOcupation").removeClass("fullLength")
            $("#motherOcupation").addClass("halfLength")
            $("#motherOcupationOther").removeClass("hidden")
        }
        else{
            $("#motherOcupation").addClass("fullLength")
            $("#motherOcupation").removeClass("halfLength")
            $("#motherOcupationOther").addClass("hidden")
        }
    })
    $("#id_schoolLeaver_0").change(function(event){
        if($(this).val()){
            $("#reasonOfLeaving").removeClass("hidden")
            $("#reasonOfLeaving").addClass("visible")
        }
    });
    $("#id_schoolLeaver_1").change(function(event){
        if($(this).val()){
            $("#reasonOfLeaving").addClass("hidden")
            $("#reasonOfLeaving").removeClass("visible")
        }
    });
    
    $("#id_finaciallySupporting").change(function(event){
        let selectedValue = $(this).val();
        
        console.log(selectedValue)
        if(selectedValue == "scholarship"){
            $("#scholarshiptype").removeClass("hidden")
        }
        else{
            $("#scholarshiptype").addClass("hidden")
        }
    });
    $("#id_typeOfScholarship").change(function(event){
        let selectedValue = $(this).val();
        
        console.log(selectedValue)
        if(selectedValue == "organizations"){
            $("#specifyScholarShip").removeClass("hidden")
        }
        else{
            $("#specifyScholarShip").addClass("hidden")
        }
    });
    $("#id_doYouPlanToWork_0").change(function(event){
        if($(this).val()){
            $("#spificyWhyDontPlantToWork").addClass("hidden")
        }
    });
    $("#id_doYouPlanToWork_1").change(function(event){
        if($(this).val()){
            $("#spificyWhyDontPlantToWork").removeClass("hidden")
        }
    });
});