/// <reference path="lib/jquery.d.ts" />
/// <reference path="lib/knockout.d.ts" />
/// <reference path="app/api.ts" />
/// <reference path="app/utils.ts" />

class KarmaButtonViewModel {
    stuff: string;
    karma = ko.observable()
        .extend({flushValue: {target: '.karma-value', speed: 200, flushOnlyChanged: true}});

    incClick(){
        api.inc_karma(
            this.stuff,
            (msg)=>{this.karma(utils.humanize_num(msg.karma))},
            ()=>{this.karma('Error')}
        )
    }
    decClick(){
        api.dec_karma(
            this.stuff,
            (msg)=>{this.karma(utils.humanize_num(msg.karma))},
            ()=>{this.karma('Error')}
        )
    }

    constructor(){
        this.stuff = $('.stuff').text();
        api.get_karma(
            this.stuff,
            (msg)=>{this.karma(utils.humanize_num(msg.karma))},
            ()=>{this.karma('Error')}
        );
    }

}
$(()=>{ko.applyBindings(new KarmaButtonViewModel())});
