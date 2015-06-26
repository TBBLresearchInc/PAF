/*
 * Grid management file :
 *  + create the grid and make it editable
 *  + adding higher level functions to access the grid cells
 *
 * Most of the file is taken from a slickgrid example
 */

var grid;
var data = [];
var options = {
    editable: true,
    enableAddRow: true,
    enableCellNavigation: true,
    asyncEditorLoading: false,
    autoEdit: false
};

var columns = [
    {
        id: "selector",
        name: "",
        field: "num",
        width: 30
    }
];

for (var i = 0; i < 26; i++) {
    columns.push({
        id: String.fromCharCode("A".charCodeAt(0) + (i % 26)),
        name:String.fromCharCode("A".charCodeAt(0) + (i % 26)),
        field: i,
        width: 80,
        editor: FormulaEditor,
        formatter: myFormatter
    });
}

// adding style to the grid
function myFormatter(row, cell, value, columnDef, dataContext) {
    if (value == null) {
        return "";
    } else {
        var txt = (value + "").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
        var format = Cell(cell, row).format;
        if(format != null) {
            return '<div class="'+ format + '">' + txt + '</div>';
        } else {
            return txt;
        }
    }
}

// enable grid edition capabilities
function FormulaEditor(args) {
    var _self = this;
    var _editor = new Slick.Editors.Text(args);
    var _selector;

    $.extend(this, _editor);

    function init() {
        // register a plugin to select a range and append it to the textbox
        // since events are fired in reverse order (most recently added are executed first),
        // this will override other plugins like moverows or selection model and will
        // not require the grid to not be in the edit mode
        _selector = new Slick.CellRangeSelector();
        _selector.onCellRangeSelected.subscribe(_self.handleCellRangeSelected);
        args.grid.registerPlugin(_selector);
    }

    this.destroy = function () {
        _selector.onCellRangeSelected.unsubscribe(_self.handleCellRangeSelected);
        grid.unregisterPlugin(_selector);
        _editor.destroy();
    };

    this.handleCellRangeSelected = function (e, args) {
        _editor.setValue(
            _editor.getValue() +
            grid.getColumns()[args.range.fromCell].name +
            args.range.fromRow +
            ":" +
            grid.getColumns()[args.range.toCell].name +
            args.range.toRow
        );
    };

    init();
}

// executed when all the required files are fully loaded and DOM is ready
$(function () {
    for (var i = 0; i < 50; i++) {
        var d = (data[i] = {});
        d["num"] = i;
    }

    grid = new Slick.Grid("#myGrid", data, columns, options);

    grid.setSelectionModel(new Slick.CellSelectionModel());
    grid.registerPlugin(new Slick.AutoTooltips());

    // set keyboard focus on the grid
    grid.getCanvasNode().focus();

    // manage copy/paste
    var copyManager = new Slick.CellCopyManager();
    grid.registerPlugin(copyManager);

    copyManager.onPasteCells.subscribe(function (e, args) {
        if (args.from.length !== 1 || args.to.length !== 1) {
            throw "This implementation only supports single range copy and paste operations";
        }

        var from = args.from[0];
        var to = args.to[0];
        var val;
        for (var i = 0; i <= from.toRow - from.fromRow; i++) {
            for (var j = 0; j <= from.toCell - from.fromCell; j++) {
                if (i <= to.toRow - to.fromRow && j <= to.toCell - to.fromCell) {
                    val = data[from.fromRow + i][columns[from.fromCell + j].field];
                    data[to.fromRow + i][columns[to.fromCell + j].field] = val;
                    grid.invalidateRow(to.fromRow + i);
                }
            }
        }
        grid.render();
    });

    grid.onAddNewRow.subscribe(function (e, args) {
        var item = args.item;
        var column = args.column;
        grid.invalidateRow(data.length);
        data.push(item);
        grid.updateRowCount();
        grid.render();
    });
});

