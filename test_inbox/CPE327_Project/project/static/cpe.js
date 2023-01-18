/*let lab = 3.1;*/

$(document).ready( function () {
    setNavigation();
    $('#maintable').DataTable();
    /*var data;
    data = document.getElementById("p1").innerHTML
    console.log(data + lab);
    document.getElementById("p1").innerHTML = "Lab 3.1";*/
    
    /*$("#p").click(function(){
      $("#p").hide();
    });

    $("#p").hide();*/
    /*$("#p1").text("Lab 3.1 by JS");
    $("#p1").load("https://nagatox.github.io/cpe231/allinvoice.json");*/

    /*$.get("https://nagatox.github.io/cpe231/allinvoice.json", function(data, status){
        console.log("Data: " + data + "\nStatus: " + status);
        var total = 0;
        $.each(data, function(key, val){
            console.log("key " + key + "\nval " + val["Extended Price"]);
            total = total + val["Extended Price"];
        });
        $("h1").text("total invoice = " + total);
      });*/
} );

function setNavigation() {
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path);

    $(".nav a").each(function () {
        var href = $(this).attr('href');
        if (path.substring(1, href.length+1) === href) {
            $(this).closest('li').addClass('active');
        }
    });
}
