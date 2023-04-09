const inp = document.querySelectorAll('.my-input');
const lab = document.querySelectorAll('.lab');

// console.log(lab);
// console.log(inp);
document.addEventListener('click', () => {
    for (let i = 0; i < inp.length; ++i) {
        if (document.activeElement != inp[i]) {

            if (inp[i].value) {
                lab[i].style.top = '-20px';
            }
            else lab[i].style.top = '0';
        }
        else lab[i].style.top = '-20px';
    }

})

setInterval(() => {
    for (let i = 0; i < inp.length; ++i) {

        if (inp[i].value) {
            lab[i].style.top = '-20px';
            inp[i].classList.add('backdrop-blur-md');
        }
        else if (document.activeElement != inp[i]) lab[i].style.top = '0';
    }
}, 100);