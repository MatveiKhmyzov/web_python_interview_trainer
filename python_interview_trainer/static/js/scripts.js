//$(document).ready(function() {
//    var form = $('#ask_form');
//    form.on('submit', function() {
//        $('#asking').addClass('d-none');
//        $('#next').find('.d-none').removeClass('d-none');
//    })
//});
$(function() {
    $("asking").click(function() {
        console.log('kuko')
        $('next').find('.d-none').removeClass('d-none');
    });
});