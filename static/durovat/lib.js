function login() {
	VK.init({
  	apiId: 3702495
	});
}

function doLogout() {
  VK.Auth.logout(logoutOpenAPI);
}

function logoutOpenAPI() {
	hide('openapi_block');
	show('login_button');
}

function authInfo(response) {
  if (response.session) {
  	getInitData(onGetInitData);
    //alert('user: '+response.session.mid);
  } else {
    //alert('not auth');
    
  }
}
function authInfo2(response) {
  if (response.session) {
  	getInitData(onGetInitData2);
    //alert('user: '+response.session.mid);
  } else {
    //alert('not auth');
    
  }
}

function getInitData(callBack) {
  var code;
  code = 'return {';
  code += 'me: API.getProfiles({ fields: "photo,sex,bdate"})[0]';
  code += '};';
  VK.Api.call('execute', {'code': code}, callBack);
}

function onGetInitData(data) {
  var r, i, j, html;
  if (data.response) {
    r = data.response;
    var old;
    if (document.getElementById('uid') != null) {
    	old = document.getElementById('uid').value;
    } else {
    	old = '';
    }
    
    /* Insert user info */
    if (r.me) {
      ge('openapi_user').innerHTML = r.me.first_name + ' ' + r.me.last_name;
      ge('openapi_userlink').href = '/id' + r.me.uid;
      ge('openapi_userphoto').src = r.me.photo;
    }
    	hide('login_button');
    	show('openapi_block');
    	var form = document.getElementById('form2');
    	document.getElementById('uid').value = r.me.uid;
    	document.getElementById('bdate').value = r.me.bdate;
    	document.getElementById('sex').value = r.me.sex;
    	document.getElementById('img_src').value = r.me.photo;
    	document.getElementById('name').value = r.me.first_name + ' ' + r.me.last_name;
    	form.submit();
    //show('openapi_wrap');
    	
  } else {
	alert('error');
  }
}

function onGetInitData2(data) {
  var r, i, j, html;
  if (data.response) {
    r = data.response;
    var old;
    if (document.getElementById('uid') != null) {
    	old = document.getElementById('uid').value;
    } else {
    	old = '';
    }
    
    /* Insert user info */
    if (r.me) {
      ge('openapi_user').innerHTML = r.me.first_name + ' ' + r.me.last_name;
      ge('openapi_userlink').href = '/id' + r.me.uid;
      ge('openapi_userphoto').src = r.me.photo;
    }
    	hide('login_button');
    	show('openapi_block');
    //show('openapi_wrap');
    	
  } else {
	alert('error');
  }
}