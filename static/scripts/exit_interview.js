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
});