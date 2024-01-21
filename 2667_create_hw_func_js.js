// 2667. Create Hello World Function
/*
Write a function createHelloWorld. It should return a new function that always returns "Hello World".
*/ 

// Difficulty: Easy

// let createHelloWorld = function() {
//     return function helloWorld(...args) {
//         return "Hello World";
//     }
// };
// Arrow function solution:
// Faster O(N) than previous solution.

let createHelloWorld = function() {
    return () => "Hello World";
};
const args = [{},null,42]
const f = createHelloWorld();
console.log(f(args));