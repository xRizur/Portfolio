$( function() {
        $( ".sortable" ).sortable();
        $( ".sortable" ).disableSelection();
    } );
function showEditForm(taskId) {
    var form = document.getElementById(`edit-form-${taskId}`);
    form.style.display = 'inline';
}
document.querySelectorAll('.edit-button').forEach(item => {
        item.addEventListener('click', event => {
            let taskItem = event.target.closest('.list-group-item');
            let taskText = taskItem.querySelector('.task-text');
            let editForm = taskItem.querySelector('.edit-form');
            let editInput = taskItem.querySelector('.edit-input');

            taskText.style.display = 'none';
            editForm.style.display = 'block';
            editInput.style.display = 'inline-block';
            editInput.focus();
        });
    });

    document.querySelectorAll('.edit-input').forEach(item => {
        item.addEventListener('focusout', event => {
            event.target.closest('.edit-form').submit();
        });
    });