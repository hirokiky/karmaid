function set_karma (karma){
    $('.karma-value').text(karma);
}

function error_karma (){
    $('.karma-value').text('Error');
}

function flush_karma (some_action){
    var flush_speed = 200;
    $('.karma-value').fadeOut(flush_speed, some_action).fadeIn(flush_speed);
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
        flush_karma(function (){ajax_action(api_url, stuff, 'inc')});
    });
    $('.dec').click(function (){
        flush_karma(function (){ajax_action(api_url, stuff, 'dec')});
    });
});
