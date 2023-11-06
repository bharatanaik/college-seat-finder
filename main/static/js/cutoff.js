

function get_courses(category_name) {
    $(".loader").css("display", "block");
    $.post(
        "kcet-cutoff/ajax/get-courses",
        {
            "_type": category_name
        },
        function (data, status) {
            $(".loader").css("display", "none");
            var courses = data["courses"];
            $("#id_course").empty();
            $("#id_course").prepend("<option>--select--</option>");
            courses.forEach(element => {
                $("#id_course").prepend(
                    `<option value="${element}">${element}</option>`
                )
            });
        }
    )
}


function get_cutoff_table() {
    var course = $("#id_course").val();
    var rank = $("#id_kcet_rank").val();
    var res_category = $("#id_category").val();
    var round = $("#id_round").val();
    if (course !== '--select--' && rank !== '' && res_category !== '--select--') {
        $(".loader").css("display", "block");
        $.post(
            "kcet-cutoff/ajax/get-data",
            {
                "_course_name": course,
                "rank": rank,
                "category": res_category,
                "_round": round
            },
            function (data, status) {
                $(".loader").css("display", "none");
                $("#scroll_focus").css("display", "block");
                var data_list = data["data"];
                $("#scroll_focus").empty();
                if (data_list.length != 0) {
                    $("#scroll_focus").append(`<h3 class="card p-3">Here are your results:</h3>`)
                    $("#scroll_focus").append(`
                    <div class="table-responsive">
                        <table class="table table-striped table-bordered">
                            <thead>
                                <tr>
                                    <th scope="col">College</th>
                                    <th scope="col">Cutoff</th>
                                    <th scope="col">Code</th>
                                    
                                </tr>
                            </thead>
                            <tbody id="cutoff-data"><tbody>
                        </table>
                    </div>
                    `);

                    data_list.forEach(element => {
                        $("#cutoff-data").append(
                            `<tr>
                                <td>${element[2]}</td>
                                <td> ${element[1]}</td>
                                <td> ${element[0]}</td>

                            </tr>`
                        )
                    })
                }
                else{
                    $("#scroll_focus").append(`<h3 class="card p-3">No Cutoff found!!</h3>`)
                }
                    $('html, body').animate({
                        scrollTop: $("#scroll_focus").offset().top - $("nav").height() - 20// minus the nav height
                    }, "slow");
                }

        )
    }
    else {
        $("#scroll_focus").css("display", "none");
    }
}