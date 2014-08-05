$(document).ready(function() {



    $('.button').on('click', function() {
        var response = $(this).data('type');
        var data = JSON.stringify(response);
        $.ajax({
            url: '/student_response/',
            type: 'POST',
            dataType: 'html',
            data: data,
            success: function(returned_response) {
                console.log('success')
            },
            error: function(returned_response) {
                console.log('error')
            }
        })
    });


    $('.submit').on('click', function() {
        var response = $(this).data('type');
        var data = JSON.stringify(response);
        $.ajax({
            url: '/teacher_response/',
            type: 'POST',
            dataType: 'html',
            data: data,
            success: function(returned_response) {
                console.log('success')
            },
            error: function(returned_response) {
                console.log('error')
            }
        })
    });
});
