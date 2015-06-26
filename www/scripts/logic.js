var rules = {};
var propositions={};
var weights={};

function parseRule(text) {
    var rule = [];
    if(text.startsWith("=!")) {
        text = text.replace(/\s+/g, "").substring(2);
        var reg = /(-|\+)?[A-Z]([0-9]+)/i;
        while(text.length >0) {
            var element = reg.exec(text);
            if(element!=null) {
                element = element[0];
                if (element.startsWith("-")) {
                    rule.push({
                        polarity: false,
                        cell: cellNameToArray(element.substring(1)),
                        name: element.substring(1)
                    });
                } else if (element.startsWith("+")) {
                    rule.push({
                        polarity: true,
                        cell: cellNameToArray(element.substring(1)),
                        name: element.substring(1)
                    });
                } else {
                    rule.push({
                        polarity: true,
                        cell: cellNameToArray(element),
                        name: element
                    });
                }
                text = text.substring(element.length);
            } else {
                break;
            }

        }
    } else if(text.startsWith("= ")) {
        text = text.replace(/\s+/g, "").substring(1);
        var donc = /donc/i;
        var ou = /ou/i;

        function getArgs(text) {
            var cell = /[A-Z]([0-9]+)/i;
            var element1 = cell.exec(text);
            if(element1!=null) {
                element1 = element1[0];
                text = text.substring(element1.length);
                var element2 = cell.exec(text);
                if (element2 != null) {
                    element2 = element2[0];
                    return [element1, element2];
                }
            }
        }

        var args = getArgs(text);
        if(args!=null && donc.test(text)) {
            rule = [
                {
                    polarity: true,
                    cell: cellNameToArray(args[0]),
                    name: args[0]
                },
                {
                    polarity: false,
                    cell: cellNameToArray(args[1]),
                    name: args[1]
                }
            ];
        } else if(args!=null && ou.test(text)) {
            rule = [
                {
                    polarity: false,
                    cell: cellNameToArray(args[0]),
                    name: args[0]
                },
                {
                    polarity: false,
                    cell: cellNameToArray(args[1]),
                    name: args[1]
                }
            ];
        }
    }
    return rule;
}

function parseWeight(text) {
    var reg = /[A-Z]([0-9]+)/i;
    var value = parseInt(text.substring(text.indexOf(":")+1));
    var propCell = reg.exec(text);
    if(propCell!=null && value!=null) {
        return { proposition: cellNameToArray(propCell[0]), value:value};
    }
}

function ruleToText(rule) {
    var index;
    var text = "=R(";
    for(index in rule) {
        var element = rule[index];
        if(!element.polarity) {
            text+="-";
        }
        text+= element.name + ",";
    }
    return text.substring(0,text.length-1) + ")";
}

function weightToText(weight) {
    return "=$" + weight.value + cellFromArray(weight.proposition).name;
}

function parseCell(cell) {
    var content = cell.text();

    if (content == null || content == "" || content.startsWith('//')) {
        return;
    } else if (content.startsWith('=')) {
        var rule = parseRule(content);
        updateRule(cell.name, rule);
        if(rule!=[])
            return ruleToText(rule);
    } else if (content.startsWith('$')) {
        var weight =  parseWeight(content);
        updateWeight(cell.name,weight);

        if(weight!=null)
            return weightToText(weight);
    } else {
        updateProposition(cell.name, content);
        return content;
    }
}

$(function() {
    grid.onCellChange.subscribe(function(e,args){
        cellContentChanged(Cell(args.cell, args.row))
    });
});
function cellContentChanged(changed) {
    var content = parseCell(changed);

    console.log(content);

    if(content==null)
        content="";

    sendCell(changed, content);
    changed.setFormat("sent");
    grid.invalidate();
}

function updateRule(cell, rule) {
    if(rule!=[])
        rules[cell] = rule;
    else
        rules[cell] = null;

}
function updateWeight(cell, weight) {
    if(weight!=null) {
        weights[cell] = weight;
        if(propositions[weight.proposition]!=null) {
            propositions[weight.proposition].weight = cell;
        }
    } else
        weights[cell] = null;
}
function updateProposition(cell, proposition) {
    propositions[cell] = proposition;
}