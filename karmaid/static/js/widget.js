(function (){
    var base_url = 'http://127.0.0.1:6543';
    var stuff = karmaid_stuff;
    var write_string = '<iframe src="' + base_url + '/button/1/?stuff=' + stuff + '" height="23" width="' + (110 + stuff.length * 7).toString() + '" scrolling="no" frameborder="0" title="Karmaid Karma Button"></iframe>';

    document.write(write_string);
})();
