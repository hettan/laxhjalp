$(document).ready( function() {
    $(".btn_read").click( function() {
        var btn = $(this);
        var text = $(this).text();
        if(btn.hasClass("btn-success")) {
            btn.text("Oläst");
            btn.removeClass("btn-success");
            btn.addClass("btn-primary");
        }
        else {
            btn.text("Läst");
            btn.removeClass("btn-primary");
            btn.addClass("btn-success");
        }
    });
});
