const formErrorDiv = document.getElementById('form-error');
const URL = 'http://localhost:8000/authorize/send/';

const sendMessage = () => {
    const token = localStorage.getItem('access');
    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    const messageText = document.getElementById('messageText').value;

    if (messageText.match(/[a-z0-9а-я]+/i)) {
        axios.post(URL, {messageText}, {headers: {
            Authorization: `Bearer ${token}`,
            'X-CSRFToken': csrfToken
        }});
        document.getElementById('messageText').value = '';
        formErrorDiv.innerHTML = `
            <p class="alert alert-success">Ваше сообщение успешно доставлено!</p>
        `;
    } else {
        formErrorDiv.innerHTML = `
            <p class="alert alert-warning">Сообщение не может быть пустым!</p>
        `;
    }
    
}