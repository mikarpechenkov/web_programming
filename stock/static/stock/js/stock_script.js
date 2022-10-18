function express_will(){
    let buttons=document.getElementsByName("wish");

    buttons.forEach(function(el){
        el.addEventListener('click',function(event){
            event.preventDefault();
            if (el.classList.contains('btn-primary')){
                el.innerHTML="Удалить";
                el.classList.remove('btn-primary');
                el.classList.add('btn-danger');
            }else if(el.classList.contains('btn-danger')){
                el.innerHTML="В корзину";
                el.classList.remove('btn-danger');
                el.classList.add('btn-primary');
            }
        })
    });
}