$(document).ready( function() {
    $(".btn_read").click( function() {
        var btn = $(this);
        var text = $(this).text();
        var id = $(this).attr("id");
        if(btn.hasClass("btn-success")) {
            var value = "False";
            btn.prop("disabled", true);
            $.get("/set_interest_read?id="+id+"&value="+value, 
                  function( data ) {
                      if(data == "OK") {
                          btn.text("Oläst");
                          btn.removeClass("btn-success");
                          btn.addClass("btn-primary");
                          update_interest_count(1);
                      }
                      btn.prop("disabled", false);
                  });
        }
        else {
            var value = "True";
            btn.prop("disabled", true);
            $.get("/set_interest_read?id="+id+"&value="+value, 
                  function( data ) {
                      if(data == "OK") {
                          btn.text("Läst");
                          btn.removeClass("btn-primary");
                          btn.addClass("btn-success");
                          update_interest_count(-1);
                      }
                      btn.prop("disabled", false);
                  });
        }
    });
});
