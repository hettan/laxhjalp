$(document).ready(function() {
    $("#logged_in_field").hide();
    $("#wrong_login").hide();
    $('input[type="submit"]').attr('disabled','disabled');
    
    if($("#login_field").length > 0) {
        $("#login_btn").click( function() {
            var user = $("#user_input").val();
            var passw = $("#passw_input").val();
            
            $.post("/login", {"user":user, "passw":passw}, function(data) {
                if (data == "True") {
                    $("#wrong_login").remove();
                    $("#login_field").remove();
                    $("#logged_in_field").show();
                    $("#user_display").html(user);
                }
                else {
                    $("#wrong_login").show();
                }
            });
        });
    }
    else {
        $("#logged_in_field").show();
    }

    $("#logout_btn").click( function() {
        $.get("/logout", function() {
            location.reload(true);
        });
    });
});
