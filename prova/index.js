function terminar(){
    var opc1=window.document.getElementsByName('opc')
    var opc2=window.document.getElementsByName('opc2')
    var opc3=window.document.getElementsByName('opc3')
    var opc4=window.document.getElementsByName('opc4')
    var opc5=window.document.getElementsByName('opc5')
    var opc6=window.document.getElementsByName('opc6')
    var opc7=window.document.getElementsByName('opc7')
    var opc8=window.document.getElementsByName('opc8')
    var opc9=window.document.getElementsByName('opc9')
    var opc10=window.document.getElementsByName('opc10')
    var msg=window.document.getElementById('msg')
    c=0
    if(opc1[1].checked){
        c++
    }
    if(opc2[0].checked){
        c++
    }
    if(opc3[1].checked){
        c++
    }
    if(opc4[1].checked){
        c++
    }
    if(opc5[1].checked){
        c++
    }
    if(opc6[2].checked){
        c++
    }
    if(opc7[0].checked){
        c++
    }
    if(opc8[3].checked){
        c++
    }
    if(opc9[2].checked){
        c++
    }
    if(opc10[3].checked){
        c++
    }
    msg.innerHTML=`Sua nota é <strong>${c}</strong>.`
    if(c<=5){
        msg.innerHTML+=' Você precisa de <strong>ATENÇÃO</strong>'
    }else{
        msg.innerHTML+=' Você precisa de <strong>NADA,você está ótimo,continue assim.</strong>'
    }
}