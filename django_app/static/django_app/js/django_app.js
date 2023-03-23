$(document).ready(function() {
  $('.btn-read-more').click(function() {
    $(this).parent().find('.news-text').toggle();
    return false;
  });
  $('.news-text').hide();
});
