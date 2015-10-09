
function select_word() {
        console.log("I'm in");
        var s = window.getSelection();
        var range = s.getRangeAt(0);
        var node = s.anchorNode;
        while (range.toString().indexOf(' ') != 0) {
            range.setStart(node, (range.startOffset - 1));
        }
        range.setStart(node, range.startOffset + 1);
        do {
            range.setEnd(node, range.endOffset + 1);

        } while (range.toString().indexOf(' ') == -1 && range.toString().trim() != '' && range.endOffset < node.length);
        var str = range.toString().trim();
        alert(str);
}

$(document).ready(function() {
    console.log("Page is ready");

    $("#story").on( "click", function(){
        console.log("I've been clicked");
        select_word();
    });
        
    console.log("I'm out");
});
