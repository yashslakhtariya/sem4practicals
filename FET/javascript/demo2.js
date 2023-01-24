let animal = {
     jumps: null
};

let rabbit = {
     jumps: true,
     __proto__:animal
}

function demo2()
{
     alert("demo");
     alert(rabbit.jumps);
     delete rabbit.jumps;
     alert(rabbit.jumps);
}

console.log(rabbit.jumps);