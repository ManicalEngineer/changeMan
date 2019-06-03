



var ecr_stat = document.getElementById("id_status");
var dispo = document.getElementById("id_ecr_disposition");
var form = document.getElementsByTagName("form")[0];
var submit = document.getElementsByTagName("button")[2];
var token = document.getElementsByName("csrfmiddlewaretoken")[0];
var fElem = form.elements;
window.addEventListener('load', check_status);
ecr_stat.addEventListener('change', check_status);
submit.addEventListener('mousedown', enable);

console.log(submit)

function check_status() {

		if (ecr_stat.options[ecr_stat.selectedIndex].value !== "CL"){
			for (var i = 0; i < fElem.length-1; i++){
				fElem[i].disabled = false;
			}
			dispo.disabled = true;
			ecr_stat.disabled = false;
			token.disabled = false;

		}else{
			for (var i = 0; i < fElem.length-1; i++){
				fElem[i].disabled = true;
			}
			dispo.disabled = false;
			ecr_stat.disabled = false;
			token.disabled = false;
		}
	}

function enable() {

	for (var i = 0; i < fElem.length; i++){
		console.log("another");
		fElem[i].disabled = false;
	}
}