function Submit() {
    var gid = document.getElementById('gid').value;
    var name = document.getElementById('name').value;
    var value = document.getElementById('value').value;
    var number = document.getElementById('number').value;

    var url = '/money?gid=%s&name=%s&value=%s&number=%s' %(gid, name, value, number)
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', url, false);
    xmlhttp.send();
    xml = xmlhttp.responseText;

}
function Clear() {
    var url = '/money?gid=%s&name=%s&value=%s&number=%s' %(0, 0, 0, 9999)
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', url, false);
    xmlhttp.send();
    xml = xmlhttp.responseText;

}
