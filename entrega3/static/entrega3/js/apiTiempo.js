$(document).ready(function(){

    var container = $("#api-tiempo")
    var titleApi = $("#ubicacion")

    const settings = {
        "async": true,
        "crossDomain": true,
        "url": "https://weatherapi-com.p.rapidapi.com/forecast.json?q=santiago&days=3&lang=es",
        "method": "GET",
        "headers": {
            "x-rapidapi-key": "41fc09421amsh62e9ada02fa463bp120f7fjsn1604d9ade37a",
            "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
        }
    };
    
    $.ajax(settings).done(function (data) {
        console.log(data);
        titleApi.text(`Clima para :  ${data.location.name}, ${data.location.country}`)
        $.each(data.forecast.forecastday, function(index, value) {

            container.append(` <div class="col-md-4 col-12 mt-2">
            <div class="card text-center border-0">
            <img src="${value.day.condition.icon}" class="card-img-top p-0" alt="..." style="margin: 10px  auto  20px;max-width: 40%">
            <div class="card-body p-0">
            <h5 class="card-title">${value.date}</h5>
            <p class="card-text">${value.day.condition.text}</p>
            <span> Mínima ${value.day.mintemp_c}</span> |
            <span>Máxima ${value.day.maxtemp_c} </span>
            </div>
        </div>
        </div>`)

        })
    });



})