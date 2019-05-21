

var ecr_number = document.getElementsByClassName("ecr-num");

var showNotes = function(e) {
	e.target.childNodes[1].classList.add("block");
	e.target.childNodes[1].classList.remove("hidden");
}

var hideNotes = function(e) {
	e.target.childNodes[1].classList.remove("block");
	e.target.childNodes[1].classList.add("hidden");
}

for (var i = 0; i < ecr_number.length; i++){
	ecr_number[i].addEventListener("mouseover", showNotes);
	ecr_number[i].addEventListener("mouseout", hideNotes);
}