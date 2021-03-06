/// <reference path="../lib/jquery.d.ts" />
/// <reference path="config.d.ts" />

var import_api = function (){
    var url_api_karma = config.url_api_karma;
    var url_api_ranking = config.url_api_ranking;

    var action_karma = function(stuff, action, done_callback, error_callback){
        $.ajax({
            type: "POST",
            url: url_api_karma,
            data: {stuff: stuff,
                   action: action},
            success: done_callback,
            error: error_callback
        })
    };
    var inc_karma = function(stuff, d, e){return action_karma(stuff, 'inc', d, e)};
    var dec_karma = function(stuff, d, e){return action_karma(stuff, 'dec', d, e)};

    var get_karma = function(stuff, done_callback, error_callback){
        $.ajax({
            type: "GET",
            url: url_api_karma,
            data: {stuff: stuff},
            async: false,
            success: done_callback,
            error: error_callback
        });
    };

    var get_ranking = function(data, done_callback, error_callback){
        $.ajax({
            type: "GET",
            url: url_api_ranking,
            data: data,
            success: done_callback,
            error: error_callback
        })
    };

    var get_ranking_asc = function(d, e){return get_ranking({}, d, e)};
    var get_ranking_desc= function(d, e){return get_ranking({desc: ''}, d, e)};

    return {
        inc_karma: inc_karma,
        dec_karma: dec_karma,
        get_karma: get_karma,
        get_ranking_asc: get_ranking_asc,
        get_ranking_desc: get_ranking_desc
    }
};

var api = import_api();
