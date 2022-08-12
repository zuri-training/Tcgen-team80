const icon = document.getElementById("burger")
// const page5 = document.querySelector(".")
const menu = document.querySelector(".menunav")
icon.onclick= function() {
    if (menu.style.display == "none") {
        menu.style.display = "flex";
    } else{
        menu.style.display = "none";
    }

};







const App_name1 = document.querySelectorAll(".appName");
const App_name = Array.from(App_name1)
const Web_name = document.querySelector("#webname");
const Company_name = document.querySelector(".companyname");
const Da_te = document.querySelector("#date");
const companyadres = document.querySelector(".comAddress");
const Country = document.querySelector("#country");
const Person_name = document.querySelector("#input individual");
const Contact_email = document.querySelector("#cEmail");
const Contact_web = document.querySelector("#cWeb");
const Contact_social = document.querySelector("#cmedia");
const Contact_number = document.querySelector("#cNum");
const Contact_postmail = document.querySelector("#cpost");
const ContactEmail = document.querySelector(".contactEmail");
const Contactphone = document.querySelector(".contactphone")
const Contacturl = document.querySelector(".contactUrl");
const Contactsocial = document.querySelector(".contactmedia");
const Contactpost = document.querySelector(".contactppost");
const web1 = document.querySelector(".web1");
const web2 = document.querySelector(".web2");
const web3 = document.querySelector(".webname4")
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





const continue1 = document.querySelector("#continue1")

const body3 = document.body

// body3.onload = loadcookie2;



const dateName = document.querySelector(".update");
const item = document.createElement("strong");
item.textcontent = `${getCookie("date")}`;
dateName.append(item.textcontent);

App_name.forEach(appnAme => {
    const itemss = document.createElement("strong");
    itemss.textcontent = `${getCookie("phone")} `;
    appnAme.append(itemss.textcontent)
});

const contactInfo = document.querySelector(".contactinfo");
const item3 = document.createElement("strong");
item3.textcontent1 = `Via this mail: ${getCookie("contactmail")}`;
ContactEmail.append(item3.textcontent1);


const item4 = document.createElement("p");
item4.textcontent = `Via this link: ${getCookie("contactweb")}`;
Contacturl.append(item4.textcontent);

const item5 = document.createElement("p");
item5.textcontent = `Via Social Media: ${getCookie("contactsocial")}`;
Contactsocial.append(item5.textcontent);

const item6 = document.createElement("p");
item6.textcontent = `Via this number: ${getCookie("contactnum")}`;
Contactphone.append(item6.textcontent);

const item7 = document.createElement("p");
item7.textcontent = `Via Postmail: ${getCookie("contactpost")}`;
Contactpost.append(item7.textcontent);

function Passvalue(name, params) {
    var item8 = document.createElement("strong");
    item8.textcontent1 = `${getCookie(`${params}`)}`;
    // console.log(item8.textcontent1);
    name.append(item8.textcontent1);
}

Passvalue(web3,"website")
const continue2 = document.querySelector("#continue2")
const shipping = document.querySelector(".shipping222")

const item8 = document.createElement("strong");
function myfunction(){  
    if (Dot_1.checked) {
        setCookie("q", `${getCookie("dot1")}`);
        console.log(getCookie("q"));
        

    } else if(Dot_2.checked){
        setCookie("q", `${getCookie("dot2")}`);
        console.log(getCookie("q"));
    }else {
        setCookie("q", `${getCookie("dot3")}`);
        console.log(getCookie("q"));
    }

    if (Dot_4.checked){
        setCookie("r", `${getCookie("dot4")}`);
        console.log(getCookie("r"));
    }else if(Dot_5.checked){
        setCookie("r", `${getCookie("dot5")}`);
        console.log(getCookie("r"));   
    }else{
        setCookie("r", `${getCookie("dot6")}`);
        console.log(getCookie("r"));
        
    }
    
    if (Dot_7.checked){
        setCookie("sist", `${getCookie("dot700")}`);
        console.log(getCookie("sist"));
        
    }else{
        setCookie("sist", `${getCookie("dot800")}`);
        console.log(getCookie("sist"));
        
    }

    if (Dot_9.checked){
        setCookie("tinn", `${getCookie("dot900")}`);
        console.log(getCookie("tinn"));
        
    }else{
        setCookie("tinn", `${getCookie("dot1000")}`);
        console.log(getCookie("tinn"));
        
    }

    if (Dot_11.checked){
        setCookie("u", `${getCookie("dot11")}`);
        console.log(getCookie("u"));
        
    }else if(Dot_12.checked){
        setCookie("u", `${getCookie("dot12")}`);
        console.log(getCookie("u"));
        
    }else if(Dot_13.checked){
        setCookie("u", `${getCookie("dot13")}`);
        console.log(getCookie("u"));
        
    }else {
        setCookie("u", `${getCookie("dot14")}`);
        console.log(getCookie("u"));
        
    }
    
    if (Dot_15.checked){
        setCookie("v", `${getCookie("dot15")}`);
        console.log(getCookie("v"));
        
    }else {
        setCookie("v", `${getCookie("dot16")}`);
        console.log(getCookie("v"));
        
    }
};




function myfunction2(){  
    if (Dot_19.checked) {
        
        setCookie("a", `${getCookie("dot19")}`);
        console.log(getCookie("a"));
        

    } else{       
        setCookie("a", `${getCookie("dot29")}`);
        console.log(getCookie("a"));    
    }

    if (Dot_49.checked){
        
        setCookie("b", `${getCookie("dot49")}`);
        console.log(getCookie("b"));
       
    }else{
       
        setCookie("b", `${getCookie("dot59")}`);
        console.log(getCookie("b"));
       
    }
    
    if (Dot_79.checked){
        
        setCookie("c", `${getCookie("dot79")}`);
        console.log(getCookie("c"));
        
        
    }else{
        
        setCookie("c", `${getCookie("dot89")}`);
        console.log(getCookie("c"));

        
    }

    if (Dot_99.checked){
       
        setCookie("k", `${getCookie("dot99")}`);
        console.log(getCookie("k"));

        
    }else{
      
        setCookie("k", `${getCookie("dot109")}`);
        console.log(getCookie("k"));
 
        
    }

    if (Dot_119.checked){
       
        setCookie("e", `${getCookie("dot119")}`);
        console.log(getCookie("e"));

        
    }else{
        
        setCookie("e", `${getCookie("dot129")}`);
        console.log(getCookie("e"));
   
        
    }
};

function myappend(name, content){
    document.getElementById(`${name}`).innerHTML = `${content}`
}




myappend("product123", getCookie("q"));
myappend("product125", getCookie("r"));
myappend("product126", getCookie("sist"));
myappend("product127", getCookie("tinn"));
myappend("product128", getCookie("u"));
myappend("shipping", getCookie("v"));


myappend("product1000", getCookie("a"));
myappend("product1001",getCookie("b"));
myappend("product1002", getCookie("c"));
myappend("product1003",getCookie("k"));
myappend("product1004",getCookie("e"));











 

