// const openBtn = document.querySelector('.product-link');
// const modal = document.querySelector('.modal');

// openBtn.addEventListener('click', openModal);

// function openModal() {
//     modal.style.display = 'flex';
// }

// closeBtn.addEventListener('click', closeModal);

// function closeModal(){
//     modal.style.display = 'none'
// }


console.log("hi")


var modal = document.getElementsByClassName("modal");

var btn = document.getElementsByClassName("product-link-btn");

btn.onclick = function() {
    modal.style.display = "flex";
  }

  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }