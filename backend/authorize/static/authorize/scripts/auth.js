const userCreateAndGetURL = 'http://localhost:8000/authorize/api/token/user/';
const authURL = 'http://localhost:8000/authorize/api/token/';
const formErrorDivReg = document.getElementById('form-error-reg');


const regUser = (event) => {
    event.preventDefault();
    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    const first_name = document.getElementById('id_first_name').value;
    const username = document.getElementById('id_username').value;
    const password1 = document.getElementById('id_password1').value;
    const password2 = document.getElementById('id_password2').value;

    if (!username.match(/^[a-z0-9]+$/i)) {
        formErrorDivReg.innerHTML = '<p class="alert alert-warning">Некорректное имя пользователя</p>';
        return;
    } else if (!first_name.match(/^[a-zа-я]+$/i)) {
        formErrorDivReg.innerHTML = '<p class="alert alert-warning">Некорректное имя</p>';
        return;
    } else if (!password1.match(/[a-zа-я]/) || !password1.match(/[A-ZА-Я]/) || !password1.match(/[0-9]/) || password1.length < 8) {
        formErrorDivReg.innerHTML = '<p class="alert alert-warning">Пароль должен состоять из букв и цифр, а так же длиной не менее 8 символов</p>';
        return;
    } else if (password1 != password2) {
        formErrorDivReg.innerHTML = '<p class="alert alert-warning">Пароли не совподают</p>';
        return;
    }

    axios.post(userCreateAndGetURL, {username, first_name, password: password1}, {headers: {'X-CSRFToken': csrfToken,}})
    .then((data) => {
        location.replace('http://localhost:8000/authorize/signin/');
    })
    .catch((error) => {
        if (error.response.data.username) {
            formErrorDivReg.innerHTML = `<p class="alert alert-warning">Пользователь уже существует</p>`;
        }        
    });
}


const authUser = (event) => {
    event.preventDefault();

    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    const username = document.getElementById('id_username').value;
    const password = document.getElementById('id_password').value;

    axios.post(authURL, {username, password}, {headers: {'X-CSRFToken': csrfToken,}})
    .then((data) => {
        localStorage.setItem('access', data.data.access);
        localStorage.setItem('refresh', data.data.refresh);
        location.replace('http://localhost:8000/authorize/');
    });
}


const getUserData = () => {
    const token = localStorage.getItem('access');
    console.log(token);
    axios.get(userCreateAndGetURL, {headers: {Authorization: `Bearer ${token}`}})
    .then(data => {
        console.log(data);
        document.getElementById('header-left').innerHTML = `
            <span class="badge badge-light username me-3" id="header-username">${data.data.username}</span>
            <button class="btn btn-primary px-4" onclick="signOut()">Выйти</button>  
        `
        document.getElementById('home-user-first-name').innerHTML = data.data.first_name;

        if (!data.data.tg_id) {
            document.getElementById('tg-error').style.display = 'block';
            document.getElementById('messageText').disabled = true;
            document.getElementById('sendMButton').disabled = true;
        }
    }).catch((error) => {
        console.log(error);
        document.getElementById('header-left').innerHTML = `
            <a 
                href="/authorize/signin" 
                class="btn btn-light me-3 px-4 fw-bold"
            >Войти</a>
            <a 
                href="/authorize/signup" 
                class="btn btn-light px-4 fw-bold"
            >Зарегистрироваться</a>
        `
        location.replace('http://localhost:8000/authorize/signin/');
    });
}


const signOut = () => {
    localStorage.clear();
    location.reload();
}


const checkUser = () => {
    const token = localStorage.getItem('access');
    console.log('abc', token)
    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    
    axios.post(
        'http://localhost:8000/authorize/api/token/verify/',
        {token}
    ).then((data) => {
        location.replace('http://localhost:8000/authorize/');
    }).catch((error) => {
        document.getElementById('header-left').innerHTML = `
            <a 
                href="/authorize/signin" 
                class="btn btn-light me-3 px-4 fw-bold"
            >Войти</a>
            <a 
                href="/authorize/signup" 
                class="btn btn-light px-4 fw-bold"
            >Зарегистрироваться</a>
        `
    });
}