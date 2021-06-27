$(document).ready(function(){

    const APINOTICIAS = 'https://newsapi.org/v2/top-headlines/';
    const APIKEY = "3ab0eff9a7e84522854225c5d45cfece";


    console.log('Cargando noticias');


    $.get({
        url: `${APINOTICIAS}?country=us&category=technology&apiKey=${APIKEY}`,
        success: function(response){       
            console.log('Respuesta correcta');
            // pinto las 3 principales
            
            let notPrincipales = [];
            notPrincipales = response.articles;

            var i;
            for (i = 0; i < 3; i++) {
                if(notPrincipales[i].title.length > 40){
                    notPrincipales[i].title = notPrincipales[i].title.substring(0, 40) + "..."
                }
            }
            //pathImage = APINOTICIAS + noticia.imagen;
            $('#not-imagen-1').attr('src', notPrincipales[0].urlToImage);
            $('#not-titulo-1').append(notPrincipales[0].title);
            $('#not-imagen-c1').attr('src',notPrincipales[1].urlToImage);
            $('#not-titulo-c1').append(notPrincipales[1].title);
            $('#not-imagen-c2').attr('src', notPrincipales[2].urlToImage);
            $('#not-titulo-c2').append(notPrincipales[2].title);
            //console.log(pathImage);
            
            // Pinto las noticias cortas
            $.each(response.articles, function(index, noticia){
    
                $('#noticias-cortas').append('<div class="col-md-3 col-12 mt-2>' + 
                    '<div class="card">' +
                    `<img src="${noticia.urlToImage}" class="card-img-top" alt="${noticia.title}" ></img>` +
                    '<div class="card-body">' + 
                    `<p class="card-text"><a href="${noticia.url}">${noticia.title}</a></p></div></div></div>`
                    
                );
                
            })

        },
        error: function(){console.log('Error al traer' )}
    })




})
