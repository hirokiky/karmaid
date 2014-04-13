/// <reference path="lib/jquery.d.ts" />
/// <reference path="lib/knockout.d.ts" />
/// <reference path="lib/underscore.d.ts" />
/// <reference path="app/ko_flushvalue.ts" />
/// <reference path="app/api.ts" />
/// <reference path="app/config.d.ts" />
function get_stuff_by_param() {
    var query = window.location.search.substring(1);
    var pos = query.indexOf('=');

    var stuff = 'karmaid';
    if (query.substring(0, pos) == 'stuff') {
        stuff = query.substring(pos + 1);
    }
    return stuff;
}

var TopViewModel = (function () {
    function TopViewModel() {
        var _this = this;
        /* Karma */
        this.karma = ko.observable().extend({ flushValue: { target: '.value', speed: 200, flushOnlyChanged: true } });
        this.stuff = ko.observable();
        this.karma_manually_updated = false;
        /* Ranking */
        this.bests = ko.observableArray();
        this.worsts = ko.observableArray();
        /* Karma */
        this.stuff.subscribe(function () {
            _this.refreshKarma();
        });
        this.stuff(get_stuff_by_param());
        setInterval(function () {
            _this.refreshKarmaPeriodically();
        }, 5000);

        /* Ranking */
        this.refreshRanking();
    }
    TopViewModel.prototype.incClick = function () {
        var _this = this;
        api.inc_karma(this.stuff(), function (msg) {
            _this.karma(msg.karma);
        }, function () {
            _this.karma('Error');
        });
        this.karma_manually_updated = true;
    };

    TopViewModel.prototype.decClick = function () {
        var _this = this;
        api.dec_karma(this.stuff(), function (msg) {
            _this.karma(msg.karma);
        }, function () {
            _this.karma('Error');
        });
        this.karma_manually_updated = true;
    };

    TopViewModel.prototype.refreshKarma = function () {
        var _this = this;
        api.get_karma(this.stuff(), function (msg) {
            _this.karma(msg.karma);
        }, function () {
            _this.karma('Error');
        });
    };

    TopViewModel.prototype.refreshKarmaPeriodically = function () {
        if (this.karma_manually_updated == false) {
            this.refreshKarma();
        } else {
            this.karma_manually_updated = false;
        }
    };

    TopViewModel.prototype.refreshRanking = function () {
        var _this = this;
        api.get_ranking_asc(function (msg) {
            _this.bests(msg.stuffs);
        }, function () {
            _this.bests(['Error']);
        });
        api.get_ranking_desc(function (msg) {
            _this.worsts(msg.stuffs);
        }, function () {
            _this.worsts(['Error']);
        });
    };

    TopViewModel.prototype.saveRankPosition = function (elem) {
        if (elem.nodeType == 1) {
            elem.saveOffsetTop = elem.offsetTop;
        }
    };

    TopViewModel.prototype.moveRank = function (elem) {
        if (elem.nodeType == 1) {
            if (elem.offsetTop !== elem.saveOffsetTop) {
                var tempElement = elem.cloneNode(true);
                $(elem).css({ visibility: 'hidden' });
                $(tempElement).css({
                    position: "absolute",
                    width: window.getComputedStyle(elem).width
                });
                elem.parentNode.appendChild(tempElement);
                $(tempElement).css({ top: elem.saveOffsetTop }).animate({ top: elem.offsetTop }, function () {
                    $(elem).css({ visibility: 'visible' });
                    elem.parentNode.removeChild(tempElement);
                });
            }
        }
    };
    return TopViewModel;
})();

$(function () {
    ko.applyBindings(new TopViewModel());

    /* Button generator, maybe this should be written on Knockout.js too... */
    var widget_template = _.template('<script>var karmaid_stuff=\"<%- stuff %>";</script>' + '<script src="<%- host %>/widget.js"></script>');
    function create_widget_script(stuff) {
        return widget_template({ stuff: stuff, host: config.host });
    }
    $('.generator-input input').change(function () {
        var generator_result_ele = $('.generator-result textarea');
        var stuff = $(this).val();
        if (stuff == '') {
            generator_result_ele.val('');
            $('generated-widget').text('');
        } else {
            generator_result_ele.val(create_widget_script(stuff)).select();
        }
    });
    $('.generator-result textarea').focus(function () {
        $(this).select();
    });
});
//# sourceMappingURL=karmaid.js.map
