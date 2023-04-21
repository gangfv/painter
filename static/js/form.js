const form = document.getElementById('form');
form.addEventListener('submit', getFormValue);

function getFormValue(event) {
    event.preventDefault();
    const email = form.querySelector('[name="email"]')
    const name = form.querySelector('[name="name"]')
    const number = form.querySelector('[name="number"]')
    const data = {
        email: email.value,
        name: name.value,
        number: number.value,
    }
    console.log(data);
    axios.post('/form/', data)
    window.location.reload();
}