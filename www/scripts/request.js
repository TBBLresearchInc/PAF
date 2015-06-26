
function sendCell(cell, content) {
    var ajaxCell = {
        row:cell.row,
        column: cell.column,
        content: content
    };

    postData(ajaxCell, function(xhr, status) {
        //updateClasses(xhr);
    });
}
function postData(data, callback) {
    $.post("py/json", data, callback);
}

function updateClasses(xhr) {
    var cell;
    var cells = JSON.parse(xhr).cells;
    var cellIndex;
    for(cellIndex in cells) {
        cell = cells[cellIndex];
        if(cell.hasOwnProperty("column") && cell.hasOwnProperty("row") && cell.hasOwnProperty("result")) {
            Cell(cell.column, cell.row).setFormat(cell.result);
        }
    }
    grid.invalidate();
}

$(function() {
    $("#conflicts").click(function() {
        cellContentChanged(activeCell());
        setFormat(propositions, "");
        $.post("py/action", {action:"conflict"}, function(xhr, status) {updateClasses(xhr)});

    });
    $("#solve").click(function() {
        setFormat(rules, "rule");
        cellContentChanged(activeCell());
        $.post("py/action", {action:"solution"}, function(xhr, status) {updateClasses(xhr)});
    });
    $.post("py/action", {action:"reset"});
});
