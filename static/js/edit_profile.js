function change_password_dialog() { 
    BootstrapDialog.show({
        title: "Byta lösenord",
        message: function(dialog) {
            var $message = $('<div></div>');
            var pageToLoad = dialog.getData('pageToLoad');
            $message.load(pageToLoad);
            return $message;
        },
        data: {
            'pageToLoad': '/change_password_dialog'
        }
    });
}

$(document).ready( function() {
    $("#change_password").click(change_password_dialog);
    $(".setting_field").each( function() {
        var field = $(this);
        var lbl = $("#lbl_field", field); 
        var input = $("#txt_field", field); 
        $("#btn_edit",this).click( function() {
            if(lbl.is(":visible")) {
                lbl.hide();
                input.show();
                input.focus();
                $("img",this).attr("src",
                                   "/static/img/glyphicons_206_ok_2.png");
            }
            else {
                var button_pressed = $(this);
                button_pressed.prop("disabled", true);
                var email = '{{profile["email"]}}';
                var field_name = $("#field_name", field).html();
                var value = input.val();
                if($.trim(lbl.text()) != value) {
                    alert(lbl.text() + "  " + value);
                    $.get("/edit_profile?email=" + email
                          +"&field=" + field_name + "&value=" + value,
                          function(data) {
                              var value = input.val();
                              input.hide();
                              lbl.show();
                              lbl.text(value);
                              $("img", button_pressed).attr("src",
							    "/static/img/glyphicons_030_pencil.png");
                              button_pressed.prop("disabled", false);
			  });
                }
                else {
                    var value = input.val();
                    input.hide();
                    lbl.show();
                    lbl.text(value);
                    $("img", button_pressed).attr("src",
                                                  "/static/img/glyphicons_030_pencil.png");
                    button_pressed.prop("disabled", false);
                    
                }
            }
        });
    });
});
