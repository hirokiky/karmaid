function set_karma (karma){
    $('.karma-value').text(karma);
}

function error_karma (){
    $('.karma-value').text('Error');
}

function ajax_action (api_url, stuff, action){
    $.ajax({
        type: "POST",
        url: api_url,
        data: {stuff: stuff,
               action: action}
    }).done(function (msg){
        set_karma(msg['karma']);
    }).error(error_karma);
}
$(function(){
    var api_url = $('#api-url').attr('value');
    var stuff = $('.stuff').text();

    $.ajax({
        type: "GET",
        url: api_url,
        data: {stuff: stuff}
    }).done(function (msg){
        set_karma(msg['karma']);
    }).error(error_karma);

    $('.inc').click(function (){
        ajax_action(api_url, stuff, 'inc');
    });
    $('.dec').click(function (){
        ajax_action(api_url, stuff, 'dec');
    });
});
