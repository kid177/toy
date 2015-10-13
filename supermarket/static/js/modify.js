function Submit() {
    alert("录入成功");
    var gid = document.getElementById('gid').value;
    var name = document.getElementById('name').value;
    var value = document.getElementById('value').value;
    var number = document.getElementById('number').value;
    var in_time = document.getElementById('in_time').value;
    var s_name = document.getElementById('s_name').value;

    var url = '/modify?gid=%s&name=%s&value=%s&number=%s&in_time=%s&s_name=%s' %(gid, name, value, number, in_time, s_name);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', url, false);
    xmlhttp.send();
    xml = xmlhttp.responseText;

}
