$(function(){



//ACCEDO AL FORMULARIO  POR SU NOMBRE
$("form[name='form-modal']").validate({

    //  ESPECIFICO LAS VALIDACIONES
    rules:{
        //llamo a cada campo por su nombre
        contrasenaValidation: "required",
        emailValidation: {
            required: true,
            email: true
        },
        
        

    },//CIERRA RULES

        //mensajes de error
        messages: {
            contrasenaValidation: "Debe escribir su contraseña",
            emailValidation: "Debe esribir su correo con el formato adecuado"
        }, //CIERRA MESSAGES
        submitHandler: function(form){
            form.submit();
            
        }
});
//ELIMINO LOS LABELS DE ERRORES
$("#modalCancel").click(function(){
    $("label.error").hide();
    $('#modalLoginEmail').val('');
    $('#modalLoginPswd').val('');


})


})