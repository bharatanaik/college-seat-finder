function get_colleges() {
    $(".loader").css("display", "block");
    $.post(
        "college-cutoff/ajax/get-colleges",
        {
            "_type": $("#id_course_category").val()
        },
        function (data, status) {
            $(".loader").css("display", "none");
            var colleges = data["colleges"];
            $("#id_college").empty();
            $("#id_college").prepend("<option>--select--</option>");
            colleges.forEach(element => {
                $("#id_college").prepend(
                    `<option value="${element[1]}">${element[1]} - [${element[0]}] </option>`
                )
            });

        }
    )
}


function get_data() {
    $(".loader").css("display", "block");
    $.post(
        "college-cutoff/ajax/get-data",
        {
            "_college_name": $("#id_college").val(),
            "category": $("#id_category").val(),
            "_round": $("#id_round").val(),
        },
        function (data, status) {
            $(".loader").css("display", "none");
            var courses = data["data"];
            if (courses.length !== 0){
                $("#college_cutoff_table").css("display", "block");
            }
            else{
                $("#college_cutoff_table").css("display", "none");

            }
            $("#course_cutoff").empty();
            $("#college_name").empty();
            $("#college_name").prepend($("#id_college").val());
            courses.forEach(ele => {
                $("#course_cutoff").prepend(`<tr><td>${ele[0]}</td><td>${ele[1]}</td></tr>`);
            });
            $('html, body').animate({
                scrollTop: $("#scroll_to_me").offset().top - $("nav").height() - 20 // minus the nav height
            }, "slow");

        }
    )
}


