function upload_data() {
    var form_data = new FormData();
    form_data.append('file_type', $("#id_type").val());
    form_data.append('upload_file', $("#id_file").get(0).files[0]);
    $.ajax({
        url: "/upload",
        type: 'POST',
        data: form_data,
        cache: false,
        contentType: false,
        enctype: 'multipart/form-data',
        processData: false,
        beforeSend: function(){
            $(".loader").css("display", "block");
        },
        success: function (data, status, jqXHR) {
            $(".loader").css("display", "none");
            $(".alert").css("display", "block");
            $(".alert").html("Data Uploaded Row Count: "+ data["row_length"]);
        },
        error: function (jqXHR, status, error) {
            $(".loader").css("display", "none");
            $(".alert").css("display", "block");
            $(".alert").html("ERROR");        
        }
    });
}