var choosingCell = false;
var choosingCellCallback;
var selectedCell = null;
var ignoreCellChange = false;
var keyDownCallback;
var inputFocus=false;
var ruleGridContent;
var weightGridContent;
var propGridContent;

$(function() {
    weightGridContent= initGrid([{name:"Poids", size:69},{name:"Proposition", size:300}],"#weights");
    ruleGridContent = initGrid([{name:"", size:40},{name:"Incompatibles", size:200},{name:"Case", size:100}],"#ruleprops");
    propGridContent = initGrid([{name:"Regle", size:200},{name:"Case", size:180}],"#proprules");

    Cell(1,1).activate();

    //display welcome sidebar
    setSidebarSection("welcome");
    loadWelcomeSidebar();

    // subscribe to grid events
    grid.onActiveCellChanged.subscribe(function (e, args) {
        sideBarChangedCell(args.cell, args.row);
    });
    grid.onClick.subscribe(function (e, args) {
        sideBarSelectedCell(args.cell, args.row, e);
    });



    // add useful function startswith to String
    if(!String.prototype.startsWith){
        String.prototype.startsWith = function (str) {
            return !this.indexOf(str);
        }
    }
});

// create a small grid and display it
//          * id : the ID of the div containing the grid
//          * columns : an array containing columns descriptor. Each descriptor
//                  should have a "name" field and a "size" field
function initGrid(columns, id) {
    var data= [];
    var options = {
        editable: true,
        enableAddRow: true,
        enableCellNavigation: true,
        asyncEditorLoading: false,
        autoEdit: false
    };
    var gridColumns = [];
    var index;
    for(index in columns) {
        gridColumns.push(
            {
               id: columns[index]["name"],
             name: columns[index]["name"],
            field: columns[index]["name"],
            width: columns[index]["size"]
        });
    }
    for (var i = 0; i < 20; i++) {
        var d = (data[i] = {});
        d["num"] = i;
    }

    var gg = new Slick.Grid(id, data, gridColumns, options);

    gg.setSelectionModel(new Slick.CellSelectionModel());
    return {data:data, grid:gg};
}

// change displayed sidebar
//          * section : the name (the ID, actually) of the sidebar to be displayed
function setSidebarSection(section) {

    selectedCell = activeCell();

    if(section != "proposition")
        $("#proposition").slideUp();
    if(section != "rule")
        $("#rule").slideUp();
    if(section != "comment")
        $("#comment").slideUp();
    if(section != "weight")
        $("#weight").slideUp();
    if(section != "welcome")
        $("#welcome").slideUp();

    switch(section) {
        case "proposition":
            setSidebarHeader("Proposition", 14);
            $("#proposition").fadeIn();
            loadPropositionSidebar();
            break;
        case "rule":
            setSidebarHeader("Regle", 8);
            $("#rule").fadeIn();
            loadRuleSidebar();
            break;
        case "comment":
            setSidebarHeader("Commentaire", 16);
            $("#comment").fadeIn();
            loadCommentSidebar();
            break;
        case "weight":
            setSidebarHeader("Ponderation", 15);
            $("#weight").fadeIn();
            loadWeightSidebar();
            break;
        case "welcome":
        default :
            setSidebarHeader("Inspecteur", 12);
            $("#welcome").fadeIn();
            break;
    }
}
// set sidebar title
//          * header : the title to be displayed
//          * w : the width of the title (for the title to be centered)
function setSidebarHeader(header, w) {
    $("#inspector").find("h1").text(header)
                              .css({width: w+"vh"});
}

// called when the user changed the active cell
function sideBarChangedCell(column, row) {
    if(!choosingCell && !ignoreCellChange) {
        var content = Cell(column, row).text();
        grid.onKeyDown.unsubscribe(keyDownCallback);
        inputFocus=false;
        cellContentChanged(selectedCell);

        if (content == null || content == "") {
            setSidebarSection("welcome");
        } else if (content.startsWith('=')) {
            setSidebarSection("rule");
        } else if (content.startsWith('$')) {
            setSidebarSection("weight");
        } else if (content.startsWith('//')) {
            setSidebarSection("comment");
        } else {
            setSidebarSection("proposition");
        }
    } else if(ignoreCellChange && selectedCell!=null) {     // prevent the active cell from changing
        selectedCell.activate();
    }

    ignoreCellChange=false;
}

