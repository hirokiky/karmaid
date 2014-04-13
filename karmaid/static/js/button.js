/// <reference path="lib/jquery.d.ts" />
/// <reference path="lib/knockout.d.ts" />
/// <reference path="app/api.ts" />
/// <reference path="app/utils.ts" />
var KarmaButtonViewModel = (function () {
    function KarmaButtonViewModel() {
        var _this = this;
        this.karma = ko.observable().extend({ flushValue: { target: '.karma-value', speed: 200, flushOnlyChanged: true } });
        this.stuff = $('.stuff').text();
        api.get_karma(this.stuff, function (msg) {
            _this.karma(utils.humanize_num(msg.karma));
        }, function () {
            _this.karma('Error');
        });
    }
    KarmaButtonViewModel.prototype.incClick = function () {
        var _this = this;
        api.inc_karma(this.stuff, function (msg) {
            _this.karma(utils.humanize_num(msg.karma));
        }, function () {
            _this.karma('Error');
        });
    };
    KarmaButtonViewModel.prototype.decClick = function () {
        var _this = this;
        api.dec_karma(this.stuff, function (msg) {
            _this.karma(utils.humanize_num(msg.karma));
        }, function () {
            _this.karma('Error');
        });
    };
    return KarmaButtonViewModel;
})();
$(function () {
    ko.applyBindings(new KarmaButtonViewModel());
});
//# sourceMappingURL=button.js.map
