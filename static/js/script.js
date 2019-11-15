$(document).ready(function () {
    /* set the date */
    $(function () {
        $('#datetimepicker4').datetimepicker({
            format: 'DD/MM/YYYY',
            maxDate: moment()
        });
    });

    $(function () {
        $('#datetimepicker5').datetimepicker({
            date: moment(),
            format: 'DD/MM/YYYY, HH:mm'
        });
    });


    $(".current-post").on("click", function () {
        let addition_id = $(this).attr("id");
        let currentPath = window.location.pathname;
        currentPath = "/delete_addition/" + addition_id;
        $("#confirm-delete").on("click", function () {
            $(this).attr("href", currentPath).submit();
        });
    });
});