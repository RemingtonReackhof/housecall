

function show_errors(xhr,status,error){
	var response = JSON.parse(xhr.responseText);
	var doc = document.getElementById("content");

	var p = document.createElement("p");
	var error_message = response.errors[0].message;
	var text = document.createTextNode(error_message);
	p.appendChild(text);
	p.setAttribute("class", "error");
	doc.appendChild(p);
}



function login_create(){
	
	//url
	//var url = base_url + '/login';

	//user input
	var data = get_login_input();

	//prev url
	var oldLocation = document.getElementById("prevURL").value;
	if (oldLocation == "None") {
		//oldLocation = base_url;
		oldLocation = 'http://0.0.0.0:3000/login';
	}
	
	//send user input via ajax
 	$.ajax({
		//url: url,				// SHOULD BE window.location !!
		url: 'http://0.0.0.0:3000/login',
		success:  function(data){window.location.assign(oldLocation);},//window.location. assign??
		error: function(xhr, status, error){show_errors(xhr,status,error);},  // show_errors and error
 		type: 'POST',
 		dataType: "json",
		contentType : "application/json",
 		data: data
 	});
}


function get_login_input(){

	//grab user input
	var username = document.getElementById("login_username_input").value;
	var password = document.getElementById("login_password_input").value;

	//make input json
	var data = '{';
	data = data + '"username": "'+username+'",';
	data = data + '"password" : "'+password+'"}';  //key not being here vs. empty string
	//login here?

	return data;
}

