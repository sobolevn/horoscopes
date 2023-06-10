var
  vk_members_data = {},
  lastCommentsResponse,
  lastCommentsPage = null,
  baseURL = window.location.protocol + '//' + window.location.hostname + '/';

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

function doLogin() {
  VK.Auth.login(
    null,
    VK.access.FRIENDS | VK.access.WIKI
  );
}
function doLogout() {
  VK.Auth.logout(logoutOpenAPI);
}
function loginOpenAPI() {
  getInitData();
}
function logoutOpenAPI() {
  /*window.location.reload();*/
  window.location = baseURL;
}
function getInitData() {
  var code;
  code = 'return {';
  code += 'me: API.getProfiles({uids: API.getVariable({key: 1280}), fields: "photo"})[0]';
  code += ',info: API.getGroupsFull({gids:1})[0]';
  code += ',news: API.pages.get({gid:1, pid: 2424933, need_html: 1})';
  code += ',friends: API.getProfiles({uids: API.getAppFriends(), fields: "photo"})';
  code += '};';
  VK.Api.call('execute', {'code': code}, onGetInitData);
}
function onGetInitData(data) {
  var r, i, j, html;
  if (data.response) {
    r = data.response;
    /* Insert user info */
    if (r.me) {
      ge('openapi_user').innerHTML = r.me.first_name + ' ' + r.me.last_name;
      ge('openapi_userlink').href = '/id' + r.me.uid;
      ge('openapi_userphoto').src = r.me.photo;
    }
    /* Insert Group info */
    if (r.info) {
      ge('group_link').href = '/club' + r.info.gid;
      ge('logo_img').src = r.info.photo;
    }
    /* Insert news */
    if (r.news) {
      ge('news_title').innerHTML = r.news.title;
      ge('news').innerHTML = r.news.html;
    }
    /* Insert friends */
    html = '';
    for (i = 0, j = r.friends.length; i < j; i++) {
      if (i >= 12) break;
      html += '<div onmouseout="this.className=\'list_cell\';" onmouseover="this.className=\'list_cell_over\'" class="list_cell"><a href="/id'+r.friends[i]['uid']+'"><div class="list_border_wrap"><div class="list_wrap"><div class="list_div"><div class="list_image"><img width="50" src="'+r.friends[i]['photo']+'"></div></div><div class="list_name">'+(r.friends[i]['first_name']+' '+r.friends[i]['last_name'])+'</div></div></div></a></div>';
    }
    ge('friends_list').innerHTML = html;
    hide('openapi_login_wrap');
    show('openapi_block');
    show('openapi_wrap');
    getComments();
  } else {
  
  }
}

function printCommentRow(id, uid, name, sex, photo, date, date_ts, comment) {
  return (
    '<div class="separator"></div>' +
    '<div id="comm'+id+'" class="comment">' +
    '<div class="notebody">' +
    '<a href="/id'+uid+'" class="userpic"><img src="'+photo+'"></a>' +
    '<div class="justComment">' +
    '<div class="header"><a class="memLink" href="/id'+uid+'">'+name+'</a> написал'+(sex == 1 ? 'a' : '')+'<br />'+date+'</div>' +
    '<div class="text">'+comment+'</div>' +
    '<div class="actions"><img id="action_progress'+id+'" src="images/upload.gif"/>'+
    ((VK._session.mid == uid && date_ts > (((new Date()).getTime() / 1000) - 15 * 60))
      ? '<a href="'+document.URL+'#" onclick="return deleteComment('+id+'); "><small>Удалить</small></a></div>'
      : ''
    )+
    '</div></div></div>'
  );
}

function renderPagination(current, total, progress) {
  var
    start,
    end,
    html = '';
  
  start = current - 4;
  if(start < 1) {
    start = 1;
  }
  end = current + 4;
  if (end > total) { 
    end = total;
  }
  //alert(start+','+end+','+total);
  
  html += '<div class="commentsPagesWrap standard"><ul class="commentsPages">';
  for (i = start; i <= end; i++) {
    if (i != current) {
      html += '<li onclick="getComments(' + i + ');" onmouseover="setStyle(this, \'textDecoration\', \'underline\')" onmouseout="setStyle(this, \'textDecoration\', \'none\')"><span>' + i + '</span></li>';
    } else {
      html += '<li class="current"><span>' + i + '</span></li>';
    }
  }
  html += '</ul><div class="progrWrap" style="height: 20px;"><img id="' + progress + '" src="images/upload.gif" style="vertical-align: -4px;"></div></div>';
  
  return html;
}

