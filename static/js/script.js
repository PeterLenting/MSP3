$(document).ready(function () {
    /* set the date */
    $(function () {
        $('#datetimepicker4').datetimepicker({
            format: 'L',
            maxDate: moment()
        });
    });

    $(function () {
        $('#datetimepicker1').datetimepicker({
            date: moment()
        });
    });


    $(document).on("click", ".current-post", function () {
        console.log("event fired")
        var UserName = $(this).attr("id");
        console.log(UserName)
        $("#current").attr("href", "`{{url_for('delete_addition')}} + ${UserName}`");
    });
});