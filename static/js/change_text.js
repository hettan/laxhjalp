function update_field(page, field, value) {
    $.get("/update_page?page="+page+"&field="+field+"&value="+value, function( data ) {
	console.log(data);
    });
}

$(document).ready( function() {
    $(".edit_btn").click( function() {
	var text_field = $(".form-control" ,$(this).parent())
	var page = $(this).data("page");
	var field = $(this).data("field");
	var value = text_field.val();
	update_field(page, field, value);
	$(this).hide();
    });
    $(".form-control").change(function() {
	$("button", $(this).parent()).show();
    });    
});

