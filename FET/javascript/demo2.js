let animal = {
     jumps: null
};

let rabbit = Object.create(animal, {
     jumps: true
});

function demo2()
{
     alert("demo");
     alert(rabbit.jumps);
     delete animal.jumps;
     alert(rabbit.jumps);
}