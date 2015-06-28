// send the content of a cell to the server
function sendCell(cell, content) {
    var ajaxCell = {
        row:cell.row,
        column: cell.column,
        content: content
    };

    postData(ajaxCell);
}
function postData(data, callback) {
    $.post("py/json", data, callback);
}

// when server answers, update cells color
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
    // configure the conflict solving buttons click event
    $("#conflicts").click(function() {
        cellContentChanged(activeCell()); // make sure last changes have been sent
        setFormat(propositions, "");      // clear propositions colors, only rule will be colored
        $.post("py/action", {action:"conflict"}, function(xhr, status) {updateClasses(xhr)}); //ask for conflict display

    });
    $("#solve").click(function() {
        setFormat(rules, "rule");           // color the rules in blue
        cellContentChanged(activeCell());   // make sure last changes have been sent
        $.post("py/action", {action:"solution"}, function(xhr, status) {updateClasses(xhr)}); // ask for best solution display
    });

    // reset server's table on page load/reload
    $.post("py/action", {action:"reset"});
});
