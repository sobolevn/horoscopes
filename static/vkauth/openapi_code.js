window.onload = function() { // когда вся страница загрузиться
    // инициализируем "приложение"
    window.vkAsyncInit = function() {
        VK.init({
            apiId: 3702495, // заменяем на id своего приложения
            nameTransportPath: 'static_media/vkauth/xd_receiver.html'    // заменяем на ссылку к файлу xd_receiver.html на вашем сервере
        });
    };
    (function() {
        var el = document.createElement('script');
        el.type = 'text/javascript';
        el.src = 'http://vkontakte.ru/js/api/openapi.js';
        el.charset="windows-1251";
        el.async = true;
        document.getElementById('vk_api_transport').appendChild(el);
    }());  
}
     
// получаем данные о пользователе. id пользователя считываем из переменной 1280
function getInitData() {
  var code;
  code = 'return {'
  code += 'me: API.getProfiles({uids: API.getVariable({key: 1280}), fields: "photo"})[0]';
  code += '};';
  //VK.Api.call('execute', {'code': code}, onGetInitData);
  VK.Api.call('users.get', {'fields': 'photo'}, onGetInitData);
}
// данные получены
function onGetInitData(data) {
    var r;
    if (data.response) {
        r = data.response;
        if (r.me) {
        	assert("here");
            ge('openapi_user').innerHTML = r.me.first_name + ' ' + r.me.last_name;
            ge('openapi_userlink').href = '/id' + r.me.uid;
            ge('openapi_userphoto').src = r.me.photo;
        }
    }
}
 
// авторизуемся
function loginOpenAPI(){
    doLogin();
    // и вызываем функцию getInitData()
    getInitData();
    return false;
}