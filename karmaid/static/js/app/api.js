var import_api = function (settings){
    var url_api_karma = settings.url_api_karma;
    var url_api_ranking = settings.url_api_ranking;

    var action_karma = function(stuff, action, done_callback, error_callback){
        $.ajax({
            type: "POST",
            url: url_api_karma,
            data: {stuff: stuff,
                action: action}
        }).done(done_callback).error(error_callback);
    };
    var inc_karma = function(stuff, d, e){return action_karma(stuff, 'inc', d, e)};
    var dec_karma = function(stuff, d, e){return action_karma(stuff, 'dec', d, e)};

    var get_karma = function(stuff, done_callback, error_callback){
        $.ajax({
            type: "GET",
            url: url_api_karma,
            data: {stuff: stuff},
            async: false
        }).done(done_callback).error(error_callback);
    };

    var get_ranking = function(data, done_callback, error_callback){
        $.ajax({
            type: "GET",
            url: url_api_ranking,
            data: data
        }).done(done_callback).error(error_callback);
    };

    var get_ranking_asc = function(error_callback){return get_ranking({}, error_callback)};
    var get_ranking_desc= function(error_callback){return get_ranking({desc: ''}, error_callback)};

    return {
        inc_karma: inc_karma,
        dec_karma: dec_karma,
        get_karma: get_karma,
        get_ranking_asc: get_ranking_asc,
        get_ranking_desc: get_ranking_desc
    }
};