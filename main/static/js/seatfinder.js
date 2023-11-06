function both() {
    get_districts();
    get_colleges();
}

function get_courses(category_name) {
    $(".loader").css("display", "block");
    $.post(
        "seat-analyser/ajax/get-courses",
        {
            "_course_type": category_name
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

function get_districts() {
    
    $(".loader").css("display", "block");
    $.post(
        "seat-analyser/ajax/get-districts",
        {
            "_course_name": $("#id_course").val()
        },
        function (data, status) {
            $(".loader").css("display", "none");
            var districts = data["districts"];
            $("#id_district").empty();
            $("#id_district").prepend("<option>--select--</option>");
            districts.forEach(element => {
                $("#id_district").prepend(
                    `<option value="${element}">${element}</option>`
                )
            });
        }
    )
}

function get_colleges() {
    $(".loader").css("display", "block");
    $.post(
        "seat-analyser/ajax/get-colleges",
        {
            "_course_name": $("#id_course").val(),
            "_district": $("#id_district").val()
        },
        function (data, status) {
            $(".loader").css("display", "none");
            var colleges = data["colleges"];
            $("#id_college").empty();
            $("#id_college").prepend("<option>--select--</option>");
            colleges.forEach(element => {
                $("#id_college").prepend(
                    `<option value="${element}">${element}</option>`
                )
            });

        }
    )
}

function get_seat_matrix() {
    var college_name = $("#id_college").val();
    var course_name = $("#id_course").val();
    var category = $("#id_reservation").val();

    if(category === "--select--"){
        $("#id_seat_matrix_table").empty();
        return}
    $(".loader").css("display", "block");
    $.post(
        "seat-analyser/ajax/get-seat-matrix",
        {
            "_course_type":$("#id_category").val(),
            "_college_name": college_name,
            "_course_name": course_name,
            "_seat_type":$("#id_seat_type").val()
        },
        function (data, status) {
            if(data["error"]){
                $("#id_seat_matrix_table").empty();
                $("#id_seat_matrix_table").prepend(`
                <div class="card shadow">
                    <div class="card-body">
                        <h1>Not Available</h1>
                    </div>
                </div>
                `);
                
                $(".loader").css("display", "none");
                return
            }
            
            $(".loader").css("display", "none");
            $("#id_seat_matrix_table").empty();
            $("#id_seat_matrix_table").prepend(
                `
                <div class="card shadow">
                    <div class="card-body">
                        <h4 class="card-title">${data["_college_name"]}</h4>
                        <p class="card-text">${data["_course_name"]}</p>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">Accredition: ${data["_accreditation"]}</li>
                        <li class="list-group-item">Affiliation: ${data["_affiliation"]}</li>
                        <li class="list-group-item">Total reserved government seats: <b>${data["_total_reserved_seats"]}</b></li>
                        <li class="list-group-item">Total Management seats: <b>${data["_management"]}</b></li>
                        <li class="list-group-item">Reserved for ${category.toUpperCase()}: <b>${data[category]}</b></li>
                      </ul>
                    <div class="card-body">
                        <b>To Know available management seats, Fees Structure & admission assistance kindly Call or Whatsapp to +919137386752</b>
                    </div>
                </div>
                    `
            )
            $('html, body').animate({
                scrollTop: $("#scroll_to_me").offset().top - $("nav").height() - 20// minus the nav height
            }, "slow");
        }
    )
}



