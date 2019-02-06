$(document).ready(function () {
	init();
	function init(){


		var audio = $('#audio');

		// ????????????????????????
		var playlistt = $('#playlist');
		

		var footer=$('.footer');

		var tracks = playlistt.find('tr.td.a');
		var len = tracks.length - 1;

		audio[0].volume = .10;
		audio[0].play();

		
      $( ".sortable" ).sortable({
          revert: true,
          stop:function(e,tr){
          	current=tr.item.find('.play').parent().index('td.title');
          },
        });
        $( "#draggable" ).draggable({
          connectToSortable: ".sortable",
      
          revert: "invalid"
        });
        $( "tr, tbody" ).disableSelection();
	     

		playlistt.on('click','.play', function(e){
			e.preventDefault();
			
			// ????????????????????????
			playlst.playlist = $('#playlist');
			playlist=playlst.playlist; 
			
			link = $(this);

			current = link.parent().index('td.title');
			run(link, audio[0]);
		});

		audio[0].addEventListener('ended',function(e){
			current++;
		
			if(current == len){
				current = 0;
				link = playlist.find('a.title')[0];
			}else{
				link = playlist.find('a.title')[current];    

			}
			run($(link),audio[0]);
		});
	}

	function run(link, player){
			$('#current').empty();
			$('#current').append("Playing: ");
			player.src = link.attr('href');
			par = link.parent();
			
			player.load();
			player.play();
			text=link.text()
			t=link.text(text.replace(/\_/g,' '))
			$('#current').append('<b>'+t.text()+'</b>');
			
	}
});