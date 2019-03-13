function submitFormAjax() {
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200){
            var response_data = JSON.parse(this.response);
            //alert(response_data['test_key'])
            //alert(this.responseText); // Here is the response
            var text_area = document.querySelector('#vigenere_text_area_2');
            text_area.value = response_data['test_key'];
        }
    }

    var vigenere_function = document.querySelector('#vigenere_function').value
    var vigenere_text = document.querySelector('#vigenere_text_area_1').value
    var vigenere_key = document.querySelector('#vigenere_key').value
    var vigenere_key_method = document.querySelector('#vigenere_key_method input[name="vigenere_key_method"]:checked').value

    req.open("POST", "/api/test", true);
    req.setRequestHeader("Content-type","application/json");
    req.send(JSON.stringify({
                function: vigenere_function,
                text: vigenere_text,
                key: vigenere_key,
                key_method: vigenere_key_method
            })
    )
}
