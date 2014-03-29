var karma_manually_updated = false;

function init_stuff_input (){
    var query = window.location.search.substring(1);
    var pos = query.indexOf('=');

    var stuff = 'karmaid';
    if (query.substring(0, pos) == 'stuff') {
        stuff = query.substring(pos+1)
    }
    $('.stuff-input').val(stuff);
}

function flush_karma (some_action){
    var flush_speed = 200;
    $('.value').fadeOut(flush_speed, some_action).fadeIn(flush_speed);
}

function set_karma (karma){
    $('.value').text(karma);
}

function error_karma (){
    $('.value').text('Error');
}

function get_stuff (){
    return $('.stuff-input').val()
}

function action_karma (api_url, action){
    $.ajax({
        type: "POST",
        url: api_url,
        data: {stuff: get_stuff(),
            action: action}
    }).done(function (msg){
        flush_karma(function (){set_karma(msg['karma'])});
    }).error(error_karma);
    karma_manually_updated = true;
}

function get_karma(api_url){
    $.ajax({
        type: "GET",
        url: api_url,
        data: {stuff: get_stuff()}
    }).done(function (msg){
        set_karma(msg['karma']);
    }).error(error_karma);
}

function get_karma_api_url() {
    return $('#api-karma').attr('value');
}


function get_ranking_api_url() {
    return $('#api-ranking').attr('value');
}


function get_host() {
    return $('#host').attr('value');
}


function refresh_karma (){
    if (karma_manually_updated === false) {
        flush_karma(function () {get_karma(get_karma_api_url())});
    } else {
        karma_manually_updated = false;
    }
    setTimeout("refresh_karma()", 5000);
}


function refresh_ranking(target, request_param){
    $.ajax({
        type: "GET",
        url: get_ranking_api_url(),
        data: request_param
    }).done(function (msg){
        var bests = msg['stuffs'];
        target.empty();
        for (var i = 0; i < bests.length; i++){
            var ele = $('<li />').text(bests[i]);
            target.append(ele);
        }
    }).error(function (){
        $('.bests').text('Some error happened')
    });
}


function create_widget_script(stuff){
    var stuff_ele = $('<script />');
    stuff_ele.text('var karmaid_stuff=\"' + stuff + '\";');
    return '<script>var karmaid_stuff=\"' + stuff + '\";</script><script src="' + get_host() + '/widget.js"></script>';
}


$(function (){
    var api_url = get_karma_api_url();
    init_stuff_input();
    refresh_karma();
    refresh_ranking($('.best'), {});
    refresh_ranking($('.worst'), {desc: ''});

    $('.inc').click(function (){
        action_karma(api_url, 'inc');
    });
    $('.dec').click(function (){
        action_karma(api_url, 'dec');
    });
    $('.stuff-input').change(function (){get_karma(api_url)});

    $('.generator-input input').change(function (){
        var generator_result_ele = $('.generator-result textarea');
        var stuff = $(this).val();
        if (stuff == '') {
            generator_result_ele.val('');
            $('generated-widget').text('');
        } else {
            generator_result_ele.val(create_widget_script(stuff)).select();
        }
    });
    $('.generator-result textarea').focus(function (){
        $(this).select();
    });
    $('.ranking-refresh').click(function (){
        var flush_speed = 200;
        $('.ranks').fadeOut(flush_speed, function(){
            refresh_ranking($('.best'), {});
            refresh_ranking($('.worst'), {desc: ''});
        }).fadeIn(flush_speed);
    })
});
