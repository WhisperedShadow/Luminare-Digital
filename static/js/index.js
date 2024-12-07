document.querySelector(".bar").addEventListener("click", function () {
  document.querySelector(".nav").classList.add("active");
});
document.querySelector(".h-mark").addEventListener("click", function () {
  document.querySelector(".nav").classList.remove("active");
});

let links = document.querySelectorAll(".s-links");
let drobdown = document.querySelector("#down");

links.forEach((link) => {
  link.addEventListener("click", function (event) {
    event.preventDefault();
    drobdown.value = this.id;
    let con = document.querySelector("#contact");
    if (con) {
      con.scrollIntoView({
        behaviour: "smooth",
      });
    }
  });
});
