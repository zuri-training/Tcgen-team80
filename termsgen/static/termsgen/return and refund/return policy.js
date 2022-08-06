
const App_name = document.querySelector("appName");
const Web_name = document.querySelector("#webname");
const Company_name = document.querySelector("#company");
const Da_te = document.querySelector("#date");
const Web_site = document.querySelector("#input website");
const Country = document.querySelector("#country");
const Person_name = document.querySelector("#input individual");
const Contact_email = document.querySelector("#cEmail");
const Contact_web = document.querySelector("#cWeb");
const Contact_social = document.querySelector("#cmedia");
const Contact_number = document.querySelector("#cNum");
const Contact_postmail = document.querySelector("#cPost");
const ContactEmail = document.querySelector(".contactEmail");
const Contactphone = document.querySelector(".contactphone")
const Contacturl = document.querySelector(".contactUrl");
const Contactsocial = document.querySelector(".contactmedia");
const Contactpost = document.querySelector(".contactpost");
const web1 = document.querySelector(".web1");
const web2 = document.querySelector(".web2");
const phone1 = document.querySelector(".phone1");
const com1 = document.querySelector(".com1");
                

const Dot_1 = document.querySelector("#dot-1");
const Dot_2 = document.querySelector("#dot-2");
const Dot_3 = document.querySelector("#dot-3");
const Dot_4 = document.querySelector("#dot-4");
const Dot_5 = document.querySelector("#dot-5");
const Dot_6 = document.querySelector("#dot-6");
const Dot_7 = document.querySelector("#dot-7");
const Dot_8 = document.querySelector("#dot-8");
const Dot_9 = document.querySelector("#dot-9");
const Dot_10 = document.querySelector("#dot-10");
const Dot_11 = document.querySelector("#dot-11");
const Dot_12= document.querySelector("#dot-12");
const Dot_13 = document.querySelector("#dot-13");
const Dot_14 = document.querySelector("#dot-14");
const Dot_15 = document.querySelector("#dot-15");
const Dot_16 = document.querySelector("#dot-16");
const Dot_19 = document.querySelector("#dot-19");
const Dot_29 = document.querySelector("#dot-29");
const Dot_39 = document.querySelector("#dot-39");
const Dot_49 = document.querySelector("#dot-49");
const Dot_59 = document.querySelector("#dot-59");

const Dot_79 = document.querySelector("#dot-79");
const Dot_89 = document.querySelector("#dot-89");
const Dot_99 = document.querySelector("#dot-99");
const Dot_109 = document.querySelector("#dot-109");
const Dot_119 = document.querySelector("#dot-119");
const Dot_129 = document.querySelector("#dot-129");
const Dot_139 = document.querySelector("#dot-139");




function setCookie(name, value){
    document.cookie = `${name}= ${value};SameSite=lax;path=/`
}


function getCookie(name){
    const cDecoded = decodeURIComponent(document.cookie);
    const cArray = cDecoded.split("; ");
    let result = null

    cArray.forEach(element => {
        if(element.indexOf(name) == 0){
            result = element.substring(name.length + 1)
        }
    })
    return result
}

console.log(getCookie("email"));


const continue1 = document.querySelector("#continue1")

continue1.addEventListener("click", () =>{
    setCookie("webname", web1.value);
    setCookie("website",web2.value);
    setCookie("phone",phone1.value);
    setCookie("date", Da_te.value);
    setCookie("company", com1.value);

});