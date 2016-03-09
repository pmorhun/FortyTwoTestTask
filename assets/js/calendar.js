$(document).ready(function() {
        $('#id_birthday').datetimepicker({
            'format': 'YYYY-MM-DD'
        }).on('dp.hide', function(event){
            $(this).blur();
        });
});
