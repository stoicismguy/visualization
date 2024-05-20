refresh_button = document.getElementsByClassName("refresh-button")[0];
ajax_url = refresh_button.getAttribute("url");
refresh_button.onclick = function (e) {
    send_data = {};
    unactive_buttons = [];
    block = e.target.parentElement;
    config_buttons = block.getElementsByClassName("config_buttons");
    for (var i=0; i < config_buttons.length; i++) {
        div = config_buttons[i];
        isActive = div.getElementsByClassName("isActiveColumn")[0].getElementsByTagName("input")[0].checked;
        if (!isActive) {
            unactive_buttons.push(i+1);
        }
        values_list = div.getElementsByClassName("items")[0].children;
        columns_data = []
        Array.from(values_list).forEach(element => {
            input = element.getElementsByTagName("input")[0];
            if (input.checked) {
                columns_data.push(input.getAttribute("value"));
            }
        });
        if (columns_data.length == 0){
            send_data[i] = columns_data.toString();
        }
        else {
            send_data[i] = columns_data;
        }  
    }
    send_data['unactive_buttons'] = JSON.stringify(unactive_buttons);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].getAttribute('value');
    send_data['csrfmiddlewaretoken'] = token;
    console.log(send_data);

    $.ajax({
        type: "POST",
        url: window.location.href+"data",
        data: send_data,
        success: function (request) {
            console.log(request)
            ul = document.getElementsByClassName("0")[0];
            ul.innerHTML = request;
            row_size(config_buttons.length+1);
        },
        error: function (request) {
            alert("Ошибка!");
        }
    })
}

function row_size(columns) {
    pos=0

    screen_width = window.screen.width;
    max_column_width = parseInt(screen_width / columns);
    
    for (var times = 0; times < columns; times++){
        max_width = 0
        uls = document.getElementsByClassName(`${pos}`);
        for (var j=0; j < uls.length; j++){
            current_ul = uls[j];
            lis = current_ul.querySelectorAll(":scope > li");;
            for (var k=0; k < lis.length; k++){
                current_li = lis[k];
                li_p = current_li.getElementsByTagName("p")[0];
                if (li_p == undefined) {
                    continue;
                }
                li_width = li_p.clientWidth;  
                if (li_width > max_width){
                    max_width = li_width
                }
            }		
        }
        if (max_width > max_column_width) {
            max_width = max_column_width - 5;
        }
        for (var j=0; j < uls.length; j++){
            current_ul = uls[j];
            lis = current_ul.querySelectorAll(":scope > li");
            for (var k=0; k < lis.length; k++){
                current_li = lis[k];
                li_p = current_li.getElementsByTagName("p")[0];
                if (li_p == undefined) {
                    continue;
                }
                li_p.style.width = `${max_width}px`;
            }			
        }
        pos += 1;
    }
    console.log("row_size()")
    
}

