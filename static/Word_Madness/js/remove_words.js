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

    while ( (range.toString().indexOf(' ') !== 0) && (range.startOffset > 0) ) {
        range.setStart(node, (range.startOffset - 1));
    }
    if(range.toString().indexOf(' ')===0) {
        range.setStart(node, range.startOffset + 1);
    }

    do {
        range.setEnd(node, range.endOffset + 1);
    } while (range.toString().indexOf(' ') == -1 && 
            range.toString().trim() != '' && range.endOffset < node.length);
    if (range.toString().indexOf(' ') != -1) {
        range.setEnd(node, range.endOffset - 1);
    }

    return range;
}

function create_table_row(counter, word) {
    var result = "<tr><td>" + counter + "</td><td><input type=\"text\" name=\"word_" + counter + "\" value = \"" + word + "\" readonly></td>";
    var opts = $("#hidden_data").text().split(";");
    result = result + "<td><select name='Part_of_Speech_" + counter + "'>";
    opts.forEach(function(element, index, array) {
        result = result + "<option value='" + element + "'>" + element 
            + "</option>";
    });
    result = result + "</select></td>";
    result = result + "<td><a href=\"javascript:void(0);\" class=\"deletelink\" onclick=\"remove_row(this);\">";
    result = result + "Delete</a></td>";
    result = result + "</tr>";

    return result;
}

function a() {
    var range = select_word();
    var str = range.toString().trim();
    var newnode = document.createElement("a");
    var cntr = Counter.get()
    range.surroundContents(newnode);
    $(newnode).attr("id", Counter.get()).attr("class", "blank_word");
    $(newnode).text("___(" + cntr + ")___");
    $("#Words tr:last").after(create_table_row(cntr, str));
    $( "#story_body" ).val($( "#story" ).html());
    Counter.increment();
}

function remove_row(clicked_element) {
    var element = clicked_element;
    while(element.tagName != "TR") {
        element = element.parentElement;
    }
    $( "#" + element.childNodes[0].innerText ).replaceWith(element.childNodes[1].childNodes[0].value);
    element.parentElement.removeChild(element);
    $( "#story_body" ).val($( "#story" ).html());
}

function sbmt_form(event) {
    event.preventDefault();
    $( "#story_body" ).val($( "#story" ).html());
    $( "form" ).submit();
}

$(document).ready(function() {
    $("#story").on( "click", function(){
        a();
    });
});