// called when the user clicked on a cell
function sideBarSelectedCell(column, row) {
    if(choosingCell) {
        choosingCell = choosingCellCallback(column, row);
        ignoreCellChange=true;
    }
}

// allow user to pick a cell in the grid and disable the default behaviour (change sidebar)
//          * callback : a function called when the user clicked on a cell
//                  it should be like function(column, row) and return true
//                  to keep selecting cells afterwards, false otherwise
function chooseCell(callback) {
    choosingCell = true;
    choosingCellCallback = callback;
}

// select the cell currently edited
//          * id : the ID of the "select" button
//          * callback : a function called when a cell has been choosen
function selectCurrentCell(id, callback) {
    $("#"+id).addClass("btnSelected")
             .text = "selectionner ...";
    selectedCell = activeCell();
    chooseCell( function(column, row) {
        $("#"+id).text(Cell(column,row).name)
                 .removeClass("btnSelected");
        if(callback!=null)
            callback(column, row);
        return false;
    });
}

// mirror the activate content to a input field
//          * id: the ID of the input field
//          * formatter : a function to get the cell expression from the input value
//          * invFormatter : a function getting back the value from a cell expression
function bindInputToActiveCell(id, formatter, invFormatter) {
    // whenever the input field changes, the cell is changed
    $("#"+id).keyup( function() {
        activeCell().text(formatter($("#"+id).val()));
        grid.invalidate();
    });
    // whenever the active cell changes, the input field is changed
    grid.onKeyDown.unsubscribe(keyDownCallback);
    keyDownCallback = function(e, args) {
        $("#"+id).val(invFormatter(activeCell().text()));
    };
    grid.onKeyDown.subscribe(keyDownCallback);

    if(activeCell()!=null && activeCell().text()!=null) {
        $("#" + id).val(invFormatter(activeCell().text()));
    } else {
        $("#" + id).val("");
    }
}

// set up select cell button
//          * id : the ID of the button
function setupCellSelect(id) {
    // if any cell is selected, show it as the current cell
    if(grid.getActiveCell()!=null) {
        $("#"+id).text(activeCell().name);
    }
    // set select cell button event
    $("#"+id).click(function() {selectCurrentCell(id)});
}

