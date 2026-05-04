import { createSignal } from 'solid-js'
import "./App.css"

function App() {
    const [result, setResult] = createSignal("")
    
    function callBun() {
        setResult("Bun!")
        console.log("Bun!")
    }

    async function callPython() {
        const response = await window.pywebview.api.callPython()
        setResult(response)
    }
    
    return (
        <div className="app">
            <span class="bigText">Bun X Python!</span>
            <span>This is just a proof of concept. <br/> But it's cool nontheless!</span>
            
            <div className="buttonContainer">
                <button onClick={callBun}>
                    <img src="./bun.svg" alt="Bun Logo"/>
                </button>
                
                <button onClick={callPython}>
                    <img src="./python.svg" alt="Python Logo"/>
                </button>
            </div>
            
            <span>Hello from {result()}</span>
        </div>
    )
}

export default App