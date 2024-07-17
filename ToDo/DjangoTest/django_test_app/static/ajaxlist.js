$(document).ready(function() {
            $('#task-form').on('submit', function(e) {
                e.preventDefault();
                $.ajax({
                    type: 'POST',
                    url: '',
                    data: $(this).serialize(),
                    success: function(response) {
                        const task = response.task;
                        $('#task-list').append(
                            `<li id="task-${task.id}" class="list-group-item d-flex justify-content-between align-items-center">
                                ${task.title} (Due: ${task.deadline})
                                <button class="btn btn-danger btn-sm" onclick="deleteTask(${task.id})">Delete</button>
                            </li>`
                        );
                        $('#task-form')[0].reset();
                    },
                    error: function(response) {
                        console.log('Error:', response);
                    }
                });
            });
        });

        function deleteTask(taskId) {
            $.ajax({
                type: 'POST',
                url: `delete/${taskId}/`,
                data: {
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(response) {
                    $(`#task-${response.id}`).remove();
                },
                error: function(response) {
                    console.log('Error:', response);
                }
            });
        }