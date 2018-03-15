const movieGenre = require('./movieGenre').movieGenre;
const assert = require('assert');

function createMovie(){
    return new movie(1, "Buba", 1, 1, 3);
}

function test_construtor(){
    let p = createPokemon();
    assert.deepEqual(p.name, "Buba");
}



