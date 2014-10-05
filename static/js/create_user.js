$(document).ready(function() {
    $('#create_user_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            username: {
                message: 'The username is not valid',
                validators: {
                    notEmpty: {
                        message: 'The username is required and cannot be empty'
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: 'The username must be more than 6 and less than 30 characters long'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9]+$/,
                        message: 'The username can only consist of alphabetical and number'
                    },
                    different: {
                        field: 'password',
                        message: 'The username and password cannot be the same as each other'
                    }
                }
            },
            first_name: {
                message: 'Förnamn får ej vara tomt',
                validators: {
                    notEmpty: {
                        message: "Du måste fylla i förnamnet"
                    }
                }
            },
            last_name: {
                message: 'Efternamnet får ej vara tomt.',
                validators: {
                    notEmpty: {
                        message: "Du måste fylla i efternamnet"
                    }
                }
            },
            postal: {
                validators: {
                    regexp: {
                        regexp: /^[0-9]+$/,
                        message: 'Endast siffror i postnummer'
                    }
                }
            },
            road_number: {
                validators: {
                    regexp: {
                        regexp: /^[0-9]+$/,
                        message: 'Endast siffror'
                    }
                }
            },
            phone: {
                message: 'Telefonnummret är inte giltigt',
                validators: {
                    regexp: {
                        regexp: /^[0-9]+$/,
                        message: 'Endast siffror i ett telefonnummer'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'Du måste fylla i en email-address'
                    },
                    emailAddress: {
                        message: 'Email-addressen är felaktig'
                    }
                }
            },
            password: {
                validators: {
                    notEmpty: {
                        message: 'Du måste fylla i lösenord'
                    },
                    different: {
                        field: 'email',
                        message: 'Lösenordet får inte vara samma som email.'
                    },
                    stringLength: {
                        min: 5,
                        message: 'Lösenordet måste vara minst 5 tecken långt'
                    }
                }
            }
        }
    });
});
