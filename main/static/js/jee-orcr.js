function get_institutes(inst_type) {
    $(".loader").css("display", "block");
    $.post(
        "jee-orcr/ajax/get-institutes",
        {
            "institute_type": inst_type,
            "year": $("#id_academic_year").val()
        },
        function (data, status) {
            $(".loader").css("display", "none");
            institutes = data["institutes"];
            $("#id_institute_name").empty();
            $("#id_institute_name").prepend(`<option>--select--</option>`);
            institutes.forEach(element => {
                $("#id_institute_name").prepend(
                    `<option value="${element}">${element}</option>`
                )
            });
        }
    )
}

document.getElementById("id_academic_year").addEventListener("change", function (e) {
    get_courses();
})

function get_courses() {
    $(".loader").css("display", "block");
    $.post(
        "jee-orcr/ajax/get-courses",
        {
            "institute": $("#id_institute_name").val(),
            "institute_type": $("#id_institute_type").val(),
            "year": $("#id_academic_year").val()
        },
        function (data, status) {
            $(".loader").css("display", "none");
            courses = data["courses"];
            $("#id_course_name").empty();
            $("#id_course_name").prepend(`<option>--select--</option>`);
            courses.forEach(element => {
                $("#id_course_name").prepend(
                    `<option value="${element}">${element}</option>`
                )
            });
        }
    )
}

function get_result() {
    $(".loader").css("display", "block");
    var institute_name = $("#id_institute_name").val();
    var course_name = $("#id_course_name").val();
    var quota = $("#id_quota").val();
    var round = $("#id_round").val();
    var seat_type = $("#id_seat_type").val();
    var gender = $("#id_gender").val();
    var year = $("#id_academic_year").val();

    $.post(
        "jee-orcr/ajax/get-result",
        {
            "year": year,
            "institute": institute_name,
            "course": course_name,
            "quota": quota,
            "round": round,
            "seat_type": seat_type,
            "gender": gender
        },
        function (data, status) {
            $(".loader").css("display", "none");
            $("#id_result").empty();
            $("#id_result").prepend(
                `<div class="card border">
                <h2 class="card-title m-3">${institute_name}</h2>
                <div class="card-body">
                    <h5>${course_name}</h5>
                </div>
                <table class="table">
                    <tbody>
                        <tr>
                            <th>Year</th>
                            <td> ${year}</td>
                        </tr>
                        <tr>
                            <th>Quota</th>
                            <td> ${quota}</td>
                        </tr>
                        <tr>
                            <th>Seat Type</th>
                            <td>${seat_type}</td>
                        </tr>
                        <tr>
                            <th>Gender</th>
                            <td>${gender}</td>
                        </tr>
                        <tr>
                            <th>Round</th>
                            <td>${round}</td>
                        </tr>
                    </tbody>
                </table>
                <hr>
                <table class="table text-center">
                    <thead class="thead-inverse">
                        <tr>
                            <th>Opening Rank</th>
                            <th>Closing Rank</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="fs-4"><b>${data.opening_rank}</b></td>
                            <td class="fs-4"><b>${data.closing_rank}</b></td>
                        </tr>
                    </tbody>
                </table>

                <p class="m-2 text-muted"> If Opening or Closing Rank Contains 'P', it indicates that the
                    corresponding rank is from Preparatory Rank List.</p>
                <p class="m-2 text-muted">Data / Information Courtesy of: JoSAA - Joint Seat Allocation Authority &
                    NIC - National Informatics Centre</p>
            </div>`
            );
            $('html, body').animate({
                scrollTop: $("#scroll_to_me").offset().top - $("nav").height() - 20 // minus the nav height
            }, "slow");
        }
    )
}

function get_college_result() {
    $(".loader").css("display", "block");
    var institute_name = $("#id_institute_name").val();
    var quota = $("#id_quota").val();
    var round = $("#id_round").val();
    var seat_type = $("#id_seat_type").val();
    var gender = $("#id_gender").val();
    var year = $("#id_academic_year").val();

    $.post(
        "jee-orcr/ajax/get-college-result",
        {
            "year": year,
            "institute": institute_name,
            "quota": quota,
            "round": round,
            "seat_type": seat_type,
            "gender": gender
        },
        function (data, status) {
            $(".loader").css("display", "none");
            $("#id_result").css("display", "block");
            var data_list = data["college_orcr"];
            $("#institute_name").text(institute_name);
            $("#result_table").empty();
            data_list.forEach(element => {
                $("#result_table").append(`<tr><td>${element[0]}</td><td>${element[1]}</td><td>${element[2]}</td></tr>`)
            })
            $('html, body').animate({
                scrollTop: $("#scroll_to_me").offset().top - $("nav").height() - 20 // minus the nav height
            }, "slow");
        }
    )
}

function get_course_result() {
    $(".loader").css("display", "block");
    var institute_type = $("#id_institute_type").val();
    var course_name = $("#id_course_name").val();
    var quota = $("#id_quota").val();
    var round = $("#id_round").val();
    var seat_type = $("#id_seat_type").val();
    var gender = $("#id_gender").val();
    var year = $("#id_academic_year").val();

    $.post(
        "jee-orcr/ajax/get-course-result",
        {
            "institute_type":institute_type,
            "year": year,
            "course": course_name,
            "quota": quota,
            "round": round,
            "seat_type": seat_type,
            "gender": gender
        },
        function (data, status) {
            $(".loader").css("display", "none");
            $("#id_result").css("display", "block");
            var data_list = data["course_orcr"];
            $("#course_name").text(course_name);
            $("#result_table").empty();
            data_list.forEach(element => {
                $("#result_table").append(`<tr><td>${element[0]}</td><td>${element[1]}</td><td>${element[2]}</td></tr>`)
            })
            $('html, body').animate({
                scrollTop: $("#scroll_to_me").offset().top - $("nav").height() - 20 // minus the nav height
            }, "slow");
        }
    )
 }




