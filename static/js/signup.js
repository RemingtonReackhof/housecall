//signup.js

function hospitalFunction() {
    document.getElementById("hospitalDropdown").classList.toggle("show");
    return false;
}

function hospitalfilterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("hospitalInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("hospitalDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

function specFunction() {
    document.getElementById("specDropdown").classList.toggle("show");
    return false;
}

function specfilterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("specInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("specDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

function hospitalSend(id) {
    document.getElementById("hospitalChoice").innerHTML = document.getElementById(id).innerHTML;
    document.getElementById("hospitalDropdown").classList.toggle("show");
}

function specSend(id) {
    document.getElementById("specChoice").innerHTML = document.getElementById(id).innerHTML;
    document.getElementById("specDropdown").classList.toggle("show");
}

function emt() {
    document.getElementById("emtButton").style.border = "5px solid #686464";
    document.getElementById("doctorButton").style.border = "0px";
    document.getElementById("buttonStatus").innerHTML = "emt";
}

function doctor() {
    document.getElementById("doctorButton").style.border = "5px solid #686464";
    document.getElementById("emtButton").style.border = "0px";
    document.getElementById("buttonStatus").innerHTML = "doctor";
}

////////

function show_errors(xhr,status,error){
    console.log(xhr.responseText)
    // var doc = document.getElementById("content");

    // var p = document.createElement("p");
    // var error_message = response.errors[0].message;
    // var text = document.createTextNode(error_message);
    // p.appendChild(text);
    // p.setAttribute("class", "error");
    // doc.appendChild(p);
}



function signup_create(){
    
    console.log('in signup create');

    //user input
    var data = get_signup_input();

    //prev url
    var oldLocation = document.getElementById("prevURL").value;
    if (oldLocation == "None") {
        //oldLocation = base_url;
        oldLocation = '/signup';
    }
    
    //send user input via ajax
    $.ajax({
        //url: url,             // SHOULD BE window.location !!
        url: '/signup',
        success:  function(data){
            document.getElementsByTagName('webapp-app')[0].page = 'dashboard';
        },//window.location. assign??
        error: function(xhr, status, error){
            show_errors(xhr,status,error);
        },  // show_errors and error
        type: 'POST',
        dataType: "json",
        contentType : "application/json",
        data: data
    });
}


function get_signup_input(){

    //grab user input
    var firstname = document.getElementById("signup_firstName_input").value;
    var lastname = document.getElementById("signup_lastName_input").value;
    var skype_username = document.getElementById("signup_skypeUserName_input").value;
    var email = document.getElementById("signup_email_input").value;
    var password = document.getElementById("signup_password_input").value;
    var buttonStatus = document.getElementById("buttonStatus").value;
    var doc = 0;
    if (buttonStatus == "emt") {
        doc = 0;
    }
    if (buttonStatus == "doctor") {
        doc = 1;
    }
    var hospital = document.getElementById("hospitalChoice").innerHTML;
    var specialty = document.getElementById("specChoice").innerHTML;

   


    //make input json
    var data = '{';
    data = data + '"firstname": "'+firstname+'",';
    data = data + '"lastname": "'+lastname+'",';
    data = data + '"skype_username": "'+skype_username+'",';
    data = data + '"email": "'+email+'",';
    data = data + '"hospital": "'+hospital+'",';
    data = data + '"specialty": "'+specialty+'",';
    data = data + '"doc": "'+doc+'",';
    data = data + '"password": "'+password+'"}';  //key not being here vs. empty string
    //login here?
    console.log(data)

    return data;
}

 