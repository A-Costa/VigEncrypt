var active_function = 'encrypt'

function activate_decrypt() {
    var label_vigenere_text_area_1 = document.querySelector('#label_vigenere_text_area_1')
    var label_vigenere_text_area_2 = document.querySelector('#label_vigenere_text_area_2')
    var label_vigenere_key = document.querySelector('#label_vigenere_key')
    var vigenere_button = document.querySelector('#vigenere_button')
    var vigenere_function = document.querySelector('#vigenere_function')

    label_vigenere_text_area_1.innerHTML = "Cipher Text"
    label_vigenere_text_area_2.innerHTML = "Plain Text"

    label_vigenere_key.innerHTML = "Decryption Key"

    vigenere_button.innerHTML = "Decrypt"
    vigenere_function.value = "decrypt"

    if(active_function == 'encrypt'){
        swap_text_area()
    }
    active_function = 'decrypt'
}

function activate_encrypt() {
    var label_vigenere_text_area_1 = document.querySelector('#label_vigenere_text_area_1')
    var label_vigenere_text_area_2 = document.querySelector('#label_vigenere_text_area_2')
    var label_vigenere_key = document.querySelector('#label_vigenere_key')
    var vigenere_button = document.querySelector('#vigenere_button')
    var vigenere_function = document.querySelector('#vigenere_function')

    label_vigenere_text_area_1.innerHTML = "Plain Text"
    label_vigenere_text_area_2.innerHTML = "Cipher Text"

    label_vigenere_key.innerHTML = "Encryption Key"

    vigenere_button.innerHTML = "Encrypt"
    vigenere_function.value = "encrypt"

    if(active_function == 'decrypt'){
        swap_text_area()
    }
    active_function = 'encrypt'
}

function swap_text_area() {
    var vigenere_text_area_1 = document.querySelector('#vigenere_text_area_1')
    var vigenere_text_area_2 = document.querySelector('#vigenere_text_area_2')

    var temp = vigenere_text_area_2.value
    vigenere_text_area_2.value = vigenere_text_area_1.value
    vigenere_text_area_1.value = temp
}

function capitalize_key() {
    var key = document.querySelector('#vigenere_key')

    text = key.value
    text = text.replace(/\s/g, '').replace(/[^a-zA-Z ]/g, '')

    key.value = text.toUpperCase()
}



document.querySelector('#encrypt_fn_button')
        .addEventListener("click", activate_encrypt)
document.querySelector('#decrypt_fn_button')
        .addEventListener("click", activate_decrypt)

document.querySelector('#vigenere_key').addEventListener("keyup", capitalize_key)
document.querySelector('#vigenere_key').addEventListener("keydown", capitalize_key)
