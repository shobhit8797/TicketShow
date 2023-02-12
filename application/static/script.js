let login_form = document.querySelector("#login_form");
if (login_form != null) {
  login_form.addEventListener("submit", (e) => {
    e.preventDefault();

    fetch("/auth/login", {
      method: "POST",
      body: new FormData(document.getElementById("login_form")),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data?.statusCode == 200) {
          window.location.href = "/";
        } else {
          alert(data.message);
        }
      });
  });
}

let signup_form = document.querySelector("#signup_form");
if (signup_form != null) {
  signup_form.addEventListener("submit", (e) => {
    e.preventDefault();
    fetch("/auth/signup", {
      method: "POST",
      body: new FormData(document.getElementById("signup_form")),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data?.statusCode == 200) {
          window.location.href = "/login";
        } else {
          alert(data.message);
        }
      });
  });
}

function Logout() {
  fetch("/auth/logout", {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => {
      if (data?.statusCode == 200) {
        window.location.href = "/login";
      } else {
        alert(data.message);
      }
    });
}