$(document).ready( function() {
    var board1 = ChessBoard('board1', {
    
        draggable: true,
        dropOffBoard: 'trash',
        sparePieces: true
    });

    $('#startBtn').on('click', function() {
        board1.start();
        board1.sparePieces = false;
        $.post('/create', 
               {},
                function(data){
                    var parsed_data = JSON.parse(data);
                    alert(parsed_data.gameid);
                    //sse(data.gameid)
                } 
        );
    });
    
    $('#clearBtn').on('click', function() {
        board1.clear()
    });
});

function sse(gameid) {
    var source = new EventSource('/stream/' + gameid);
    source.onmessage = function(e) {
        alert(e);
    };
}