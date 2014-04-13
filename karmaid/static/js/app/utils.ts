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

    return {
        humanize_num: humanize_num
    }
}

var utils = import_utils();
