$(function(){
    var api = import_api({url_api_karma: $('#api-url').attr('value')});
    var utils = import_utils();
    var stuff = $('.stuff').text();

    var KarmaButtonViewModel = function(){
        var self = this;
        self.karma = ko.observable()
            .extend({flushValue: {target: '.karma-value', speed: 200, flushOnlyChanged: true}});

        self.incClick = function(){
            api.inc_karma(
                stuff,
                function(msg){self.karma(utils.humanize_num(msg.karma))},
                function(){self.karma('Error')}
            )
        };
        self.decClick = function(){
            api.dec_karma(
                stuff,
                function(msg){self.karma(utils.humanize_num(msg.karma))},
                function(){self.karma('Error')}
            )
        };
        api.get_karma(
            stuff,
            function(msg){self.karma(utils.humanize_num(msg.karma))},
            function(){self.karma('Error')}
        );

    };
    ko.applyBindings(new KarmaButtonViewModel());
});
