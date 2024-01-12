
/*$(document).ready(function(){
  $("#etiqueta").submit(function(e){
      e.preventDefault();




  })





})





$(document).ready(function(){

  $('.borrador').click(function () {
  //var close=$(this).parent();
  if (confirm("Are you sure you want to delete this?")){
    $.ajax({

      url: $(this).attr('action'),
    type: $(this).attr('method'),
    data: $(this).serialize(x), 
    dataType: "json",
            //url: $(this).data('url'),
      beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
      },
      success: function(data) {
        $('#fila_a_ocultar').hide();
      }
    });
  }
});
});














$("#etiqueta").click(function () {
  //var close=$(this).parent();
  if (confirm("Are you sure you want to delete this?")){
    $.ajax({

      url: $(this).attr('action'),
    type: $(this).attr('method'),
    data: $(this).serialize(), 
            //url: $(this).data('url'),
      beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
      },
      success: function() {
        data.hide();
      }
    });
  }
});



        /*success: function(json){
          console.log(json)
          }*/

/*

//--------------------------------------------------------------
UNA BUENA IDEA SI TUVIERA TODOS LOS CAMPOS
MOSTRADOS EN EL DOM

function borrar_previo(){
  //arreglo = [#apellidoz, #paiz, #cell, #nomusuario, #rolsys]
  
  arreglo = [id, nombre]
  var cantidad_items = arreglo;

  for (var i = 0; i < cantidad_items.length; i++) {

    $("arreglo[i]").remove(data[0].cantidad_items[i]);

  };

}

//---------------------------------------------------------

(chequear que el canal este vacio, por ejemplo, antes de enviar algo al backend)
LO QUE HAY QUE HACER ES EN EL DOM MANDAR A ESCONDER EL ITEM
Y MIENTRAS ESTA ESCONDIDO  MANDAR A QUE EN EL BACKEND SE EJECUTE UNA RUTINA DE BORRADO COMPLETO AL ESTILO DE AQUEL user.delete()


---------------------------------------------------------------

  nombre = models.CharField(max_length=20)
  apellidos = models.CharField(max_length= 30)
  edad = models.IntegerField()
  sexo = models.CharField(max_length=1)
  profesion = models.CharField(max_length=30)
  fecha_nacimiento = models.DateTimeField()
  pais = models.CharField(max_length=30)
  ciudad_procedencia = models.CharField(max_length=30)
  numero_celular = models.CharField(max_length=30)
  nombre_usuario_sys = models.CharField(max_length=30)
  rol= models.CharField(max_length=10)
  password = models.CharField(max_length=30)
  fecha_creacion_usuario = models.DateTimeField()

*/

          /*success: function(data){
      
            $("#apellidoz").remove(data[0].apellidos);
            $("#paiz").remove(data[0].pais);
            $("#cell").remove(data[0].numero_celular);
            $("#nomusuario").remove(data[0].nombre_usuario_sys);
            $("#rolsys").remove(data[0].rol);

          } */

          //success: function(){
          //  alert("ya funciona AJAX, solo queda efectuar borrado");
          //}

          //success: function(data){
            //aqui hay que iterar en un json
            //para borrar el json




            /*

            OPERACION SUBIENDO_NIVEL:
            
            -HAY QUE TRABAJAR EN JAVA SCRIPT ORIENTADO A EVENTOS EN UN JSON Y GUARDANDO DATOS JSON EN LA CACHE DEL NAVEGADOR, Y MANIPULANDO ESE JSON EN LA CACHE

            -chequear que la conexion este limpia desde el frontend al backend, poniendo un setTimeOut y durante ese tiempo reviso si se puede ejecutar la operacion, y si el timeOut se vence, pues decir que no se pudo borrar, que lo vuelva a intentar
            
            SI SE PUEDE HACER:
            -almacenar el nombre de usuario (NICKNAME) en la cache del navegador
            -borrar el json en el frontend

            -si el borrado fue exitoso, mandar a ejecutar una funcion que esta en el backend, que es la que borra todo el item de la BD

            -y que es funcion renderice una plantilla que diga que el usuario ha sido borrado, y hiperlinke a listarusuarios 

            -[SI ES POSIBLE HACER QUE ESA FUNCION EJECUTE LA OPERACION DE BORRADO EN VARIOS HILOS DE EJECUCION, EN CASO DE QUE EXISTA MAS DE UNA CONEXION AL BACKEND:---SIMULARLO PARA VERLO----]

            -[ SI ES POSIBLE CREAR UN DEMONIO EN AJAX QUE DURANTE TODA LA TRANSACCION VERIFIQUE EL ESTADO DE LA CONEXION ENTRE SERVIDOR Y CLIENTE, Y USANDO UN ALGORITMO DE RECONOCIMIENTO DE PATRONES DETECTE EL MOMENTO MAS OPTIMO (EL DE MENOS TRAFICO) PARA ENVIAR LOS DATOS, Y ASI LLEGAN SIN DAÑO. VAYA: SIMPLEMENTE USAR KNN
            ]



            */
            /*$("#apellidoz").remove(data[0].apellidos);
            $("#paiz").remove(data[0].pais);
            $("#cell").remove(data[0].numero_celular);
            $("#nomusuario").remove(data[0].nombre_usuario_sys);
            $("#rolsys").remove(data[0].rol);
            
          */

        //    alert("el usuario ha sido borrado");
            /*for (var i = 0; i < data.length; i++) 
            {

              
              alert ("el"+" "+ data[i].text+ " "+"es borrado");
              console.log(data);
              //delete data[i];


            };*/
            //alert("el usuario ha sido borrado");

  /*        }

      })

  })


})

*/


  //var btn = $(this);

  /*$.ajax({
    //csrfmiddlewaretoken: '{{ csrf_token }}',
    /*url: "http://localhost:8000"+btn.attr("href"),
    type: "POST",
    dataType: 'json',   */
    /*
    beforeSend: function(){
      if 
    }*/

          /*url: $(this).attr('action'),
          type: $(this).attr('method'),
        //  data: $(this).serialize(), */
/*
    success: function(data){
      function()
      $("#apellidoz").remove(data[0].apellidos);
      $("#paiz").remove(data[0].pais);
      $("#cell").remove(data[0].numero_celular);
      $("#nomusuario").remove(data[0].nombre_usuario_sys);
      $("#rolsys").remove(data[0].rol);
      

      $("#nombre_et").remove(data[0].nombre);
      $("#edad_et").remove(data[0].edad);
      $("#sexo_et").remove(data[0].sexo);
      $("#profesion_et").remove(data[0].profesion);
      $("#nacimiento_et").remove(data[0].fecha_nacimiento);
      $("#ciudad_et").remove(data[0].ciudad_procedencia);
      $("#password_et").remove(data[0].password);
      $("#creacion_et").remove(data[0].fecha_creacion_usuario);

      }

    */

        //success: function(json){
          //console.log(json)
        //}


  //  });

//});





