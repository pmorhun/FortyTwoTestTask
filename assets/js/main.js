function showRequests() {
    $('#btn').click(function(){

    var rq = $(this);

    $.ajax({
        async: true,
        type: "POST",
        data: {
            last_request: rq.data('last_request'),
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
            },
        url: url_requests_list,//rq.attr('href'),
        dataType: 'json',
        success: function (html) {
            alert('Yes');
            //viewed = [];
            //last_req = html.last_request
            //html.requests = JSON.parse(html.requests);
            //for(var i = 0; i < html.requests.length; i++) {
            //    var obj = html.requests[i];
            //    $('#requests tr:eq('+addingRequest(table_child, priority, obj['fields']['priority'])+')').after('<tr style="font-weight: bold;"><td>'+obj['pk']+'</td><td>'+obj['fields']['type']+'</td><td>'+Date(obj['fields']['time']).replace(' GMT+0300 (EEST)', '')+'</td><td>'+obj['fields']['url']+'</td><td>'+priorityForm(obj['pk'])+'</td></tr>');
            //    viewed.push(obj['pk']);
            //}
            //markViewed(viewed);
        },
        error: function (html) {
            alert('Error AJAX!');
        }

    });
});

}

function markViewed(viewed){
    $.ajax({
        async: true,
        type: "POST",
        data: {
            'viewed[]': viewed
            },
        url: 'url_viewed',
        success: function (html) {
            console.log('Success-viewed')
        },
        error: function (html) {
            console.log('Error-viewed')
        }
    });
}

//var url_viewed = '{% url 'requests_viewed' %}';
//var last_req = '{{ last_request }}';
var viewed = [];
$(document).ready(function(){
  showRequests();
  //setInterval('showRequests()', 11500);

});
