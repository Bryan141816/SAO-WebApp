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
        let newRow = `<tr class="sibllingsrowTemplate">
                        <td>
                            <div class="field_container">
                                <input type="text" name="name[]">
                            </div>
                        </td>
                        <td>
                            <div class="field_container">
                                <input type="number" name="age[]">
                            </div>      
                        </td>
                        <td>
                            <div class="field_container">
                                <input type="text" name="placework[]">
                            </div>
                        </td>
                        <td>
                            <button class="deleteRow OrangeButton">Delete</button>
                        </td>
                    </tr>`
        $("#siblings").append(newRow);
    });
    $("#siblings").on("click", ".deleteRow", function(event) {
        event.preventDefault();
        var rowCount = $("#siblings tr.sibllingsrowTemplate").length;
        if (rowCount > 1) {
            $(this).closest("tr").remove();
        } else {
            $(this).closest("tr").find("input").val("");
        }
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
        if(selectedValue == "familyownedbusiness" || selectedValue == "relatives"){
            $("#source_income_container").removeClass("hidden")
            $('#id_sourceOfIncomeSpecify').attr('required','required')
        }
        else{
            $("#source_income_container").addClass("hidden")
            $('#id_sourceOfIncomeSpecify').removeAttr('required','required')
        }
    })
    $("#id_studentType").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "newStudent"){
            $("#hs_curriculum").removeClass("hidden")
            $('#id_curriculumtype').attr('required','required')
        }
        else{
            $("#hs_curriculum").addClass("hidden")
            $('#id_curriculumtype').removeAttr('required','required')
        }
    })
    $("#id_curriculumtype").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "seniorhigh"){      
            $("#hs_track").removeClass("hidden")
            $("#id_track").attr('required','required')
        }
        else{
            $("#trackbox").addClass("hidden")
            $("#id_track").removeAttr('required','required')
        }
    })
    $("#id_livingWith").change(function(event){
        let selectedValue = $(this).val();

        if(selectedValue=="relative" || selectedValue == "others"){
            $("#living_specify").removeClass("hidden")
            $("#id_livingSpecify").attr('required','required')
        }
        else{
            $("#living_specify").addClass("hidden")
            $("#id_livingSpecify").removeAttr('required','required')
        }
    })
    
    $("#id_placeOfLiving").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "others"){
            $("#place_of_living_other").removeClass("hidden")
            $("#id_placeOfLivingOthers").attr('required','required')
        }
        else{
            $("#place_of_living_other").addClass("hidden")
            $("#id_placeOfLivingOthers").removeAttr('required','required')
        }
    })
    
    $("#id_fatherOccupation").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "others"){
            $("#father_occupation_other").removeClass("hidden")
            $("#id_fatherOtherOccupation").attr('required','required')
        }
        else{
            $("#father_occupation_other").addClass("hidden")
            $("#id_fatherOtherOccupation").removeAttr('required','required')
        }
    })
    $("#id_motherOccupation").change(function(event){
        let selectedValue = $(this).val();
    
        console.log(selectedValue)
        if(selectedValue == "others"){
            $("#mother_occupation_other").removeClass("hidden")
            $("#id_motherOtherOccupation").attr('required','required')
        }
        else{
            $("#mother_occupation_other").addClass("hidden")
            $("#id_motherOtherOccupation").removeAttr('required','required')
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

    function validateFields(container) {
        var isValid = true;
        container.find('input, select, textarea').each(function() {
            if ($(this).prop('required')) {
                if (!$(this).val()) {
                    isValid = false;
                }
            }
        });
        return isValid;
    }

    $('.nextpage').on('click', function() {
        let current = $('.current-page-activated');
        let next = current.next('.fill_out_container');
        let curret_page_counter = $('.current-fill-out');
        let next_page_counter = curret_page_counter.next('.page_viewer');

        current.removeClass('current-page-activated').addClass('current-page-deactivated');
        curret_page_counter.removeClass('current-fill-out');
        next_page_counter.addClass('current-fill-out');
        setTimeout(function() {
            current.addClass('hidden');
            next.removeClass('hidden').addClass('current-page-activated');
            current.removeClass('current-page-deactivated');
        }, 200);

        // if(validateFields(current)){
        //     current.removeClass('current-page-activated').addClass('current-page-deactivated');
        //     curret_page_counter.removeClass('current-fill-out');
        //     next_page_counter.addClass('current-fill-out');
        //     setTimeout(function() {
        //         current.addClass('hidden');
        //         next.removeClass('hidden').addClass('current-page-activated');
        //         current.removeClass('current-page-deactivated');
        //     }, 200);
        // }
    });
    $('.prevPage').on('click',()=>{
        let current = $('.current-page-activated');
        let prev = current.prev('.fill_out_container');
        let curret_page_counter = $('.current-fill-out');
        let prev_page_counter = curret_page_counter.prev('.page_viewer');
        current.removeClass('current-page-activated');
        curret_page_counter.removeClass('current-fill-out');
        prev_page_counter.addClass('current-fill-out');
        setTimeout(function() {
            current.addClass('hidden');
            prev.removeClass('hidden').addClass('current-page-activated');
            current.removeClass('current-page-deactivated');
        }, 200);
    
    });
});