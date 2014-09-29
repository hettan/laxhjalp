function update_field(page, field, value) {
    $.post("/update_page", {"page_name": page, "field": field, "value": value})
	.done(function( data ) {
	    alert(data);
	});
}
/*
$(document).ready( function() {
    
    
});
*/
