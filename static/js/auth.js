document.getElementById('showPwd').onclick = function(){showPassword()}

function showPassword(){
    console.log('Working...........')
    var pwdField = document.getElementById('password');
    if (pwdField.type === 'password'){
        pwdField.type = 'text';
    }else{
        pwdField.type = 'password';
    }
}