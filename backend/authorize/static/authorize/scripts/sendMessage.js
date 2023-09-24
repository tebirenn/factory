const TOKEN = '6673013764:AAHQQjsVIOX0H9SQlO7qYJKYeM4apuIzWyo';
const URL = `https://api.telegram.org/bot${ TOKEN }/sendMessage`;
const formErrorDiv = document.getElementById('form-error');

const sendMessage = () => {
    // event.preventDefault();

    const messageText = document.getElementById('messageText').value;
    const userTgId = document.getElementById('userTgId').value;
    const username = document.getElementById('userUsername').value;
    
    const botMessage = `<b>${username}</b>, я получил от тебя сообщение:\n\n${messageText}`;

    if (messageText.match(/[a-z0-9а-я]+/i)) {
        axios.post(URL, {
            chat_id: userTgId,
            parse_mode: "html",
            text: botMessage
        });
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