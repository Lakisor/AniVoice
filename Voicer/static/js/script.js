let choosed = []
let added = []


function Choose(id) {
    obj = document.getElementById(id)
    index = choosed.indexOf(obj);

    if (choosed.includes(obj)) {
        choosed.splice(index, 1)
        obj.classList.toggle('Clicked');
    } else {
        choosed.push(obj)
        obj.classList.toggle('Clicked');
    }
}

function Add() {
    added = [].concat(choosed);
    choosed.length = 0;
    kuda = document.getElementById('added')
    for (let i = 0; i <= added.length; i++) {
        if (added.length > 0) {
            obj = added[i];
            obj.parentNode.removeChild(obj);
            console.log(obj);
            kuda.innerHTML += obj.innerHTML;
        }
    }
}