const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const path = require('path')
const url = require('url')

let mainWindow = null

const createWindow = () => {
    mainWindow = new BrowserWindow({width: 800, height: 600})
    mainWindow.loadURL(url.format({
	pathname: path.join(__dirname, 'index.html'),
	protocol: 'file:',
	slashes: true,
    }))
    mainWindow.webContents.openDevTools()
    mainWindow.on('closed', () => {
	mainWindow = null
    })
}

app.on('ready', createWindow)
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
	app.quit()
    }
})
app.on('activate', () => {
    if (mainWindow === null) {
	createWindow()
    }
})

/// zerorpc interconnect
let pyProc = null
let pyPort = null

function selectPort() {
    pyPort = 4242
    return pyPort
}

function createPyProc() {
    let port = '' + selectPort()
    let script = path.join(__dirname, 'pyapp', 'api.py')
    pyProc = require('child_process').spawn('python', [script, port])
    if (pyProc != null) {
	console.log('Child process [' + script + '] is running')
    }
}

function exitPyProc() {
    pyProc.kill()
    pyProc = null
    pyPort = null
}

app.on('ready', createPyProc)
app.on('will-quit', exitPyProc)
