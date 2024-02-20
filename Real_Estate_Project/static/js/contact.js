function validateForm() {
    var name = document.forms["contactForm"]["name"].value;
    var email = document.forms["contactForm"]["email"].value;
    var message = document.forms["contactForm"]["message"].value;

    var nameError = document.getElementById("nameError");
    var emailError = document.getElementById("emailError");
    var messageError = document.getElementById("messageError");

    nameError.textContent = "";
    emailError.textContent = "";
    messageError.textContent = "";

    if (name === "") {
      nameError.textContent = "Please enter your name.";
      return false;
    }

    if (name.length < 3) {
      nameError.textContent = "Name must be at least 3 characters long.";
      return false;
    }

    if (email === "") {
      emailError.textContent = "Please enter your email address.";
      return false;
    }

    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      emailError.textContent = "Please enter a valid email address.";
      return false;
    }

    if (message === "") {
      messageError.textContent = "Please enter a message.";
      return false;
    }

    
    if (message.length < 100) {
      messageError.textContent = "Message must be at least 100 characters long.";
      return false;
    }

   
    var nameRegex = /^[a-zA-Z]+$/;
    if (!nameRegex.test(name)) {
      nameError.textContent = "Name must contain only alphabetic characters.";
      return false;
    }

   
    return true;
  }