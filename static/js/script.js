$(document).ready(function () {
    /* set the date */
    $(function () {
        $('#datetimepicker4').datetimepicker({
            format: 'L',
            maxDate: moment()
        });
    });
});