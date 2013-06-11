var
  vk_members_data = {},
  lastCommentsResponse,
  lastCommentsPage = null,
  baseURL = window.location.protocol + '//' + window.location.hostname + '/';
 
 // функция для вывода полученной информации
function ge() {
  var ea;
  for (var i = 0; i < arguments.length; i++) {
    var e = arguments[i];
    if (typeof e == 'string')
      e = document.getElementById(e);
    if (arguments.length == 1)
      return e;
    if (!ea)
      ea = new Array();
    ea.push(e);
  }
  return ea;
}
 
function array_unique(ar){
  if (ar.length && typeof ar !== 'string') {
    var sorter = {};
    var out = [];
    for (var i=0, j=ar.length; i<j; i++) {
      if(!sorter[ar[i]+typeof ar[i]]){
        out.push(ar[i]);
        sorter[ar[i]+typeof ar[i]]=true;
      }
    }
  }
  return out || ar;
}
 
// функция авторизации
function doLogin() {
  VK.Auth.login(
    null,
    VK.access.FRIENDS | VK.access.WIKI // запрашиваем доступ к друзьям и вики
  );
}
// функция выхода
function doLogout() {
  VK.Auth.logout(logoutOpenAPI);
}
function logoutOpenAPI() {
  window.location = baseURL;
}
 