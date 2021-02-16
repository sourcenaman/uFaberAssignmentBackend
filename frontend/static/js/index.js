
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


function deleteProject(project_id) {
    $.ajax({
        url: "http://127.0.0.1:8000/api/project/" + project_id,
        headers: {'X-CSRFToken': csrftoken},
        type: "DELETE",
        contentType: "application/json",
        success: function(data) {
            window.location.replace("/project");
        }
    });
}


function deleteTask(project_id, task_id) {
    $.ajax({
        url: "http://127.0.0.1:8000/api/project/" + project_id + "/task/" + task_id,
        headers: {'X-CSRFToken': csrftoken},
        type: "DELETE",
        contentType: "application/json",
        success: function(data) {
            window.location.replace("/project/" + project_id + "/task");
        }
    });
}


function deleteSubtask(project_id, task_id, subtask_id) {
    $.ajax({
        url: "http://127.0.0.1:8000/api/project/" + project_id + "/task/" + task_id + "/subtask/" + subtask_id,
        headers: {'X-CSRFToken': csrftoken},
        type: "DELETE",
        contentType: "application/json",
        success: function(data) {
            window.location.replace("/project/" + project_id + "/task/" + task_id + "/subtask");
        }
    });
}

$(document).ready(function () {
    $(".datepicker").datepicker({
        dateFormat: 'yy-mm-dd',//check change
        changeMonth: true,
        changeYear: true
    });
});