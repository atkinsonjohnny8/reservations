

	
		$(document).on("ready", resultado);

		function resultado(){
		$('.apireq').click( function() {
			$.ajax({
				url: $(this).attr('action'),
                //type: $(this).attr('method'),
               // data: $(this).serialize(),

				//url : "http://localhost:8000/studentsapi",
				dataType: "json",
				success : function (datos) {
						$('#elid').text( datos[0].id);
						$('#nombre').text( datos[0].nombre);
						$('#apellidoz').text( datos[0].apellidos);
						$('#paiz').text( datos[0].pais);

						$('#cell').text( datos[0].numero_celular);
						$('#nomusuario').text( datos[0].nombre_usuario_sys);
						$('#rolsys').text( datos[0].rol);
						$('#sex').text( datos[0].sexo);
						$('#procedencia').text( datos[0].ciudad_procedencia);
						$('#profesion').text( datos[0].profesion);
						}
				});
			});	
		}
