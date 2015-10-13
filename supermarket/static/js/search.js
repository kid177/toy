function Submit() {
    var gid = document.getElementById('g').value;
    var name = document.getElementById('n').value;
    var number = document.getElementById('num').value;
    var s_n = document.getElementById('s_n').value;
    var s_t = document.getElementById('s_t').value;
    var e_t = document.getElementById('e_t').value;

    var url = '/search?g=%s&n=%s&num=%s&s_t=%s&e_t=%s&s_n=%s' %(gid, name, number, s_t, e_t, s_n);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', url, false);
    xmlhttp.send();
    xml = xmlhttp.responseText;

}
