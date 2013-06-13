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

function done(res, status) {
    alert('done ' + status + ' ' + res.responseText);
  if (status == "success") {
      console.log(res);
  }
  else {
  }
}

function getInitData(callBack) {
  var code;
  code = 'return {';
  code += 'me: API.getProfiles({ fields: "photo,sex,bdate"})[0]';
  code += '};';
  VK.Api.call('execute', {'code': code}, callBack);
}

function authInfo(response, csrf) {
  if (response.session) {
  	getInitData(function(data) {
        onGetInitData(data, csrf);
    });
    //alert('user: '+response.session.mid);
  } else {
    //alert('not auth');

  }
}

function onGetInitData(data, csrf) {
  var r, i, j, html;
  if (data.response) {
    r = data.response;
    /* Insert user info */
    if (r.me) {
      ge('openapi_user').innerHTML = r.me.first_name + ' ' + r.me.last_name;
      ge('openapi_userlink').href = 'http://vk.com/id' + r.me.uid;
      ge('openapi_userphoto').src = r.me.photo;
      ge('uid').value = r.me.uid
    }
    	hide('login_button');
    	show('openapi_block');
        var fullName = r.me.first_name + ' ' + r.me.last_name;
        var data = { uid: r.me.uid, sex: r.me.sex, bdate: r.me.bdate, img_src: r.me.photo,
            name: fullName, 'csrfmiddlewaretoken': csrf};

        var args = { type:"POST", url:"/login", data:data, complete:done};
        $.ajax(args);

  } else {
	alert('error');
  }
}

function buttonPressed(value, uid, csrf) {

    if (value && csrf && uid) {
        var data = { 'horoscope_id': value, 'uid': uid, 'csrfmiddlewaretoken': csrf};

        var args = { type:"POST", url:"/sign", data:data, complete:done};
        $.ajax(args);
    }

}
