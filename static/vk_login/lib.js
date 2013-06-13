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
  if (status == "success") {
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
