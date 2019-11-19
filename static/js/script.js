$(document).ready(function () {
    /* Allows the user to set the date of the visit */
    $(function () {
        $('#datetimepicker4').datetimepicker({
            format: 'DD/MM/YYYY',
            maxDate: moment()
        });
    });

    /* Sets and shows current date */
    $(function () {
        $('#datetimepicker5').datetimepicker({
            date: moment(),
            format: 'DD/MM/YYYY, HH:mm'
        });
    });

    /* ".current-post" is the "Yes"-button in the modal that shows when the "Delete"-button is clicked on index.html
    When "Yes" is clicked, the correct post (with the corresponding ID is being deleted. */
    $(".current-post").on("click", function () {
        let addition_id = $(this).attr("id");
        let currentPath = window.location.pathname;
        currentPath = "/delete_addition/" + addition_id;
        $("#confirm-delete").on("click", function () {
            $(this).attr("href", currentPath).submit();
        });
    });
});