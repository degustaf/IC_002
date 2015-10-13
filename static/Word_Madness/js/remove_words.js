var Counter = (function(){
    var clicked = 0;
    function reset (){
        clicked = 0;
    }
    function increment() {
        clicked = clicked + 1;
    }
    function getClicked (){
        return clicked;
    }
    return{
        reset: reset,
        increment: increment,
        get: getClicked
    }

}());

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
    range.surroundContents(newnode);
    $(newnode).attr("id", Counter.get()).attr("class", "blank_word");
    $(newnode).text("___(" + Counter.get() + ")___")
    Counter.increment();
}

$(document).ready(function() {
    $("#story").on( "click", function(){
        a();
    });
});
