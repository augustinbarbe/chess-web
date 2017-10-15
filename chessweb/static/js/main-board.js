$(document).ready( function() {
    var board1 = ChessBoard('board1', 'start');
    // var board1 = ChessBoard('board1', {
    
    //     draggable: true,
    //     dropOffBoard: 'trash',
    //     sparePieces: true
    // });

    $('#startBtn').on('click', function() {
        board1.start();
        $.post('/create', { 'message' : "empty"} );
    });
    
    $('#clearBtn').on('click', function() {

    });
});