// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

console.log("entering renderer.js")
const zerorpc = require("zerorpc")
// console.log("required zerorpc")

let formula = document.querySelector('#formula')
let result = document.querySelector('#result')
let resultText = document.createTextNode('')
result.appendChild(resultText)
let initialized = false

function update_func(result, reply) {
    console.log("update:"+result)
    resultText.textContent = result
    reply(null, formula.value)
}

let server = new zerorpc.Server({
    update: update_func
})
console.log("instantiated zerorpc server")

server.bind("tcp://0.0.0.0:4242")
console.log("bound to port 4242")
