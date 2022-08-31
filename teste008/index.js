function tabuada(){
    let tab=window.document.getElementById('seltab')
    let num=window.document.getElementById('n')
    c=1
    if(num.value.length==0){
        alert('Por favor,digite um número')
    }else{
        tab.innerHTML=''
        while(c<=10){
            let item=window.document.createElement('option')
            let n=Number(num.value)
            item.text=`${n} x ${c} = ${n*c}`
            c++
            tab.appendChild(item)
        }
    }
}