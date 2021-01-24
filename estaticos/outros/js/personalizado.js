$(document).ready(function(){
    $('.data-confirm-inativar').click(function(ev){
        var href = $(this).attr('href');
        if (!$('#modalInativarCartao').length){
            $('body').append('<div class="modal fade" id="modalInativarCartao" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true"><div class="modal-dialog" role="document"><div class="modal-content"><div class="modal-header"><h5 class="modal-title" id="exampleModalLabel">Cartão</h5><button type="button" class="close" data-dismiss="modal" aria-label="Fechar"><span aria-hidden="true">&times;</span></button></div><div class="modal-body">Deseja realmente inativar o cartão?</div><div class="modal-footer"><button type="button" class="btn btn-danger" data-dismiss="modal">Não</button><a class="btn btn-success text-white" id="id">Sim</button></div></div></div></div>');
        }
        $('#id').attr('href',href);
        $('#modalInativarCartao').modal({shown:true});
        return false;
    });
    $('.data-confirm-ativar').click(function(ev){
        var href = $(this).attr('href');
        if (!$('#modalAtivarCartao').length){
            $('body').append('<div class="modal fade" id="modalAtivarCartao" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true"><div class="modal-dialog" role="document"><div class="modal-content"><div class="modal-header"><h5 class="modal-title" id="exampleModalLabel">Cartão</h5><button type="button" class="close" data-dismiss="modal" aria-label="Fechar"><span aria-hidden="true">&times;</span></button></div><div class="modal-body">Deseja realmente ativar o cartão?</div><div class="modal-footer"><button type="button" class="btn btn-danger" data-dismiss="modal">Não</button><a class="btn btn-success text-white" id="id">Sim</button></div></div></div></div>');
        }
        $('#id').attr('href',href);
        $('#modalAtivarCartao').modal({shown:true});
        return false;
    });


});