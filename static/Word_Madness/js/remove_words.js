function select_word() {
    var s = window.getSelection();
    var range = s.getRangeAt(0);
    var node = s.anchorNode;

    while (range.toString().indexOf(' ') != 0) {
        range.setStart(node, (range.startOffset - 1));
    }
    range.setStart(node, range.startOffset + 1);

    do {
        range.setEnd(node, range.endOffset + 1);
    } while (range.toString().indexOf(' ') == -1 && 
            range.toString().trim() != '' && range.endOffset < node.length);
    if (range.toString().indexOf(' ') != -1) {
        range.setEnd(node, range.endOffset - 1);
    }

    return range;
}

function a() {
    var range = select_word();
    var str = range.toString().trim();
    var newnode = document.createElement("a");
    newnode.className = "blank_word";
    range.surroundContents(newnode);
}

$(document).ready(function() {
    $("#story").on( "click", function(){
        a();
    });
});
