// OBTENER ELEMENTOS MODAL SEEKER

let modalSeeker = document.getElementById('modal_seeker');
let buttonSeeker = document.getElementById('button_seeker');
let closeModalSeeker = document.getElementById('close_seeker');


// OBTENER ELEMENTOS MODAL ITEM

let modalItem = document.getElementById('modal_item');
let buttonsItem = document.getElementsByClassName('button_item');
let buttonCloseModalItem = document.getElementById('button_close_modal_item')
let closeModalItem = document.getElementById('close_item');



// EVENTOS MODAL SEEKER
buttonSeeker.addEventListener("click", function(event) {
    event.preventDefault()
    modalSeeker.style.display = "block";
})

closeModalSeeker.onclick = function() {
    modalSeeker.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == modalSeeker) {
        modalSeeker.style.display = 'none';
    } else if (event.target == modalItem) {
        modalItem.style.display = 'none';
    }
}

// EVENTOS MODAL ITEM

for(let i=0; i<buttonsItem.length; i++){
    buttonsItem[i].addEventListener("click", function(event) {
        event.preventDefault();
        modalItem.style.display = "block";
    })
}

buttonCloseModalItem.addEventListener("click", function(event) {
    event.preventDefault()
    modalItem.style.display = "none";
})

closeModalItem.onclick = function() {
    modalItem.style.display = 'none';
}