inputs = document.getElementsByClassName("input-columns");
    Array.from(inputs).forEach(element => {
        element.addEventListener("click", function(e) {
            element.classList.toggle("off");
            element.getElementsByTagName("input")[0].checked = !element.getElementsByTagName("input")[0].checked;
        });
    });