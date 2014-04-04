$(function(){
    var api = import_api({url_api_karma: $('#api-url').attr('value')});
    var utils = import_utils();
    var stuff = $('.stuff').text();

    var KarmaButtonViewModel = function(){
        var self = this;
        self.karma = ko.observable();

        self.flushValue = function(callback){
            utils.flush_element($('.karma-value'), 200, callback);
        };

        self.incClick = function(){
            self.flushValue(function(){
                api.inc_karma(stuff,
                    function(msg){self.karma(utils.humanize_num(msg.karma))},
                    function(){self.karma('Error')})
            })
        };
        self.decClick = function(){
            self.flushValue(function(){
                api.dec_karma(stuff,
                    function(msg){self.karma(utils.humanize_num(msg.karma))},
                    function(){self.karma('Error')})
            })
        };
        api.get_karma(
            stuff,
            function(msg){self.karma(utils.humanize_num(msg.karma))},
            function(){self.karma('Error')}
        );

    };
    ko.applyBindings(new KarmaButtonViewModel());
});
