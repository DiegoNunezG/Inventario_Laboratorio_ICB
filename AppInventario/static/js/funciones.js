let boton_editar = document.getElementById("botoneditarmarca");
let input_id = document.getElementById("inputidmarca");
let input_modal_marca = document.getElementById("inputmodalmarca");
let input_nombre_marca = document.getElementById("inputnombremarca");
boton_editar.addEventListener("click", cargar_modal);
console.log(input_modal_marca);
console.log(boton_editar);
console.log(input_nombre_marca);
console.log(input_id);
function cargar_modal() {
    input_modal_marca.value = input_nombre_marca.value;
    console.log(input_modal_marca)
}