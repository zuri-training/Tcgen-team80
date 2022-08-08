    $('.feat-btn').click(function(){
        $('#feat-show').toggleClass("show");
        $('.first').toggleClass("rotate");
      });
      $('.serv-btn').click(function(){
        $('#serv-show').toggleClass("show1");
        $('.second').toggleClass("rotate");
      });

      $('.wrapper .sidebar ul li').click(function(){
        $(this).addClass("active").siblings().removeClass("active");
      });
