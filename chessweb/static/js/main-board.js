$(document).ready( function() {
    var board1 = ChessBoard('board1', {
    
        draggable: true,
        dropOffBoard: 'trash',
        sparePieces: true
    });

    $('#startBtn').on('click', function() {
        board1.start();
        board1.sparePieces = false;
        $.post('/create', { 'message' : "empty"} );
    });
    
    $('#clearBtn').on('click', function() {
        board1.clear()
    });
});