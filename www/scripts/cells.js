// create an object containing  additionnal info about cells
var cells = {};

// make a cell object, containing useful shortcuts
function Cell(column, row) {
    var c = {column: column, row: row};
    c.name = getCellName(column, row);  // give the cell a readable name, like "C1"
    c.text = function(txt) {            // get the text contained in the cell
        if(txt!=null)                                  // if txt arg was given, update grid content
            setCellText(column, row, txt);
        else if(grid.getCellEditor(column,row)!=null)  //if the cell is currently edited, get the text entered
            return grid.getCellEditor(column,row).getValue();
        else
            return getCellText(column,row);
    };

    c.coordinates = [column, row];
    // get all the extra info stored in cells (if any)
    if(cells[c.name]!=null) {
        $.extend(c,cells[c.name]);
    }
    // set this cell as selected
    c.activate = function() {
        grid.setActiveCell(c.row, c.column);
    };
    // getters and setters
    c.setFormat = function(format) {
        if(cells[c.name]==null)
            cells[c.name]={};
        cells[c.name].format = format;
    };
    c.setWeight = function(weightCol, weightRow) {
        if(cells[c.name]==null)
            cells[c.name]={};
        cells[c.name].linkedWeight = [weightCol, weightRow];
    };
    c.getWeight = function() {
        if(c.linkedWeight!=null)
            return cellFromArray(c.linkedWeight);
    };
    c.setProposition = function(propCol, propRow) {
        if(cells[c.name]==null)
            cells[c.name]={};
        c.text("$"+Cell(propCol,propRow).name+":"+c.text().substring(c.text().indexOf(":")+1));
        cells[c.name].linkedProposition = [propCol, propRow];
    };
    c.getProposition = function() {
        if(c.linkedProposition!=null)
            return cellFromArray(c.linkedProposition);
    };
    return c;
}
// get the current active cell
function activeCell() {
    var c= grid.getActiveCell();
    return Cell(c.cell, c.row);
}

function cellFromArray(array) {
    return Cell(array[0],array[1]);
}
function getCellText(column, row) {
    return data[row][grid.getColumns()[column].field];
}
function setCellText(column, row, value) {
    data[row][grid.getColumns()[column].field] = value;
}
// get a cell "natural" name, (e.g. "C3" or "E4")
function getCellName(column, row) {
    return grid.getColumns()[column].name + row + "";
}

function cellNameToArray(name) {
    var column = parseInt(grid.getColumnIndex(name.substring(0,1)));
    var row = parseInt(name.substring(1));
    return [column, row];
}
function cellNamed(name) {
    return cellFromArray(cellNameToArray(name));
}
function setFormat(cells, format) {
    var cellname;
    for(cellname in cells) {
        cellNamed(cellname).setFormat(format);
    }
}