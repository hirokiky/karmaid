function humanize_num(karma){
    var digits = karma.toString().length
    if (digits < 4){
        return karma.toString();
    } else if (digits >= 4 && digits < 7){
        return (Math.round(karma / 100) / 10).toString() + 'k'
    } else if (digits >= 7 && digits < 10){
        return (Math.round(karma / 100000) / 10).toString() + 'm'
    } else {
        return (Math.round(karma / 100000000) / 10).toString() + 'g'
    }
}

function set_karma (karma){
    $('.karma-value').text(humanize_num(karma));
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
