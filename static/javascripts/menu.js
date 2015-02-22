(function () {

    const MENU_ACTIVE_TOP = "0px";
    const MENU_INACTIVE_TOP = "-50px";
    var isMenuActive = false;

    function initMenu() {
        $('.icon-menu').click(function () {
            isMenuActive = !isMenuActive;
            $('.header').animate({
                top: isMenuActive? MENU_ACTIVE_TOP : MENU_INACTIVE_TOP
            }, 200);
        });

        $('#page-wrap').click(function () {
            $('.header').animate({
                top: MENU_INACTIVE_TOP
            }, 200);
        });
    }

    $(document).ready(initMenu);

})();
