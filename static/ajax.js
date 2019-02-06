

$(document).ready(function(){
   
    function processAjaxData(response, urlPath, filename){
            document.title = response;
            window.history.pushState({"html":filename,"pageTitle":response},"/example", urlPath);
    }

// AJAX

    $(document).on('click','.to_playlist',function(e){
        e.preventDefault();
        playlist_name=$(this).text();
        $.ajax({
            url: '/example/my_playlist/'+playlist_name,
            success: function (data) {
                $.getScript("/static/song2.js", function() {
                //         loaded=true;
                        
                });
                dt=$(data).filter('.c').html();
                $('.c').html(dt);
            
            },

        });
        processAjaxData('Music App', '/example/my_playlist/'+playlist_name, '/example/my_playlist/'+playlist_name);
        window.onpopstate = function(e){
        if(e.state){

                $('.c').load(e.state.html+' .c>*');
                document.title = e.state.pageTitle;
            }
        };
    })


    $(document).on('click','.click-album',function(e){
        
        e.preventDefault();

        band_name=($(this).find('h3').text());
        $('.c').load(encodeURI('/example/album/'+band_name)+' .c>*');
        processAjaxData('Music App', '/example/album/'+band_name, '/example/album/'+band_name);
        window.onpopstate = function(e){
        if(e.state){
                $('.c').load(e.state.html+' .c>*');
                document.title = e.state.pageTitle;
            }
        };
	})
	
	$(document).on('click','.click-album',function(e){
        
        e.preventDefault();

        band_name=($(this).find('h3').text());
        $('.c').load(encodeURI('/example/album/'+band_name)+' .c>*');
        processAjaxData('Music App', '/example/album/'+band_name, '/example/album/'+band_name);
        window.onpopstate = function(e){
        if(e.state){
                $('.c').load(e.state.html+' .c>*');
                document.title = e.state.pageTitle;
            }
        };
    })


    $(document).on('click',"#bands",function(e){
        
        e.preventDefault();

        $('.c').load('/example/bands .c>*');
        processAjaxData('Music App', '/example/bands', '/example/bands');
        window.onpopstate = function(e){
        if(e.state){
                $('.c').load(e.state.html+' .c>*');
                document.title = e.state.pageTitle;
            }
        };
    })

$(document).on('click',"#your_playlists",function(e){
        
        e.preventDefault();
		
		$('.c').load('/example/my_playlist .c>*',function(){
			$('.btn').each(function(){
				$(this).addClass('share');
			})
		});
		
		processAjaxData('Music App', '/example/my_playlist', '/example/my_playlist');
		
        window.onpopstate = function(e){
        if(e.state){
                $('.c').load(e.state.html+' .c>*');
                document.title = e.state.pageTitle;
            }
        };
    })


//// DODAWANIE PLAYLISTY AJAX
$(document).on('click',"#add_playlist",function(e){
    e.preventDefault();
    playlist_name=$('#playlist-name').val();
    $.ajax({
        url: "/example/ajaxcreateplaylist",
        data: {
		  'playlist_name': playlist_name,
		  
        },
        success: function (data) {
			// $('.playlist-modal-sm').modal('toggle');
		
            $('.c').load('/example/my_playlist .c>*', function() {
				$('.modal-backdrop').remove();
                $('#message').removeClass().text();
                $('#message').addClass(data.class).text(data.text);
            });
        },
  });
})

$(document).on('click','.share',function(e){
       
	  e.preventDefault();
	  form=$(this).closest('form');
	  user_id_modal=$(this).parent().find('.user_id_modal').val();
	  playlist_title_modal=$(this).parent().find('.playlist_title_modal').val();
	  $.ajax({

		  url: "/example/ajaxshareplaylist",
		  type:'POST',
		  beforeSend: (function(xhr, settings) {
			   if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
				   // Only send the token to relative URLs i.e. locally.
				   xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			   };
		   }),
		  data: {
			'user_id_modal':user_id_modal,
			'playlist_title_modal': playlist_title_modal,
		  },
		  
		  success: function (data) {
				
			  $('#message').removeClass().text();
			  $('#message').addClass(data.class).text(data.text);
		  }
	});
  })

// SONG CAŁY TO KOPIOWANIA - ESTETYKA
    $(document).on('click','.songs',function(e){
       
        e.preventDefault();
        album_name=($(this).find('h3').text());
     
        band_name=($(this).find('.band').text());
        
        $.ajax({
            url: '/example/album/'+band_name+"/"+album_name,
            success: function (data) {
                $.getScript("/static/song2.js", function() {
                //         loaded=true;       
                });
                dt=$(data).filter('.c').html();
                $('.c').html(dt);
              
                // if(!loaded){
                //     $.getScript("/static/Song.js", function() {
                //         loaded=true;
                        
                //      });
                // }
            },

        });
        processAjaxData('Music App', '/example/album/'+band_name+"/"+album_name, '/example/album/'+band_name+"/"+album_name);
        window.onpopstate = function(e){
        if(e.state){
                $('.c').load(encodeURI(e.state.html)+' .c>*');
                document.title = e.state.pageTitle;
                // if(!loaded){
                //     $.getScript("/static/Song.js", function() {
                //         loaded=true;
                //      });
                    
                // }
                // $.getScript("/static/Song.js", function() {
                //         loaded=true;
                //         alert('loaded');
                //      });
            }
        };
    })

    
/////DODAWANIE SONG DO PLAYLIST
    $(document).on('click','.click',function(e){
        e.preventDefault();
        form=$(this).closest('form');
        playlist_id=$(this).closest('form').find('.playlist_id').val();
        song_id=$(this).closest('form').find('.song_id').val();
        $.ajax({
            url: "/example/ajax_song_to_playlist",
            data: {
              'playlist_id': playlist_id,
              'song_id':song_id
            },
            success: function (data) {
				
                $('#message').removeClass().text();
                $('#message').addClass(data.class).text(data.text);
            }
      });
    })

// DO POSTA
    function getCookie(name)
    {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                

                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


/// POST?? DODANIE BAND DO FAVOURITE
    $(document).on('click','.band_name',function(e){
       
         e.preventDefault();
        form=$(this).closest('form');
        band_name=$(this).parent().find('.band_name').val();
        $.ajax({

            url: "/example/ajaxaddfavouritesband",
            type:'POST',
            beforeSend: (function(xhr, settings) {
                 if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                     // Only send the token to relative URLs i.e. locally.
                     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                 };
             }),
            data: {
              'band_name': band_name,
            },
            
            success: function (data) {
				
                $('#message').removeClass().text();
                $('#message').addClass(data.class).text(data.text);
            }
      });
    })
// 
	


    $(document).on('hover',".song-div",function(){
       $(this).find('a').not('.dropp a').animate({
           color:'#767a84',
       },400,function(){
       });
    },function(){
       $(this).find('a').not('.dropp a').animate({
           color:'#89eaed',
       },400,function(){
       });
    });

    $(document).on('hover',".click",function(){
       $(this).animate({
           color:'#767a84',
       },400,function(){
		   
       });
    },function(){
       $(this).animate({
           color:'black',
       },400,function(){
       });
    });

    $(document).on('click',"#playlist a",function(event){
       
       $(".song-div").animate({
           opacity:1,
           backgroundColor:'',
       },400,function(){
       });

       $(this).parent().parent().animate({
           opacity:0.5,
           backgroundColor:'#d2d6d0',
       },400,function(){
       });
    });

    $(document).on('click',".click",function(event){
     event.stopPropagation();
    });

    $('.share_btn').click(function(){
     val=$(this).next().val();
     $('.playlist_title_modal').val(val);
    })

})