function renderCommentsPage(data) {
  var 
    cmm,
    count,
    pages,
    member,
    name,
    html,
    i, j;
  
  count = data.shift();
  pages = Math.ceil(count / 10);
  if (lastCommentsPage === null) {
    lastCommentsPage = pages;
  }
  html = renderPagination(lastCommentsPage, pages, 'progressTop');
  for (i = 0, j = data.length; i < j; i++) {
    cmm = data[i];
    member = vk_members_data[cmm.uid];
    name = member.first_name + ' ' + member.last_name;
    html += printCommentRow(cmm.id, cmm.uid, name, member.sex, member.photo, cmm.date, cmm.date_ts, cmm.comment);
  }
  html += renderPagination(lastCommentsPage, pages, 'progressBottom');
  
  return html;
}

function onCommentsResponse(response) {
  var
    uids  = [],
    i, j;
    
  //alert(responseText);
  lastCommentsResponse = response;
  for (i = 0, j = response.length; i < j; i++) {
    if(response[i]['uid']) {
      uids.push(response[i]['uid']);
    }
  }
  uids = array_unique(uids);
  VK.Api.call('getProfiles', {'uids': uids.join(','), 'fields': 'photo,sex'}, onGetProfilesData);
}

function getComments(s) {
  var
    onSuccess,
    onFail;
  
  onSuccess = function(ajaxObj, responseText) {
    var
      response = eval('(' + responseText + ')');
      
    onCommentsResponse(response);
  };
  onFail = function(ajaxObj, responseText) {
    responseText = responseText || 'Request error.';
    alert(responseText);
  }
  Ajax.Send(baseURL, {
    'op': 'a_get_comments', 
    's': s || 0
  }, {
    'onSuccess': onSuccess,
    'onFail': onFail    
  });
  lastCommentsPage = s || null;
  show('progressTop', 'progressBottom');
  return false;
}

function onGetProfilesData(r) {
  var 
    data,
    html,
    i, j;
  
  if (r.response) {
    data = r.response;
    for (i =0, j = data.length; i < j; i++) {
      if (!vk_members_data[data[i]['uid']]) {
        vk_members_data[data[i]['uid']] = data[i];
      }
    }
  }
  
  html = renderCommentsPage(lastCommentsResponse);
  ge('comments_list').innerHTML = html;
  hide('progressTop', 'progressBottom');
}

function postComment() {
  var
    comment = ge('comment').value,
    onSuccess,
    onFail;
    
  if(comment) {
    onSuccess = function(ajaxObj, responseText) {
    var
      response = eval('(' + responseText + ')');
    
    lastCommentsPage = null;
    ge('comment').value = '';
    onCommentsResponse(response);
    };
    onFail = function(ajaxObj, responseText) {
      responseText = responseText || 'Request error.';
      alert(responseText);
    }
    Ajax.Send(baseURL, {
      'op': 'a_add_comment', 
      'comment': comment
    }, {
      'onSuccess': onSuccess,
      'onFail': onFail    
    });
  } else {
    ge('comment').focus();
  }
  return false;
}

function deleteComment(cid) {
  var
    onSuccess,
    onFail;
  
  onSuccess = function(ajaxObj, responseText) {
    var
      response = eval('(' + responseText + ')');
    if(response.ok == 1) {
      commentBox = ge('comm' + response.cid);
      commentBox.innerHTML = '<div class="dld" style="font-weight:normal;">Комментарий удален.</div>';
    }
  };
  onFail = function(ajaxObj, responseText) {
    responseText = responseText || 'Request error.';
    alert(responseText);
  }
  Ajax.Send(baseURL, {
    'op': 'a_del_comment', 
    'cid': cid
  }, {
    'onSuccess': onSuccess,
    'onFail': onFail    
  });
  return false;
}