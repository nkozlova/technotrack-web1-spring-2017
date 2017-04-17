$(document).ready(function() {
    function updateContent() {
        $('.autorefresh').each(function () {
            var el = $(this);
            el.load(el.data('url'));
        });
    }

    updateContent();

    window.setInterval(updateContent, 1000);

    $('.likebutton').click(function() {
            $.ajax({
                url: $('.likebutton').data('url'),
                success: function (data) {
                    $('.likescount').html(data);
                }
            });
            //$(".likebutton").hide();
        }
    );

    $(document).on('click', '.post-edit-link', function() {
        $(".dlgbody").load($(this).attr('href'), function() {
            dlg.dialog({buttons: {"Сохранить" : function() {
                dlg.find("form").submit();
                dlg.dialog("close");
            }}});
            dlg.dialog("open");
            dlg.dialog({width : $(".dlgbody").outerWidth(true) + 40, height:$(".dlgbody").outerHeight(true) + 165});
        });
        return false;
    });

    var dlg = $(".dialog").dialog({width:500, height:500, autoOpen:false, title: 'Редактирование поста'});

    $('select').chosen();

});