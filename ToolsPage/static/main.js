// OBTENER ELEMENTOS MODAL SEEKER

let modalSeeker = document.getElementById('modal_seeker');
let buttonSeeker = document.getElementById('button_seeker');
let closeModalSeeker = document.getElementById('close_seeker');


// OBTENER ELEMENTOS MODAL ITEM

let modalItem = document.getElementById('modal_item');
let buttonsItem = document.getElementsByClassName('button_item');
let buttonCloseModalItem = document.getElementById('button_close_modal_item');
let closeModalItem = document.getElementById('close_item');
// let itemImage = document.getElementById('item_image');
// let englishName = document.getElementById('english_name');
// let englishDescription = document.getElementById('english_description');
// let spanishName = document.getElementById('spanish_name');
// let spanishDescription = document.getElementById('spanish_description');

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

// FUNCIONES MODAL ITEM




// EVENTOS MODAL ITEM

for(let i=0; i<buttonsItem.length; i++){
    buttonsItem[i].addEventListener("click", function(event) {
        let id = this.getAttribute('data-id');
        let url = `http://127.0.0.1:8000/tools/get_tool/${id}`;
        fetch(url)
            .then(response => response.json())
            .then(tool_data => {
                document.getElementById('item_image').src = `/static/images/${tool_data.tool_image}`;
                document.getElementById('english_name').textContent = tool_data.english_name;
                document.getElementById('english_description').textContent = tool_data.english_description;
                document.getElementById('spanish_name').textContent = tool_data.spanish_name;
                document.getElementById('spanish_description').textContent = tool_data.spanish_description;
                event.preventDefault(); // Detenemos el envío de la etiqueta a
                modalItem.style.display = 'block';
            })
            .catch(error => console.error('Error al obtener detalles del item:', error));
        
    })
}

buttonCloseModalItem.addEventListener("click", function(event) {
    event.preventDefault()
    modalItem.style.display = "none";
})

closeModalItem.onclick = function() {
    modalItem.style.display = 'none';
}