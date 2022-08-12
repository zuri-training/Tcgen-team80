const icon = document.getElementById("burger")
const about1 = document.querySelector(".nav-buttons")
const menu = document.querySelector(".head")
icon.onclick= function() {
    if (menu.style.display == "none" ) {
        menu.style.display = "flex";
    } else{
        menu.style.display = "none";
    }

};
// icon.onclick= function() {
//     if (about1.style.display == "none" ) {
//         about1.style.display = "block";
//     } else{
//         about1.style.display = "none";
//     }

// };
