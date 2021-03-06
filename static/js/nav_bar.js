function update_interest_count(n) {
    var count = parseInt($("#interest_count").html());
    count += n;
    $("#interest_count").html(count);
};

function interest_dialog() { 
    BootstrapDialog.show({
        title: "Intresseanmälan",
        message: function(dialog) {
            var $message = $('<div></div>');
            var pageToLoad = dialog.getData('pageToLoad');
            $message.load(pageToLoad);
            return $message;
        },
        data: {
            'pageToLoad': '/interest_dialog'
        }
    });
}

$(document).ready(function() {
    if($("#admin_nav").length > 0) {
        $("#admin_nav").click( function() {
            if(!$(this).hasClass("active")) {
                $("#nav_option li").each( function() {
                    $(this).removeClass("active");
                });
            }
            else {
                $(this).addClass("active");
            }
        });
    }
    
    if($("#login_field").length > 0) {
        $("#login_btn").click( function() {
            var user = $("#user_input").val();
            var passw = $("#passw_input").val();
            
            $.post("/login", {"user":user, "passw":passw}, function(data) {
                if (data != "True") {
                    $("#wrong_login").show();
                }
                else {
                    location.reload(true);
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

    $(".register_click").click(interest_dialog);
});
