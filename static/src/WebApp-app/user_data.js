function user_data () {
	this.type = "uninitialized type";
	this.username = "uninit username";
	this.userID = 0;
	this.callID = 0;
	this.callList = {};
	this.drSkypeID;
}; 

var user = new user_data();