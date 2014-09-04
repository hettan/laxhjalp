$(document).ready( function() {
    $(".setting_field").each( function() {
        var field = $(this);
        var lbl = $("#lbl_field",field); 
        var input = $("#txt_field",field); 
        $("#btn_edit",this).click( function() {
            if(lbl.is(":visible")) {
                lbl.hide();
                input.show();
                input.focus();
                $("img",this).attr("src",
                                        "static/img/glyphicons_206_ok_2.png");
            }
            else {
                var value = input.val();
                input.hide();
                lbl.show();
                lbl.text(value);
                $("img",this).attr("src",
                                        "static/img/glyphicons_030_pencil.png");
            }
        });
    });
});
