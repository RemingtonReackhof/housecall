function contactsFilterFunctionByName() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("contactsInputByName");
    filter = input.value.toUpperCase();
    div = document.getElementById("skypeButtons").children;
    a = document.getElementsByClassName("name");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            div[i].style.display = "";
        } else {
            div[i].style.display = "none";
        }
    }
}

function contactsFilterFunctionBySpecialty() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("contactsInputBySpecialty");
    filter = input.value.toUpperCase();
    div = document.getElementById("skypeButtons").children;
    a = document.getElementsByClassName("specialty");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            div[i].style.display = "";
        } else {
            div[i].style.display = "none";
        }
    }
}

function contactsFunction() {
    document.getElementById("contactsDropdown").classList.toggle("show");
    return false;
}

function contactsSend(id) {
    var input, filter, ul, li, a, i;
    input = document.getElementById(id).innerHTML;
    filter = input.toUpperCase();
    div = document.getElementById("skypeButtons").children;
    a = document.getElementsByClassName("specialty");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            div[i].style.display = "";
        } else {
            div[i].style.display = "none";
        }
    }
}



function clearFilters() {
    var skypeButtons = document.getElementById("skypeButtons").children;    
    var i;
    document.getElementById("contactsInputBySpecialty").value = "";
    document.getElementById("contactsInputByName").value = "";
    for(i = 0; i < skypeButtons.length; i++)
    {
        skypeButtons[i].style.display = "";
    }
}









