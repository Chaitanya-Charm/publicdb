/* All the functions whose names ends with verify are used for verification of that particular fields*/
/* All the starting names of the functions are used to identify which field that function is validating for*/
/*The Form will be submitted successfully only when all the fields are filled satisfying that field requirements*/
/*All the id names are used to get the value of that particular fields for validation*/
/*Only the class name=verifypass used to get the total details of the passport*/
/*The Passport Details and Nationality card Number will be enabled for the users whose native country is not India*/   
function getid(a){
	return document.getElementById(a);
}
function fnameverify(){
	var fn=getid("fname").value.length;
	if(fn>50){
		getid("fnameverify").innerHTML="Please enter name upto 50 characters only";
	}
	if(fn<5){
		getid("fnameverify").innerHTML="Please enter valid name(required min 5 charcters)";
	}
	if(fn>=5 && fn<=50){
		getid("fnameverify").innerHTML="";
		getid("fname").style.borderColor="initial";
		return 1;
	}
	if(fn>50 || fn<5){
		getid("fname").style.borderColor="red";
		return 0;
	}
}
function snameverify(){
	var sn=getid("sname").value.length;
	if(sn>10){
		getid("snameverify").innerHTML="Please enter short name in 10 characters";
	}
	if(sn<3){
		getid("snameverify").innerHTML="Please enter valid name";
	}
	if(sn>=3 && sn<=10){
		getid("snameverify").innerHTML="";
		getid("sname").style.borderColor="initial";
		return 1;
	}
	if(sn>10 || sn<3){
		getid("sname").style.borderColor="red";
		return 0;
	}
}
function phnoverify(){
	var phn=getid("phno").value.length;
	if(phn!=10){
		getid("phnoverify").innerHTML="Please enter a valid phone number";
		getid("phno").style.borderColor="red";
		return 0;
	}
	if(phn==10){
		getid("phnoverify").innerHTML="";
		getid("phno").style.borderColor="initial";
		return 1;
	}
}
function emailidverify(){   /*Verification of Email Id*/
	var emidv=getid("emailid").value;
	var pattern=/^[a-zA-Z0-9\.]+@[a-z0-9]+?\.(com|in|org|net|co.in)$/;            /*/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;*/
	if(pattern.test(emidv)){
		getid("emailidverify").innerHTML="";
		getid("emailid").style.borderColor="initial";
		return 1;
	}
	else{
		getid("emailidverify").innerHTML="Please enter the valid email id";
		getid("emailid").style.borderColor="red";
		return 0;
	}
}
function dobverify(){
	var dobv=getid("dob").value.length;
	if(dobv==0){
		getid("dobverify").innerHTML="Please enter the date of birth";
		getid("dob").style.borderColor="red";
		return 0;
	}
	else{
		getid("dobverify").innerHTML="";
		getid("dob").style.borderColor="initial";
		return 1;
	}
}
function addressverify(){
	var adv=getid("address").value.length;
	getid("addressverify").innerHTML=(adv!=0)?"":"Please enter the address";
	if(adv!=0){
		getid("address").style.borderColor="initial";
		return 1;
	}
	else{
		getid("address").style.borderColor="red";
		return 0;
	}
}
function incomeverify(){
	var incv=getid("income").value.length;
	getid("incomeverify").innerHTML=(incv!=0)?"":"Please enter the annual income";
	if(incv!=0){
		getid("income").style.borderColor="initial";
		return 1;
	}
	else{
		getid("income").style.borderColor="red";
		return 0;
	}
}
function pancardnoverify(){
	var panv=getid("pancardno").value.length;
	getid("pancardnoverify").innerHTML=(panv!=0)?"":"Please enter the pan card number";
	if(panv!=0){
		getid("pancardno").style.borderColor="initial";
		return 1;
	}
	else{
		getid("pancardno").style.borderColor="red";
		return 0;
	}
}
function idcardnoverify(){ 
	var idv=getid("idcardno").value.length;
	getid("idcardnoverify").innerHTML=(idv!=0)?"":"Please enter the national id card number";
	if(idv!=0){
		getid("idcardno").style.borderColor="initial";
		return 1;
	}
	else{
		getid("idcardno").style.borderColor="red";
		return 0;
	}
}
function pinverify(){
	var pinv=getid("pin").value.length;
	if(pinv!=6){
		getid("pinverify").innerHTML="Please enter a valid pin number";
		getid("pin").style.borderColor="red";
		return 0;
	}
	if(pinv==6){
		getid("pinverify").innerHTML="";
		getid("pin").style.borderColor="initial";
		return 1;
	}
}
function fun2(){	
	getid("idcardno").disabled=false;
	getid("passno").disabled=false;
	getid("passissuedate").disabled=false;
	getid("passexpdate").disabled=false;
	getid("passissueofice").disabled=false;
	getid("passissueauth").disabled=false;
	getid("pinverify").innerHTML="";
	getid("pin").style.borderColor="initial";
	getid("pin").value="";
	getid("pin").disabled=true;
}
function fun1(){
	getid("idcardno").disabled=true;
	getid("passno").disabled=true;
	getid("passissuedate").disabled=true;
	getid("passissueofice").disabled=true;
	getid("passexpdate").disabled=true;
	getid("passissueauth").disabled=true;
	getid("pin").disabled=false;
	getid("idcardnoverify").innerHTML="";
	getid("idcardno").value="";
	getid("idcardno").style.borderColor="initial";
	var passv=document.getElementsByClassName("verifypass");
	var i;
	for(i=0;i<5;i++){
		passv[i].value=null;
	}
}
function fileverify(){
	var filev=getid("file").value.length;
	if(filev!=0){
		getid("fileverify").innerHTML="";
		getid("file").style.borderColor="initial";
		return 1;
	}
	else{
		getid("fileverify").innerHTML="Please Upload a file for proof";
		getid("file").style.borderColor="red";
		return 0;
	}
}
function signverify(){
	var filev=getid("sign").value.length;
	if(filev!=0){
		getid("signverify").innerHTML="";
		getid("sign").style.borderColor="initial";
		return 1;
	}
	else{
		getid("signverify").innerHTML="Please Upload a file for proof of signature";
		getid("sign").style.borderColor="red";
		return 0;
	}
}
function passverify(){
	var passv=document.getElementsByClassName("verifypass");
	var i,k=true;
	for(i=0;i<5;i++){
		if(passv[i].value==0){
			k=false;
			break;
		}
	}
	if(k){
		return 1;
	}
	else{
		return 0;
	}
}
function submitform(){
	if(fnameverify() && snameverify() && phnoverify() && emailidverify() && dobverify() && addressverify() && incomeverify() && pancardnoverify() && fileverify() && signverify()){
		if(getid("indian").checked==true){
			if(pinverify()){
				alert("Your details are saved successfully");
			}
			else{
				alert("Please fill all the details in the form,then submit your form");
			}
		}
		else{
			if(idcardnoverify() && passverify()){
				alert("Your details are saved successfully");
			}
			else{
				alert("Please fill all the details in the form,then submit your form");
			}
		}
	}
	else{
		alert("Please fill all the details in the form,then submit your form");
	}
}

	