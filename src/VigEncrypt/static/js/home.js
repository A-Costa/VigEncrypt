function activate_decrypt() {
    var label1 = document.querySelector(
        'body > div > div:nth-child(2) > div.col-md-8 > form > div:nth-child(1) > label')
    label1.innerHTML = "Cipher Text"

    var label2 = document.querySelector(
        'body > div > div:nth-child(2) > div.col-md-8 > form > div:nth-child(2) > label')
    label2.innerHTML = "Decryption Key"

    var button = document.querySelector(
        'body > div > div:nth-child(2) > div.col-md-8 > form > button')
    button.innerHTML = "Decrypt"

    var label3 = document.querySelector(
        'body > div > div:nth-child(2) > div.col-md-8 > form > div:nth-child(6) > label')
    label3.innerHTML = "Plain Text"

    swap_text_area()
}

function activate_encrypt() {
    var label1 = document.querySelector(
        'body > div > div:nth-child(2) > div.col-md-8 > form > div:nth-child(1) > label')
    label1.innerHTML = "Plain Text"

    var label2 = document.querySelector(
        'body > div > div:nth-child(2) > div.col-md-8 > form > div:nth-child(2) > label')
    label2.innerHTML = "Encryption Key"

    var button = document.querySelector(
        'body > div > div:nth-child(2) > div.col-md-8 > form > button')
    button.innerHTML = "Encrypt"

    var label3 = document.querySelector(
        'body > div > div:nth-child(2) > div.col-md-8 > form > div:nth-child(6) > label')
    label3.innerHTML = "Cipher Text"

    swap_text_area()
}

function swap_text_area() {
    var text_area_1 = document.querySelector('#TextArea1')
    var text_area_2 = document.querySelector('#TextArea2')

    var temp = text_area_2.value
    text_area_2.value = text_area_1.value
    text_area_1.value = temp
}

function capitalize_key() {
    var key = document.querySelector('#KeyTextarea')

    text = key.value
    text = text.replace(/\s/g, '').replace(/[^a-zA-Z ]/g, '')

    key.value = text.toUpperCase()
}



document.querySelector(
    'body > div > div:nth-child(2) > div.col-md-4.border-right.info > div > label:nth-child(2)'
).addEventListener("click", activate_decrypt)
document.querySelector(
    'body > div > div:nth-child(2) > div.col-md-4.border-right.info > div > label.btn.btn-secondary.active'
).addEventListener("click", activate_encrypt)

document.querySelector('#KeyTextarea').addEventListener("keyup", capitalize_key)
document.querySelector('#KeyTextarea').addEventListener("keydown", capitalize_key)