// load content and register events when showing a new sidebar
function loadWelcomeSidebar() {
    $("#propBt").click(function() {setSidebarSection("proposition")});
    $("#ruleBt").click(function() {setSidebarSection("rule")});
    $("#weightBt").click(function() {setSidebarSection("weight")});
    $("#commentBt").click(function() {setSidebarSection("comment")});
    inputFocus=true;
}
function loadPropositionSidebar() {
    // unload previous event callbaks
    $("#propweight").off("change");

    // set select cell button event
    setupCellSelect("propcase");

    // set select weight cell button event and bind weight input to selected cell
    function setWeight(column, row) {
        var w = Cell(column, row);
        var reg = /[A-Z]([0-9]+)/i;
        var propCell = reg.exec(w.text());
        if(propCell!=null) {
            propCell=propCell[0];
        }

        if(w.text()==null || w.text()=="") { // if the cell is empty
            w.text("$" + activeCell().name+ ":" + $("#propweight").val());
            $("#propweight").focus();
            grid.invalidate();
        } else if(w.text().startsWith("$") && propCell == activeCell().name) { // if the selected cell already contains a weight
            $("#propweight").val(w.text().substring(w.text().indexOf(":")+1))
                            .focus();
        } else {                                // if the cell contains other stuff, cancel linking
            $("#propweightcell").text("case ...");
            return;
        }
        activeCell().setWeight(w.column, w.row);
        w.setProposition(activeCell().column, activeCell().row);
        $("#propweight").change(function() {
            w.text("$" + activeCell().name + ":" + $("#propweight").val());
            cellContentChanged(w);
            grid.invalidate();
        });
    }
    $("#propweightcell").click(function() {selectCurrentCell("propweightcell", setWeight)});

    if(activeCell().getWeight()!=null) {
        var w = activeCell().getWeight();
        $("#propweight").val(w.text().substring(w.text().indexOf(":")+1))
                        .change(function() {
                              w.text("$" + activeCell().name + ":" + $("#propweight").val());
                              grid.invalidate();
                              cellContentChanged(w);
                        });
        $("#propweightcell").text(w.name);
    } else {
        $("#propweight").val("");
        $("#propweightcell").text("case ...");
    }
    // mirror the content of the cell in the main textbox
    bindInputToActiveCell("propval", function(text) {return text}, function(text) {return text});

    if(inputFocus)
        $("#propval").focus();
    // load content into the list of rules using this proposition
    updatePropGrid();
}
function loadWeightSidebar() {

    $("#weightval")
        .off("change") // unload previous event callbaks
        .change(function() {     // set select weight cell button event and bind weight input to selected cell
            activeCell().text("$" + activeCell().getProposition().name + ":" + $("#weightval").val());

            updateWeight(activeCell().name,parseWeight(activeCell().text()));
            updateWeightGrid();

            grid.invalidate();
        });
    // set select cell button event
    setupCellSelect("weightcase");

    // set up select proposition action event
    function setProp(column, row) {
        var p = Cell(column, row);
        if(p.text()==null)
            p.text("");
        if(p.text().startsWith("$") || p.text().startsWith("=") || p.text().startsWith("//")) { // if cell already used and is not a proposition
            $("#weightproposition").text("Selectionner ...");
            $("#weight").find("p").text("Selectionnez la proposition que vous souhaitez ponderer");
        } else {                                // if the cell contains a proposition
            activeCell().setProposition(p.column, p.row);
            $("#weight").find("p").text(p.text());
            p.setWeight(activeCell().column, activeCell().row);
            grid.invalidate();
        }
    }
    $("#weightproposition").click(function() {selectCurrentCell("weightproposition", setProp)});

    // set up sidebar
    var activeText = activeCell().text();
    if(activeText!=null && activeText!= "") {
        var w = parseWeight(activeText);
        if(w!=null) {   // if weight is syntaxically correct, parse weight and fill the fields
            $("#weightval").val(w.value);
            $("#weightproposition").text(cellFromArray(w.proposition).name);
            $("#weight").find("p").text(cellFromArray(w.proposition).text());
        } else {        // otherwise, try with a more flexible method
            $("#weightval").val(activeText.substring(activeText.indexOf(":") + 1));
            $("#weightproposition").text(activeCell().getProposition().name);
            $("#weight").find("p").text(activeCell().getProposition().text());
        }
    } else {
        activeCell().text("$:0");
        grid.invalidate();
        $("#weight").find("p").text("Selectionnez la proposition que vous souhaitez ponderer");
        $("#weightval").val(0);
    }
    updateWeightGrid();
    // mirror the content of the cell in the main textbox
    bindInputToActiveCell("propval", function(text) {return "lol "+ text}, function(text) {return text.substring(4)});
    // create and load content into the list of rules using this proposition
}
function loadCommentSidebar() {
    // set select cell button event
    setupCellSelect("commentcase");
    if(inputFocus)
        $("#commentval").focus();

    // mirror the content of the cell in the main textbox
    bindInputToActiveCell("commentval", function(text) {return "//"+text}, function(text) {return text.substring(2)});
}
function loadRuleSidebar() {
    // set select cell button event
    setupCellSelect("rulecase");

    //set up inputs fields
    function inputSetup(id, otherId, symbol, separator) {
        var field = $("#"+id);
        var otherField = $("#"+otherId);
        var lastAdditionIsClick = false;

        function refreshCell(field, otherField, symbol) {
            if(otherField.val() != "" && otherField.val()!=null ) { // if the other field was edited before
                activeCell().text(symbol + field.val());
                grid.invalidate();
                otherField.val("");
                lastAdditionIsClick = false;
                bindInputToActiveCell(id, function(t) {return symbol+t}, function(t) {return t.substring(2)});
            }
            updateRuleGrid(parseRule(activeCell().text()));
        }

        // allow user to click on the cells to add their name on the rule
        field.focus(function() {
            chooseCell(function(column, row) {
                refreshCell(field, otherField, symbol);

                if(lastAdditionIsClick)
                    field.val(field.val() + separator);
                field.val(field.val()+Cell(column, row).name);
                field.focus();

                activeCell().text(symbol+field.val());
                grid.invalidate();

                updateRuleGrid(parseRule(activeCell().text()));

                lastAdditionIsClick = true;
                return true;
            })
        })
        .click(function() {return false}) // absorb click (otherwise it would pass the event to the sidebar and disable cell picking)
        .keyup(function(e) {
            refreshCell(field, otherField, symbol);
            lastAdditionIsClick = false;

            updateRuleGrid(parseRule(activeCell().text()));

            if(e.which == 13) {
                field.blur();
                choosingCell = false;
                ignoreCellChange=false;
            }
        });
    }
    $("#rule").click(function() {
        ignoreCellChange=false;
        choosingCell = false;
    });

    inputSetup("ruleval", "rulesimpleval", "=!", " + ");
    inputSetup("rulesimpleval", "ruleval", "= ", " donc ");

    // set up the new sidebar
    var activeText = activeCell().text();
    if(activeText==null) {
        activeText = "=!";
        activeCell().text("=!");
    } else {
        updateRuleGrid(parseRule(activeCell().text()));
    }
    if(activeText.startsWith("=!")) { // the cell contains an incompatibility
        $("#rulesimpleval").val("");
        bindInputToActiveCell("ruleval", function(t) {return "=!"+t}, function(t) {return t.substring(2)});
        if(inputFocus)
            $("#ruleval").focus();
    } else {
        bindInputToActiveCell("rulesimpleval", function(t) {return "= "+t}, function(t) {return t.substring(2)});
        $("#ruleval").val("");
        if(inputFocus)
            $("#rulesimpleval").focus();
    }
}

