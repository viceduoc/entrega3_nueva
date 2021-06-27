$(document).ready(function(){

    const APINOTICIAS = 'https://patriciomardonesduoc.github.io/noticias/';

    console.log('Cargando noticias');
    var rowNoticias = $('#row-noticias');
    var cardNoticiaGrande = $('#noticia-grande');
    var cardNoticia1 = $('#noticia-chica-1');
    var CardNoticia2 = $('#noticia-chica-2');

    $.get({
        url: APINOTICIAS + "noticias.json",
        success: function(response){       
            console.log('Respuesta correcta');
            // pinto las 3 principales
            let notPrincipales = [];
            notPrincipales = response.noticias;
            console.log(notPrincipales[0].imagen);

            var i;
            for (i = 0; i < notPrincipales.length; i++) {
                if(notPrincipales[i].titulo.length > 40){
                    notPrincipales[i].titulo = notPrincipales[i].titulo.substring(0, 40) + "..."
                }
            }

            //pathImage = APINOTICIAS + noticia.imagen;
            $('#not-imagen-1').attr('src', APINOTICIAS + notPrincipales[0].imagen);
            $('#not-titulo-1').append(notPrincipales[0].titulo);
            $('#not-imagen-c1').attr('src', APINOTICIAS + notPrincipales[1].imagen);
            $('#not-titulo-c1').append(notPrincipales[1].titulo);
            $('#not-imagen-c2').attr('src', APINOTICIAS + notPrincipales[2].imagen);
            $('#not-titulo-c2').append(notPrincipales[2].titulo);
            //console.log(pathImage);

            // Pinto las noticias cortas
            $.each(response.noticias, function(index, noticia){
                
                $('#noticias-cortas').append('<div class="col-md-3 col-12 mt-2>' + 
                    '<div class="card" id="'+  noticia.idnot +'">' +
                    '<img src="'+ APINOTICIAS + noticia.imagen +'" class="card-img-top" alt="'+ noticia.titulo +'" ></img>' +
                    '<div class="card-body">' + 
                    '<p class="card-text">' + noticia.titulo + '</p></div></div></div>'
                );
                
            })
            
        },
        error: function(){console.log('Error al traer' )}
    })

})

