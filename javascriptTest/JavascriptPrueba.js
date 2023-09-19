const jsonData = require('./data.json')


function user() {

    function getByName(name) {
        const data = jsonData;
        const data_filter = data.find(a => a.name === name);
        console.log(data_filter);
    }

    function getAllHobbies(name) {
        if(typeof name !== 'undefined' && name.length > 0){ 
        const data = jsonData;
        const getHobbies = data.find(a => a.name === name);
        console.log('Toma, estos son tus hobbies: ' + getHobbies["interests"].join(', '));
        }
        else console.log('Por favor, tienes que ingresar algun dato')
    }

    return {
        getAllHobbies,
        getByName
    }
}

user().getAllHobbies()