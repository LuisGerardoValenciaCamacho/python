function limpiarForm()
{
	document.getElementById("nombre").value="";
	document.getElementById("apellidos").value="";
	document.getElementById("fechaNacimiento").value="";
	document.getElementById("masculino").checked=true;
	document.getElementById("femenino").checked=false;
}

function validaMensaje(mensaje)
{
	if(mensaje != null && mensaje != 'null' && mensaje != "")
	{
		alert(mensaje);
	}
}

function validarCrearUsuario()
{
	var nombres = document.getElementById("nombre").value;
	var apellidos = document.getElementById("apellidos").value;
	var fechaNacimiento = document.getElementById("fechaNacimiento").value;
	if(nombres == '')
	{
		alert("El campo 'Nombres' es requerido")
		return;
	}
	if(apellidos == '')
	{
		alert("El campo 'Apellidos' es requerido")
		return;
	}
	if(fechaNacimiento == '')
	{
		alert("El campo 'Fecha de nacimiento' es requerido")
		return;
	}
	alert("Usuario guardado")
	document.getElementById("formularioUsuarios").submit();
}

function borrarUsuario(id, nombre, apellido)
{
	var res = confirm("¿Seguro de borrar el usuario '" + nombre + " " + apellido + "?");
	if(res == true)
	{
		document.getElementById("idUsuario").value = id;
		document.getElementById("formularioUsuarios").action = "borrar-usuario";
		document.getElementById("formularioUsuarios").submit();
	}
}