
function add_user_dialog() { 
    BootstrapDialog.show({
        title: "Lägg till användare",
        message: function(dialog) {
            var $message = $('<div></div>');
            var pageToLoad = dialog.getData('pageToLoad');
            $message.load(pageToLoad);
            return $message;
        },
        data: {
            'pageToLoad': '/add_user_dialog'
        }
    });
}

$(document).ready(function() {
    $(".add_user_click").click(add_user_dialog());
});
