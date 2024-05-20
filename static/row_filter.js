var checkList = document.getElementsByClassName('list-vipal');
Array.from(checkList).forEach(el => {
    el.getElementsByClassName('anchor')[0].onclick = function(evt) {
        if (el.classList.contains('visible')) {
            el.classList.remove('visible');
        }  
        else {
            el.classList.add('visible');
        }
    }
})
