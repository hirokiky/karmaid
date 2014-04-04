$(function(){
    var api = import_api({url_api_karma: $('#api-url').attr('value')});
    var utils = import_utils();
    var stuff = $('.stuff').text();

    function set_karma (karma){
        $('.karma-value').text(karma);
    }

    api.get_karma(
        stuff,
        function(msg){set_karma(utils.humanize_num(msg.karma))},
        function(){set_karma('Error')}
    );

    $('.inc').click(function (){
        utils.flush_element($('.karma-value'), 200, function(){
            api.inc_karma(
                stuff,
                function(msg){
                    set_karma(utils.humanize_num(msg.karma));
                },
                function(){return 'Error'}
            )
        })
    });
    $('.dec').click(function (){
        utils.flush_element($('.karma-value'), 200, function(){
            api.dec_karma(
                stuff,
                function(msg){
                    set_karma(utils.humanize_num(msg.karma));
                },
                function(){return 'Error'}
            )
        })
    });
});
