$(document).ready(function() {
    $('#passwordForm').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
	    old_password: {
		message: " ",
		validators: {
		    notEmpty: {
                        message: "Får inte vara tomt."
                    }
		}
	    },
            new_password: {
                message: 'The username is not valid',
                validators: {
		    notEmpty: {
                        message: "Får inte vara tomt."
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: 'Lösenordet måsta vara minst 6 tecken långt'
                    },
                    different: {
                        field: 'old_password',
                        message: 'Lösenordet får inte vara samma som tidigare'
                    }
                }
            },
            new_password_ver: {
                message: '  ',
                validators: {
                    notEmpty: {
                        message: "Får inte vara tomt."
                    },
		    identical: {
			field: "new_password",
                        message: "Matchar inte med det nya lösenordet"
                    }
                }
            }
        }
    });
});
