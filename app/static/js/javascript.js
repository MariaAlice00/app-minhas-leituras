(function(win,doc) {
    'use scrict'

    if (doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel')
        for(let i=0; i<btnDel.length;i++){
            btnDel[i].addEventListener('click', function(event) {
                if(confirm('Deseja mesmo apagar este livro?')){
                    return true
                } else{
                    event.preventDefault()
                }
            })
        }
    }
})(window,document)