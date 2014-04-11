/*
 * An additional extender which is to flush element when observable value changed.
 *
 * option: you should apply object as option containing following properties:
 *
 * - target: element name for flushing.
 * - speed: speed for flushing (milli seconds)
 * - flushOnlyChanged:
 *       You can apply true if the element should flush only the observable value changed.
 */


var utils = import_utils();


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
