function submitFormAjax() {
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200)
            alert(this.responseText); // Here is the response
    }

    var vigenere_function = document.querySelector('#vigenere_function').value
    var vigenere_text = document.querySelector('#vigenere_text_area_1').value
    var vigenere_key = document.querySelector('#vigenere_key').value
    var vigenere_key_method = document.querySelector('#vigenere_key_method input[name="vigenere_key_method"]:checked').value

    req.open("POST", "/api/test", true);
    req.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    req.send("function="+vigenere_function+
             "&text="+vigenere_text+
             "&key="+vigenere_key+
             "&key_method="+vigenere_key_method);
}
