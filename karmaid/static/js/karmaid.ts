/// <reference path="lib/jquery.d.ts" />
/// <reference path="lib/knockout.d.ts" />
/// <reference path="lib/underscore.d.ts" />
/// <reference path="app/ko_flushvalue.ts" />
/// <reference path="app/api.ts" />
/// <reference path="app/config.d.ts" />


function get_stuff_by_param(){
    var query = window.location.search.substring(1);
    var pos = query.indexOf('=');

    var stuff = 'karmaid';
    if (query.substring(0, pos) == 'stuff') {
        stuff = query.substring(pos+1)
    }
    return stuff
}


class TopViewModel {
    /* Karma */
    karma = ko.observable()
        .extend({flushValue: {target: '.value', speed: 200, flushOnlyChanged: true}});
    stuff = ko.observable();
    karma_manually_updated: boolean = false;

    incClick(){
        api.inc_karma(this.stuff(),
            (msg)=>{this.karma(msg.karma)},
            ()=>{this.karma('Error')
            });
        this.karma_manually_updated = true;
    }

    decClick(){
        api.dec_karma(this.stuff(),
            (msg)=>{this.karma(msg.karma)},
            ()=>{this.karma('Error')
            });
        this.karma_manually_updated = true;
    }

    refreshKarma(){
        api.get_karma(this.stuff(),
            (msg)=>{
                this.karma(msg.karma);
            },
            ()=>{this.karma('Error')})
    }

    refreshKarmaPeriodically(){
        if (this.karma_manually_updated == false){
            this.refreshKarma();
        } else {
            this.karma_manually_updated = false;
        }
    }

    /* Ranking */
    bests = ko.observableArray();
    worsts = ko.observableArray();

    refreshRanking(){
        api.get_ranking_asc(
            (msg)=>{this.bests(msg.stuffs)},
            ()=>{this.bests(['Error'])}
        );
        api.get_ranking_desc(
            (msg)=>{this.worsts(msg.stuffs)},
            ()=>{this.worsts(['Error'])}
        );
    }

    saveRankPosition(elem){
        if (elem.nodeType == 1) {
            elem.saveOffsetTop = elem.offsetTop;
        }
    }

    moveRank(elem){
        if (elem.nodeType == 1) {
            if (elem.offsetTop !== elem.saveOffsetTop) {
                var tempElement = elem.cloneNode(true);
                $(elem).css({visibility: 'hidden'});
                $(tempElement).css({
                    position: "absolute",
                    width: window.getComputedStyle(elem).width
                });
                elem.parentNode.appendChild(tempElement);
                $(tempElement)
                    .css({top: elem.saveOffsetTop})
                    .animate({top: elem.offsetTop}, function() {
                        $(elem).css({visibility: 'visible'});
                        elem.parentNode.removeChild(tempElement);
                    });
            }
        }
    }

    constructor(){
        /* Karma */
        this.stuff.subscribe(()=>{this.refreshKarma()});
        this.stuff(get_stuff_by_param())
        setInterval(()=>{this.refreshKarmaPeriodically()}, 5000);

        /* Ranking */
        this.refreshRanking();
    }

}

$(()=>{
    ko.applyBindings(new TopViewModel());

    /* Button generator, maybe this should be written on Knockout.js too... */
    var widget_template = _.template('<script>var karmaid_stuff=\"<%- stuff %>";</script>' +
        '<script src="<%- host %>/widget.js"></script>');
    function create_widget_script(stuff){
        return widget_template({stuff: stuff, host: config.host});
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