function updateRuleGrid(rule) {
    var i;
    var data = ruleGridContent.data;

    for(i=0;i<rule.length;i++) {
        var element = rule[i];
        if(element.polarity) {
            data[i][""] = "et"
        } else {
            data[i][""] = "et non"
        }
        data[i]["Incompatibles"]=cellFromArray(element.cell).text();
        data[i]["Case"] = element.name;
    }
    for(i;i<data.length;i++) {
        data[i]["Incompatibles"]="";
        data[i]["Case"]="";
        data[i][""]="";
    }
    data[0][""] = "";
    ruleGridContent.grid.invalidate();
}
function updateWeightGrid() {
    var sorted = Object.keys(weights).sort(function(a,b){return weights[a].value-weights[b].value});
    var data = weightGridContent.data;

    for(var i=0;i<sorted.length;i++) {
        data[i]["Poids"]=weights[sorted[i]].value;
        data[i]["Proposition"]=cellFromArray(weights[sorted[i]].proposition).text();
        if(sorted[i]==activeCell().name) {
            weightGridContent.grid.setActiveCell(i,0);
        }
    }
    for(i;i<data.length;i++) {
        data[i]["Poids"]="";
        data[i]["Proposition"]="";
    }
    weightGridContent.grid.invalidate();
}
function updatePropGrid() {
    var data = propGridContent.data;
    var j=0;
    for(var cell in rules) {
        for(var i in rules[cell]) {
            if(rules[cell][i].name==activeCell().name) {
                data[j]["Regle"] = cellNamed(cell).text();
                data[j]["Case"] = cell;
                j++;
            }
        }
    }
    for(j;j<data.length;j++) {
        data[j]["Regle"]="";
        data[j]["Case"]="";
    }
    propGridContent.grid.invalidate();
}