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

    $('#searchButton').on('click', function(event) {
        event.preventDefault(); // Prevent default form submission behavior
        console.log('hs')
        // Get the entered ID number
        let idNumber = $('#studentIDBox').val();

        // Send AJAX request to fetch student info
        $.ajax({
            url: '/search_student_info/',
            method: 'POST',
            data: {'id_number': idNumber},
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(response) {
                $('#info_table').removeClass('hidden')
                $('#questionForm').removeClass('hidden')

                $('#studentID').val(response.student_id)
                $('#info_table tr').empty();
                
                // Append new row with retrieved data
                $('#info_table').append(
                    '<tr id="info_table_head">'+
                    '<th>NAME</th>'+
                    '<th>CONTACT NO.</th>'+
                    '</tr>'
                );
                $('#info_table').append(
                    '<tr>' +
                    '<td>' + response.name + '</td>' +
                    '<td>' + '0' + response.contact_number + '</td>' +
                    '</tr>'
                );
            },
            error: function(error) {
                $('#requestForm').addClass('hidden')
                $('#info_table').removeClass('hidden')
                $('#info_table').empty()
                $('#info_table').append(
                    '<tr>' +
                    '<td colspan="2">Student ID not found.</td>' +
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
                statusSpan.replaceWith(' <span class="accepted">Accepted</span>')
                accept.remove()
                decline.remove()
            },
            error: function(xhr, status, error) {
                // Handle error if needed
            }
        });
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