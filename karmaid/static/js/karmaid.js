$(function(){
    var api = import_api(
        {url_api_karma: $('#api-karma').attr('value'),
         url_api_ranking: $('#api-ranking').attr('value')}
    );
    var utils = import_utils();
    var host = $('#host').attr('value');

    ko.extenders.flushValue = function(target, option){
        return ko.computed({
            read: target,
            write: function(value){
                var current = target();
                if (!option.flushOnlyChanged || current !== value){
                    utils.flush_element($(option.target), option.speed, function(){target(value)});
                }
            }
        });
    };

    var TopViewModel = function(){
        var self = this;

        /* Karma */
        self.karma = ko.observable()
            .extend({flushValue: {target: '.value', speed: 200, flushOnlyChanged: true}});
        self.stuff = ko.observable();
        self.karma_manually_updated = false;

        self.incClick = function(){
            api.inc_karma(self.stuff(),
                function(msg){self.karma(utils.humanize_num(msg.karma))},
                function(){self.karma('Error')
                });
            self.karma_manually_updated = true;
        };

        self.decClick = function(){
            api.dec_karma(self.stuff(),
                function(msg){self.karma(utils.humanize_num(msg.karma))},
                function(){self.karma('Error')
                });
            self.karma_manually_updated = true;
        };

        self.refreshKarma = function(){
            api.get_karma(self.stuff(),
                function(msg){
                    self.karma(msg.karma);
                },
                function(){self.karma('Error')})
        };

        self.stuff.subscribe(function(){self.refreshKarma()});

        (function init_stuff(){
            var query = window.location.search.substring(1);
            var pos = query.indexOf('=');

            var stuff = 'karmaid';
            if (query.substring(0, pos) == 'stuff') {
                stuff = query.substring(pos+1)
            }
            self.stuff(stuff);
        })();

        self.refreshKarmaPeriodically = function(){
            if (self.karma_manually_updated == false){
                self.refreshKarma();
            } else {
                self.karma_manually_updated = false;
            }
        };
        setInterval(self.refreshKarmaPeriodically, 5000);

        /* Ranking */

        self.bests = ko.observableArray()
            .extend({flushValue: {target: '.best', speed: 200, flushOnlyChanged: false}});
        self.worsts = ko.observableArray()
            .extend({flushValue: {target: '.worst', speed: 200, flushOnlyChanged: false}});

        self.refreshRanking = function(){
            api.get_ranking_asc(function(msg){self.bests(msg.stuffs)},
                function(){self.bests(['Error'])});
            api.get_ranking_desc(function(msg){self.worsts(msg.stuffs)},
                function(){self.worsts(['Error'])});
        };
        self.refreshRanking();
    };

    ko.applyBindings(new TopViewModel());


    /* Button generator, maybe this should be written on Knockout.js too... */

    var widget_template = _.template('<script>var karmaid_stuff=\"<%- stuff %>";</script>' +
                                     '<script src="<%- host %>/widget.js"></script>');
    function create_widget_script(stuff){
        return widget_template({stuff: stuff, host: host});
    }
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

});
