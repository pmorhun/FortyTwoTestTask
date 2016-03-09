function initEditContactPage() {
    $('#edit-form').click(function(event){
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'success': function(data, status, xhr){
                    // check if we got successfull response from the server
                    if (status != 'success') {
                        alert('Servers error. Try latter');
                        return false;
                    }
                    // update modal window with arrived content from the server
                    var modal = $('#myModal');
                    var html = $(data);
                    var form = html.find('#contact-form');
                    modal.find('.modal-title').html(html.find('#title-form').text());
                    modal.find('.modal-body').html(form);
                    // init our edit form
                    initEditContactForm(form, modal);
                    // setup and show modal window finally
                    modal.modal({
                    'keyboard': false,
                    'backdrop': false,
                    'show': true
                    });
                },
                'error': function(){
                    alert('Servers error. Try latter');
                    return false;
                }
        });
        return false;
    });
}

function initEditContactForm(form, modal) {
    // attach datepicker
    initDateFields();
    // close modal window on Cancel button click
    form.find('input[name="cancel_button"]').click(function(event){
        modal.modal('hide');
        return false;
    });
    // make form work in AJAX mode
    form.ajaxForm({
        'dataType': 'html',
        'error': function(){
            alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
            return false;
        },
        'success': function(data, status, xhr) {
            var html = $(data);
            var newform = html.find('#content-column form');
            // copy form to modal if we found it in server response
            if (newform.length > 0) {
                modal.find('.modal-body').append(newform);
                // initialize form fields and buttons
                initEditContactForm(newform, modal);
            } else {
                // if no form, it means success and we need to reload page
                // to get updated contact
                location.reload(true);
            }
        }
    });
}


// Calendar
function initDateFields() {
        $('#id_birthday').datetimepicker({
            'format': 'YYYY-MM-DD'
        }).on('dp.hide', function(event){
            $(this).blur();
        });
}

$(document).ready(function(){
    initEditContactPage();
});

