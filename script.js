function pegarconsole(){
    let console =document.querySelector('.imagem').getAttribute('data-console')
    document.querySelector('.dive').innerHTML = console
    
}
function trocar(imagem,consolename){
    document.querySelector('.imagem').setAttribute('src',imagem)
    console.log('Apertou')
    document.querySelector('.imagem').setAttribute('data-console',consolename)
    pegarconsole()
    
}

