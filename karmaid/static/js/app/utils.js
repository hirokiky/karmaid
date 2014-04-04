function import_utils(){
    var humanize_num = function (inputed){
        var digits = inputed.toString().length;
        if (digits < 4){
            return inputed.toString();
        } else if (digits >= 4 && digits < 7){
            return (Math.round(inputed / 100) / 10).toString() + 'k'
        } else if (digits >= 7 && digits < 10){
            return (Math.round(inputed / 100000) / 10).toString() + 'm'
        } else {
            return (Math.round(inputed / 100000000) / 10).toString() + 'g'
        }
    };

    var flush_element = function (target_element, flush_speed, callback){
        target_element.fadeOut(flush_speed, callback).fadeIn(flush_speed);
    };

    return {
        humanize_num: humanize_num,
        flush_element: flush_element
    }
}
