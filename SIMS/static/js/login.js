const form = document.querySelector('form')
form.addEventListener('submit', (event) => {
    event.target.checkValidity()
})

document.getElementById("loginForm").addEventListener("submit", function(event){
  // event.preventDefault();
  var pwd = document.getElementById("password").value;
  var errorElement = document.getElementById("error");
  
  if(pwd === ""){
    errorElement.textContent = "エラー：パスワードを入力してください。";
  } else if(!/^[a-zA-Z0-9]+$/.test(pwd)){
    errorElement.textContent = "エラー：パスワードは英数字のみで入力してください。";
  } else {
    errorElement.textContent = "";
  }
});

document.getElementById("loginForm").addEventListener("submit", function(event2){
  event2.preventDefault2();
  var user_id = document.getElementById("user_id").value;
  var error2Element = document.getElementById("error2");
  
  if(pwd === ""){
    error2Element.textContent = "エラー: ユーザー名を入力してください。";
  } else if(!/^[a-zA-Z0-9]+$/.test(user_id)){
    error2Element.textContent = "エラー: ユーザー名は英数字のみで入力してください。";
  } else {
    error2Element.textContent = "";
  }
});




