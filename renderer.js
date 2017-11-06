// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

// console.log("entering renderer.js")
const zerorpc = require("zerorpc")
// console.log("required zerorpc")
let client = new zerorpc.Client()
// console.log("instantiated zerorpc client")
client.connect("tcp://127.0.0.1:4242")
// console.log("connected to zerorpc client")

let formula = document.querySelector('#formula')
let result = document.querySelector('#result')
let form = document.querySelector('form')
form.addEventListener('submit', submitForm)

function submitForm(e) {
    e.preventDefault()
    const user_input = formula.value
    client.invoke("calc", formula.value, function(error, res) {
	if(error) {
	    console.error(error)
	} else {
	    result.textContent = res
	}
    })
}
