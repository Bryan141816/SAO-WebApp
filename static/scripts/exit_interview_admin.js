$(document).ready(function(){
    $('input[name="currentlyEmployed"]').change(function(){
        $('#explainationEmployed').removeClass('hidden')
        let selectedValue = $('input[name="currentlyEmployed"]:checked').val();
        if (selectedValue === "True") {
            $('#employedYesNo').text('-Please provide the name and address of the company:');
        } else if (selectedValue === "False") {
            $('#employedYesNo').text('-Please provide the name and address of the company you want:');
        }
    });
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    // Intercept form submission
    $('#searchButton').on('click', function(event) {
        event.preventDefault(); // Prevent default form submission behavior
        
        // Get the entered ID number
        var idNumber = $('#studentIDBox').val();

        // Send AJAX request to fetch student info
        $.ajax({
            url: '/search_exit_interview_request/',
            method: 'POST',
            data: {'id_number': idNumber},
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(response) {
                $('#info_table tr').empty();
            
                // Append table headers
                $('#info_table').append(
                    '<tr id="info_table_head">' +
                    '<th>DATE RECEIVED</th>' +
                    '<th>STUDENT ID</th>' +
                    '<th>NAME</th>' +
                    '<th colspan="3">STATUS</th>' +
                    '</tr>'
                );
            
                // Append data for each student
                response.forEach(function(student) {
                    let show_form = '<button class="showformButton hidden">SHOW FORM</button>';
                    let status_val = '';
                    let button_element = '';
            
                    show_form = '<button class="showformButton hidden">SHOW FORM</button>'
                    if(student.status == 'Accepted'){
                        show_form = '<button class="showformButton">SHOW FORM</button>'
                        status_val = '<span class="accepted">Accepted</span>'
                    }
                    else if(student.status == 'Declined')
                        status_val = '<span class="declined">Pending</span>'
                    else if(student.status == 'Pending')
                        status_val = '<span class="pending">Pending</span>'
                    else{
                        status_val = '<span class="expired">Expired</span>'
                    }
                    if(student.status != 'Pending'){
                        button_element =  '<button class="delete">DELETE</button>'
                    }
                    else{
                        button_element = `<button class="accept">ACCEPT</button>
                        <button class="decline">DECLINE</button>
                        <button class="delete">DELETE</button>`
                    }
            
                    $('#info_table').append(
                        '<tr>' +
                        '<td>' + student.date_received + '</td>' +
                        '<td>' + student.student_id + '</td>' +
                        '<td>' + student.name + '</td>' +
                        '<td>' + status_val + '</td>' +
                        '<td>' + '<div class="horizontal">' + button_element + '</div>' + '</td>' +
                        '<td>' + show_form + '</td>' +
                        '</tr>'
                    );
                });
            },
            error: function(error) {
                $('#requestForm').addClass('hidden')
                $('#info_table').removeClass('hidden')
                $('#info_table').empty()
                $('#info_table').append(
                    '<tr>' +
                    '<td colspan="4">Student ID not found.</td>' +
                    '</tr>'
                );
            }
        });
    });
    $('.accept').click(function() {
        let exitinterviewId = $(this).closest('tr').find('.exitinterviewId').val();
        let statusSpan = $(this).closest('tr').find('.pending');
        let accept = $(this).closest('tr').find('.accept');
        let decline = $(this).closest('tr').find('.decline');
        // Perform further actions here, such as sending the ID to the server
        $.post({
            url: '/update_exit_interview_status/',
            data: { 'exitinterviewId': exitinterviewId, 'type': 'accept' },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            headers: {'X-CSRFToken': csrftoken}, 
            success: function(response) {
                $('.showformButton').removeClass('hidden')
                statusSpan.replaceWith(' <span class="accepted">Accepted</span>')
                accept.remove()
                decline.remove()
            },
            error: function(xhr, status, error) {
                // Handle error if needed
            }
        });
    });
    $(document).on('click', '.showformButton', function() {
        console.log('haha');
        let OjtRequestID = $(this).closest('tr').find('.OjtRequestID').val();
        $('.showform_container').addClass('active');
        /*$.post({
            url: '/get_ojt_assessment_data/',
            data: { 'OjtRequestID': OjtRequestID},
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            headers: {'X-CSRFToken': csrftoken}, 
            success: function(response) {
                console.log(response)
                $('#student-name').text(response.name)
                $('#school-year').text(response.schoolyear)
                $('#student-course').text(`${response.program}.`)
                $('#issue-date').text(response.date_accepted)
                $('.showform_container').addClass('active');
            },
            error: function(xhr, status, error) {
                // Handle error if needed
            }
        });*/
    });
    $('.closeform').click(function(){
        $('.showform_container').removeClass('active');
    });
    // Event listener for decline button
    $('.decline').click(function() {
        let exitinterviewId = $(this).closest('tr').find('.exitinterviewId').val();
        let statusSpan = $(this).closest('tr').find('.pending');
        let accept = $(this).closest('tr').find('.accept');
        let decline = $(this).closest('tr').find('.decline');
        // Perform further actions here, such as sending the ID to the server
        $.post({
            url: '/update_exit_interview_status/',
            data: { 'exitinterviewId': exitinterviewId, 'type': 'decline' },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            headers: {'X-CSRFToken': csrftoken}, 
            success: function(response) {
                statusSpan.replaceWith(' <span class="declined">Declined</span>')
                accept.remove()
                decline.remove()
            },
            error: function(xhr, status, error) {
                // Handle error if needed
            }
        });
    });

    // Event listener for delete button
    $('.delete').click(function() {
        let exitinterviewId = $(this).closest('tr').find('.exitinterviewId').val();
        let parentRow = $(this).closest('tr')
        $.post({
            url: '/delete_exit_interview_status/',
            data: { 'exitinterviewId': exitinterviewId },
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            headers: {'X-CSRFToken': csrftoken}, 
            success: function(response) {
                parentRow.remove()
            },
            error: function(xhr, status, error) {
                // Handle error if needed
            }
        });
    });
});