const cross = document.querySelectorAll('.cross');
const rmv = (el) => {
    el.parentElement.remove();
}

    cross.forEach(el => {
        el.addEventListener('click', ()=> {
            rmv(el);
        })
    })
    


