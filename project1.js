function goEnroll() {
	location.replace("project1_enroll.html");
}
function say() {
	alert('hello');
}

function checkId() {
	var input = document.getElementById("enrollId").value;
	alert(input);
	var form = true;

	for (var i=0; i<input.length; i++) {
		alert(input.charCodeAt(i)==1);
		alert(input.charCodeAt(i));
		alert(idElemnt(input.charCodeAt(i)));
		if(!idElemnt(input.charCodeAt(i))) {
			alert("잘못된 입력");
		}
	}
}

function idElement(a) {
	if ((48<=a && a<=57) || (97<=a && a<=122)) return true;
	else return false;
}