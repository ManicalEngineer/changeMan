



var ecr_stat = document.getElementById("id_status");
var dispo = document.getElementById("id_ecr_disposition");
var form = document.getElementsByTagName("form")[0];
var fElem = form.elements;
window.addEventListener('load', check_status);
ecr_stat.addEventListener('change', check_status);


function check_status() {
		console.log(fElem);
		if (ecr_stat.options[ecr_stat.selectedIndex].value !== "CL"){
			dispo.disabled = true;
			for (var i = 0; i < fElem.length; i++){
				fElem[i].disabled = false;
			}
		}else{
			dispo.disabled = false;
			for (var i = 0; i < fElem.length; i++){
				fElem[i].disabled = true;
			}
		}
	}