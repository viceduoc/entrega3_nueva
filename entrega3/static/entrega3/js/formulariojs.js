console.log('prueba')


$().ready(function () {

    $("form[name='formulario']").validate({
        rules:{
            nombre: "required",
            apellido: "required",
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            },
            phone: {
                required: true,
                number: true,
                minlength: 9,
                maxlength:9
            },
            area:{
                required: true,
                minlength: 50,
                maxlength: 500
            },
            check :{
                required: true
            }


        },
        messages: {
            nombre: "Por favor ingresa un nombre",
            apellido: "Por favor ingresa tu apellido",
            email: "Por favor agrega un email",
            password: {
                required: "Por favor crea una contraseña",
                minlength: "Debe tener la menos 5 caracteres"
            },
            phone: "Debes 9 números",
            area: "Por favor cuentanos algo",
            check: "Campo obligatorio "

        },
        submitHandler: function (form) {
            form.submit();
        }
    });

    $("#btnclean").click(function(){
        $("label.error").hide();
    })
});